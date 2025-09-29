"""
QA Log router
-------------
Endpoints for storing and retrieving chat history.

Why not store `answer_text` as a DB column?
- We avoid a migration for now (production safety). Instead, we embed
  `answer_text` inside `dsl_json` under the key `answer_text`.
  The response schema still surfaces `answer_text` directly for the UI.
"""

from __future__ import annotations

from datetime import datetime
from typing import List

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import desc
from sqlalchemy.orm import Session

from app.database import get_db
from app import models
from app.schemas import QaLogEntry, QaLogCreate
from app.deps import get_current_user


router = APIRouter(prefix="/qa-log", tags=["qa-log"])


@router.get("/{workspace_id}", response_model=list[QaLogEntry])
def get_log(
    workspace_id: str,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
    limit: int = Query(20, ge=1, le=200),
):
    """
    Fetch latest QA interactions for a workspace.
    Sorted by newest first.
    Security: require current user and ensure workspace match.
    """
    if str(current_user.workspace_id) != str(workspace_id):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")

    rows: List[models.QaQueryLog] = (
        db.query(models.QaQueryLog)
        .filter(models.QaQueryLog.workspace_id == workspace_id)
        .order_by(desc(models.QaQueryLog.created_at))
        .limit(limit)
        .all()
    )

    out: List[QaLogEntry] = []
    for r in rows:
        dsl = r.dsl_json or {}
        out.append(
            QaLogEntry(
                id=str(r.id),
                question_text=r.question_text,
                answer_text=(dsl.get("answer_text") if isinstance(dsl, dict) else None),
                dsl_json=dsl,
                created_at=r.created_at,
            )
        )
    return out


@router.post("/{workspace_id}", response_model=QaLogEntry)
def create_log(
    workspace_id: str,
    entry: QaLogCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    """
    Store a new QA log entry. For now, store `answer_text` inside `dsl_json`
    to avoid a migration. When we introduce a dedicated column later, this API
    won't need to change.
    """
    if str(current_user.workspace_id) != str(workspace_id):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")

    dsl_payload = entry.dsl_json or {}
    if isinstance(dsl_payload, dict):
        dsl_payload.setdefault("answer_text", entry.answer_text)

    log = models.QaQueryLog(
        workspace_id=workspace_id,
        user_id=current_user.id,
        question_text=entry.question_text,
        dsl_json=dsl_payload,
        created_at=datetime.utcnow(),
    )
    db.add(log)
    db.commit()
    db.refresh(log)

    return QaLogEntry(
        id=str(log.id),
        question_text=log.question_text,
        answer_text=entry.answer_text,
        dsl_json=dsl_payload,
        created_at=log.created_at,
    )



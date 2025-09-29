"""
QA Router
---------
Thin controller that accepts a user question, delegates to QAService,
and returns a structured result with both human-readable answer and DSL.
"""

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.schemas import QARequest, QAResult
from app.services.qa_service import QAService
from app.services.metric_service import MetricService
from app.database import get_db


router = APIRouter(prefix="/qa", tags=["qa"])


@router.post("/", response_model=QAResult)
def ask_question(
    req: QARequest,
    workspace_id: str = Query(..., description="Workspace context for scoping queries"),
    db: Session = Depends(get_db),
):
    """
    POST /qa
    Input:  { "question": "Why is my CVR down this week?" }
    Output: { "answer": "...", "executed_dsl": {...}, "data": {...} }

    WHY workspace_id param?
    - Ensures tenant scoping
    - Prevents cross-workspace data leaks
    """
    metric_service = MetricService(db)
    qa_service = QAService(metric_service)

    try:
        return qa_service.answer(req.question, workspace_id)
    except Exception as exc:  # noqa: BLE001
        raise HTTPException(status_code=400, detail=str(exc))



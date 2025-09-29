"""
QA Service
----------
Responsibilities:
1) Translate a natural language question → JSON DSL (MetricQuery) using OpenAI
2) Validate with Pydantic (reject invalid JSON)
3) Execute DSL via MetricService
4) Build a concise human-readable answer

Why a separate service file?
- Separation of concerns: keeps the /qa route thin
- Extensibility: room for multi-step reasoning, safety checks, logging
- Testability: can unit-test translation and execution separately
"""

from __future__ import annotations

import json
from typing import Dict, Any

from openai import OpenAI

from app.schemas import MetricQuery
from app.services.metric_service import MetricService
from app.deps import get_settings
from app import models
from datetime import datetime


class QAService:
    def __init__(self, metric_service: MetricService):
        settings = get_settings()
        # Keep client creation here so it can be mocked in tests and picks up env on startup.
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)
        self.metric_service = metric_service

    def _build_prompt(self, question: str) -> str:
        """
        System prompt constrains the LLM to emit ONLY valid JSON matching our DSL.
        We do not allow free text. This minimizes injection risk and hallucinations.
        """
        return f"""
You are a translator that converts marketing analytics questions into a JSON object following this schema:

{{
  "metric": "spend|revenue|clicks|impressions|conversions|roas|cpa|cvr",
  "time_range": {{ "last_n_days": int }} OR {{ "start": "YYYY-MM-DD", "end": "YYYY-MM-DD" }},
  "compare_to_previous": true|false,
  "group_by": "none|campaign|adset|ad",
  "filters": {{ "provider": string|null, "entity_ids": [uuid]|null, "level": "campaign|adset|ad"|null }}
}}

Return ONLY valid JSON. No explanation text. Example:
{{ "metric": "roas", "time_range": {{ "last_n_days": 7 }}, "compare_to_previous": true, "group_by": "campaign", "filters": {{}} }}

User question: "{question}"
"""

    def translate_to_dsl(self, question: str) -> MetricQuery:
        """Call OpenAI to translate the question into a MetricQuery DSL object."""
        prompt = self._build_prompt(question)
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You only output valid JSON DSL."},
                {"role": "user", "content": prompt},
            ],
            temperature=0,
        )
        raw = response.choices[0].message.content.strip()
        try:
            dsl_dict = json.loads(raw)
        except Exception as exc:  # noqa: BLE001
            raise ValueError(f"Failed to parse JSON from LLM: {raw}") from exc
        return MetricQuery(**dsl_dict)

    def answer(self, question: str, workspace_id: str, db=None, user_id=None) -> Dict[str, Any]:
        """
        1) Translate → DSL (Pydantic-validated)
        2) Execute DSL via MetricService
        3) Build human-readable summary
        """
        dsl = self.translate_to_dsl(question)

        result = self.metric_service.execute(query=dsl, workspace_id=workspace_id)

        answer = f"Your {dsl.metric.upper()} for the selected period is {result.get('summary')} ."
        if dsl.compare_to_previous and isinstance(result.get("delta"), (int, float)):
            answer += f" That is a {round(result['delta'], 2)}% change vs previous."

        # Persist query log for history. We avoid schema changes by embedding
        # the answer text inside dsl_json (under key `answer_text`).
        if db is not None:
            dsl_payload = dsl.model_dump()
            dsl_payload["answer_text"] = answer
            try:
                log = models.QaQueryLog(
                    workspace_id=workspace_id,
                    user_id=user_id if user_id else None,  # attach if available
                    question_text=question,
                    dsl_json=dsl_payload,
                    created_at=datetime.utcnow(),
                )
                db.add(log)
                db.commit()
            except Exception:
                db.rollback()

        return {
            "answer": answer,
            "executed_dsl": dsl,
            "data": result,
        }



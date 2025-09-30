"""
QA Telemetry Logging
====================

Structured logging for QA system observability.

Related files:
- app/services/qa_service.py: Calls log_qa_run() on every query
- app/models.py: QaQueryLog table
- app/telemetry/eval.py: Reads logs for offline evaluation (Phase 6)

Design:
- Every QA run is logged (success or failure)
- Logs include: question, DSL, validity, latency, errors
- Stored in database for historical analysis
- Structured for easy querying and metrics
"""

from __future__ import annotations

import logging
from datetime import datetime
from typing import Optional, Dict, Any

from sqlalchemy.orm import Session

from app import models


# Set up Python logger for console output
logger = logging.getLogger(__name__)


def log_qa_run(
    db: Session,
    workspace_id: str,
    question: str,
    dsl: Optional[Dict[str, Any]],
    success: bool,
    latency_ms: int,
    user_id: Optional[str] = None,
    error_message: Optional[str] = None,
    answer_text: Optional[str] = None
) -> None:
    """
    Log a QA query run to the database.
    
    Args:
        db: Database session
        workspace_id: Workspace UUID
        question: Original user question
        dsl: Validated DSL dict (None if validation failed)
        success: Whether the query succeeded
        latency_ms: Total latency in milliseconds
        user_id: User UUID (optional)
        error_message: Error message if failed (optional)
        answer_text: Generated answer text (optional)
        
    Side effects:
        - Inserts record into qa_query_logs table
        - Commits the transaction (or rolls back on error)
        
    Design notes:
    - We embed answer_text in dsl_json to avoid schema changes
    - error_message helps debug failures
    - latency_ms enables performance monitoring
    - success flag enables success rate tracking
    
    Related:
    - Called by: app/services/qa_service.py
    - Stored in: app/models.QaQueryLog
    """
    try:
        # Build payload for dsl_json column
        dsl_payload = dsl.copy() if dsl else {}
        
        # Embed answer and metadata
        if answer_text:
            dsl_payload["answer_text"] = answer_text
        if error_message:
            dsl_payload["error_message"] = error_message
        dsl_payload["success"] = success
        dsl_payload["latency_ms"] = latency_ms
        
        # Create log record
        log_entry = models.QaQueryLog(
            workspace_id=workspace_id,
            user_id=user_id,
            question_text=question,
            dsl_json=dsl_payload,
            created_at=datetime.utcnow(),
            duration_ms=latency_ms
        )
        
        db.add(log_entry)
        db.commit()
        
        # Also log to console for real-time monitoring
        logger.info(
            f"QA run logged: workspace={workspace_id}, "
            f"success={success}, latency={latency_ms}ms, "
            f"question='{question[:50]}...'"
        )
        
    except Exception as e:
        logger.error(f"Failed to log QA run: {str(e)}")
        db.rollback()
        # Don't propagate error - logging failure shouldn't break QA


def get_qa_stats(db: Session, workspace_id: str, days: int = 30) -> Dict[str, Any]:
    """
    Get QA statistics for a workspace.
    
    Args:
        db: Database session
        workspace_id: Workspace UUID
        days: Number of days to analyze
        
    Returns:
        Dict with:
            - total_queries: Total number of queries
            - success_rate: Percentage of successful queries
            - avg_latency_ms: Average latency
            - common_errors: List of common error messages
            
    Use cases:
    - Dashboard metrics
    - Quality monitoring
    - Performance tracking
    
    Related:
    - Data source: app/models.QaQueryLog
    - Used by: Admin dashboard (future)
    """
    from datetime import timedelta
    
    cutoff = datetime.utcnow() - timedelta(days=days)
    
    logs = (
        db.query(models.QaQueryLog)
        .filter(models.QaQueryLog.workspace_id == workspace_id)
        .filter(models.QaQueryLog.created_at >= cutoff)
        .all()
    )
    
    if not logs:
        return {
            "total_queries": 0,
            "success_rate": 0.0,
            "avg_latency_ms": 0,
            "common_errors": []
        }
    
    total = len(logs)
    successes = sum(
        1 for log in logs 
        if log.dsl_json and log.dsl_json.get("success", False)
    )
    
    latencies = [
        log.duration_ms for log in logs 
        if log.duration_ms is not None
    ]
    avg_latency = sum(latencies) / len(latencies) if latencies else 0
    
    # Extract error messages
    errors = [
        log.dsl_json.get("error_message")
        for log in logs
        if log.dsl_json and log.dsl_json.get("error_message")
    ]
    
    # Count error frequency
    error_counts = {}
    for error in errors:
        error_counts[error] = error_counts.get(error, 0) + 1
    
    common_errors = sorted(
        error_counts.items(),
        key=lambda x: x[1],
        reverse=True
    )[:5]  # Top 5 errors
    
    return {
        "total_queries": total,
        "success_rate": (successes / total * 100) if total > 0 else 0.0,
        "avg_latency_ms": int(avg_latency),
        "common_errors": [
            {"message": msg, "count": count}
            for msg, count in common_errors
        ]
    }

"""
Telemetry Module
================

Structured logging and observability for QA system.

WHY telemetry?
- Monitor LLM translation success/failure rates
- Track query latency and performance
- Log DSL validity for improvement
- Enable offline evaluation and debugging

Module structure:
- logging.py: Structured logging for QA runs
- eval.py: Offline evaluation harness (Phase 6)

Related modules:
- app/services/qa_service.py: Logs every QA run
- app/models.py: QaQueryLog table for persistence
"""

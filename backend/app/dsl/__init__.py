"""
DSL (Domain-Specific Language) Module
======================================

This module provides a safe, validated query language for metrics.

WHY DSL?
- Prevents LLM from generating arbitrary SQL or breaking the database
- Ensures backend is the single source of truth for metrics calculations
- Provides clear validation boundaries and error messages
- Enables deterministic query execution

Module structure:
- schema.py: Pydantic models defining the DSL contract
- canonicalize.py: Synonym and time phrase normalization
- validate.py: Validation and repair logic
- planner.py: Converts DSL into execution plans
- executor.py: Executes plans via SQLAlchemy
- examples.md: Few-shot examples for LLM prompts

Related modules:
- app/services/metric_service.py: Legacy metric aggregation (being phased out)
- app/nlp/translator.py: LLM-based natural language → DSL translation
- app/routers/qa.py: HTTP endpoint for question answering
"""

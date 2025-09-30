"""
NLP (Natural Language Processing) Module
========================================

Handles translation of natural language questions into validated DSL queries.

WHY separate from DSL?
- Separation of concerns: NLP deals with LLM interaction, DSL deals with structure
- Testability: Can mock LLM calls without touching DSL validation
- Swappability: Can replace OpenAI with other providers without changing DSL

Module structure:
- translator.py: Main translation orchestrator (LLM → DSL)
- prompts.py: System prompts and few-shot examples

Related modules:
- app/dsl/schema.py: Target DSL structure
- app/dsl/canonicalize.py: Pre-processing before LLM call
- app/dsl/validate.py: Post-processing after LLM response
- app/services/qa_service.py: High-level orchestrator
"""

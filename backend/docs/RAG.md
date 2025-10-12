example flow

VRAAG
  ↓
[RAG]
  Zoek extra info:
   - Betekenis van “ROAS”
   - Tijd: September → 2025-09-01–09-30
   - “Holiday campaign” → entity_id = 123
  ↓
[LLM → DSL]
  Bouw valide DSL met die kennis
  ↓
[Validator + Executor]
  Query draait, facts komen terug
  ↓
[Answer Builder]
  Bouwt natuurlijk antwoord

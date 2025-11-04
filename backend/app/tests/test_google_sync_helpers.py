"""Unit tests for small helpers in google_sync router.

WHAT: Validate date chunking and customer ID normalization.
WHY: Keeps important logic covered without full HTTP stack.
REFERENCES: app/routers/google_sync.py
"""

from datetime import date

from app.routers.google_sync import _compute_date_chunks, _normalize_customer_id


def test_normalize_customer_id_strips_non_digits():
    assert _normalize_customer_id("123-456-7890") == "1234567890"
    assert _normalize_customer_id("  999  ") == "999"
    assert _normalize_customer_id("abc123") == "123"


def test_compute_date_chunks_week_sized():
    s = date(2024, 10, 1)
    e = date(2024, 10, 15)
    chunks = _compute_date_chunks(s, e, 7)
    # Expect: 1-7, 8-14, 15-15
    assert chunks[0] == (date(2024, 10, 1), date(2024, 10, 7))
    assert chunks[1] == (date(2024, 10, 8), date(2024, 10, 14))
    assert chunks[2] == (date(2024, 10, 15), date(2024, 10, 15))
    assert len(chunks) == 3


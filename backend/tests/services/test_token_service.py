"""
Unit tests for token_service (Phase 2.1).

WHAT:
    Validates encryption + persistence wiring for provider tokens.
WHY:
    Ensures connections receive encrypted tokens and updates work as expected.
REFERENCES:
    - backend/app/services/token_service.py
    - docs/living-docs/META_INTEGRATION_STATUS.md
"""

from datetime import datetime, timedelta
from uuid import uuid4
from unittest.mock import Mock

from sqlalchemy.orm import Session

from app.models import Connection, ProviderEnum
from app.security import decrypt_secret
from app.services.token_service import store_connection_token


def _build_connection() -> Connection:
    """Helper to build a Connection instance for tests."""
    return Connection(
        id=uuid4(),
        provider=ProviderEnum.meta,
        external_account_id="act_123456",
        name="Test Meta Account",
        status="active",
        workspace_id=uuid4(),
    )


def test_store_connection_token_encrypts_and_links():
    """New tokens should be encrypted and linked to the connection."""
    db = Mock(spec=Session)
    db.flush.return_value = None

    connection = _build_connection()
    access_token = "plain-access-token"

    token = store_connection_token(
        db,
        connection,
        access_token=access_token,
        scope="system-user",
        ad_account_ids=["act_123456"],
    )

    assert token.access_token_enc != access_token
    assert connection.token is token
    assert decrypt_secret(token.access_token_enc, context="test:access") == access_token
    db.flush.assert_called_once()


def test_store_connection_token_updates_existing():
    """Updates should rotate ciphertext and preserve metadata."""
    db = Mock(spec=Session)
    db.flush.return_value = None

    connection = _build_connection()
    original_token = store_connection_token(
        db,
        connection,
        access_token="first-token",
        scope="initial",
    )
    first_cipher = original_token.access_token_enc

    # Simulate DB session clean slate between calls.
    db.flush.reset_mock()

    updated_token = store_connection_token(
        db,
        connection,
        access_token="second-token",
        refresh_token="refresh-token",
        expires_at=datetime.utcnow() + timedelta(days=30),
        scope="updated",
        ad_account_ids=["act_123456", "act_654321"],
    )

    assert updated_token is original_token
    assert updated_token.access_token_enc != first_cipher
    assert decrypt_secret(updated_token.access_token_enc, context="test:update") == "second-token"
    assert decrypt_secret(updated_token.refresh_token_enc, context="test:update-refresh") == "refresh-token"
    assert updated_token.ad_account_ids == ["act_123456", "act_654321"]
    db.flush.assert_not_called()

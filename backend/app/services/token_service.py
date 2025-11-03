"""Token service for encrypting and persisting provider credentials.

WHAT:
    Wraps the low-level encryption helpers introduced in Phase 2.1 and
    encapsulates how tokens are attached to connections.

WHY:
    - Keeps encryption logic out of routers.
    - Simplifies future OAuth callback handling.

REFERENCES:
    - docs/living-docs/META_INTEGRATION_STATUS.md (Phase 2.1 roadmap)
    - backend/app/security.py (encrypt_secret / decrypt_secret)
"""

from __future__ import annotations

from datetime import datetime
import logging
from typing import Optional, Sequence

from sqlalchemy.orm import Session

from app.models import Connection, Token
from app.security import encrypt_secret

logger = logging.getLogger(__name__)


def store_connection_token(
    db: Session,
    connection: Connection,
    *,
    access_token: str,
    refresh_token: Optional[str] = None,
    expires_at: Optional[datetime] = None,
    scope: Optional[str] = None,
    ad_account_ids: Optional[Sequence[str]] = None,
) -> Token:
    """Encrypt and persist tokens for a connection.

    WHAT:
        Creates or updates the `Token` row referenced by the given connection.
    WHY:
        Centralizes encryption + persistence so Phase 3/7 flows can reuse it.
    REFERENCES:
        backend/app/routers/meta_sync.py (consumes decrypted tokens)

    Returns:
        The Token ORM instance associated with the connection.
    """
    label = f"{connection.provider.value}:{connection.external_account_id}"
    encrypted_access = encrypt_secret(access_token, context=f"{label}:access")
    encrypted_refresh = (
        encrypt_secret(refresh_token, context=f"{label}:refresh") if refresh_token else None
    )

    if connection.token:
        token = connection.token
        token.access_token_enc = encrypted_access
        token.refresh_token_enc = encrypted_refresh
        token.expires_at = expires_at
        token.scope = scope
        token.ad_account_ids = list(ad_account_ids) if ad_account_ids else None
        logger.info("[TOKEN_SERVICE] Updated encrypted token for %s", label)
    else:
        token = Token(
            provider=connection.provider,
            access_token_enc=encrypted_access,
            refresh_token_enc=encrypted_refresh,
            expires_at=expires_at,
            scope=scope,
            ad_account_ids=list(ad_account_ids) if ad_account_ids else None,
        )
        db.add(token)
        db.flush()
        connection.token_id = token.id
        connection.token = token
        logger.info("[TOKEN_SERVICE] Created encrypted token for %s", label)

    db.add(connection)
    return token

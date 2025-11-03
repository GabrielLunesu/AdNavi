"""Pytest configuration shared across backend tests.

WHAT:
    - Ensures backend package importability (`import app` works)
    - Provides deterministic security configuration for test runs.
WHY:
    Phase 2.1 token encryption requires `TOKEN_ENCRYPTION_KEY` at import time.
REFERENCES:
    - backend/app/security.py
"""

import os
import sys
from pathlib import Path

from cryptography.fernet import Fernet

# Make sure the backend package (containing `app/`) is importable.
BACKEND_ROOT = Path(__file__).resolve().parents[1]
if str(BACKEND_ROOT) not in sys.path:
    sys.path.insert(0, str(BACKEND_ROOT))

# Ensure JWT + token encryption secrets exist for the test process.
os.environ.setdefault("JWT_SECRET", "test-jwt-secret")
os.environ.setdefault("TOKEN_ENCRYPTION_KEY", Fernet.generate_key().decode())

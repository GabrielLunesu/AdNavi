# AdNavi Backend (FastAPI + PostgreSQL + SQLAlchemy + Alembic)

This service provides email/password authentication using JWT stored in an HTTP-only cookie, backed by PostgreSQL. It is designed to work with the AdNavi Next.js frontend at `http://localhost:3000`.

## Prerequisites
- Python 3.11+
- Docker (for PostgreSQL)
- A virtual environment (recommended)

## .env
Create a `.env` file in this directory with the following keys:

```
# JWT
JWT_SECRET=change_me_in_prod
JWT_EXPIRES_MINUTES=10080

# DB (match docker-compose service, user, pass, db)
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_USER=adnavi
POSTGRES_PASSWORD=adnavi
POSTGRES_DB=adnavi

# SQLAlchemy URL (sync driver)
DATABASE_URL=postgresql+psycopg2://adnavi:adnavi@localhost:5432/adnavi

# CORS / Cookies
BACKEND_CORS_ORIGINS=http://localhost:3000
COOKIE_DOMAIN=localhost
```

## Start DB
```bash
cd backend
docker compose up -d
```

## Install Dependencies
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run Migrations
```bash
alembic upgrade head
```

## Seed Mock Data (Optional)
To populate the database with test data for development:
```bash
python -m app.seed_mock
```

This creates:
- Workspace: "Defang Labs"
- Users: owner@defanglabs.com / viewer@defanglabs.com (password: password123)
- Mock connection with entity hierarchy (2 campaigns > 4 adsets > 8 ads)
- 30 days of metric data (240 records)
- P&L snapshots with calculated CPA/ROAS

View the data at: http://localhost:8000/admin

## Run API
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## Test
```bash
# Register
curl -X POST http://localhost:8000/auth/register \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"password123"}'

# Login (sets cookie)
curl -i -X POST http://localhost:8000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"password123"}'

# Me
curl -i http://localhost:8000/auth/me

# Logout
curl -i -X POST http://localhost:8000/auth/logout
```

## Alembic
- Configured via `alembic.ini` and `alembic/` directory
- First migration creates `users` table

```bash
alembic revision --autogenerate -m "create users"
alembic upgrade head
```

## Notes
- Do not call `Base.metadata.create_all()`; use migrations only.
- JWT is stored as an HTTP-only cookie named `access_token` with value `Bearer <jwt>`.
- CORS allows `http://localhost:3000` with credentials.




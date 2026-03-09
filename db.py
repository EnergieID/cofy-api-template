"""
Database scaffold for Cofy API.

Wraps CofyDB which provides:
  - Alembic migrations (each module owns its own migration branch)
  - Seeding helpers
  - CLI commands: migrate, reset, seed, generate

Requirements:
  pip install "cofy-api[db]"   (or add the [db] extra in pyproject.toml)

Usage:
  poe db migrate   - run pending migrations
  poe db reset     - drop & recreate all tables
  poe db seed      - run the seed function below
  poe db generate  - auto-generate a new migration

See https://github.com/EnergieID/cofy-api for full documentation.
"""

from os import environ

from cofy.db import CofyDB

from main import cofy

# ---------------------------------------------------------------------------
# Initialise the database
# ---------------------------------------------------------------------------
# Swap the URL for your own database (Postgres, MySQL, SQLite, …).
# Reads DATABASE_URL from .env so you can keep credentials out of code.
db = CofyDB(url=environ.get("DATABASE_URL", "sqlite:///./app.db"))

# Bind the database to the Cofy app so modules that use the database can be discovered by the migration tool.
db.bind_api(cofy)


# ---------------------------------------------------------------------------
# Seed data (optional)
# ---------------------------------------------------------------------------
# Define a function that inserts initial / demo data and register it here.
# It will run when you call `poe db seed`.
#
# async def seed():
#     ...
#
# db.set_seed(seed)


# ---------------------------------------------------------------------------
# CLI entrypoint
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    db.cli()

# cofy-api-template

Template repository for spinning up a new [cofy-api](https://github.com/EnergieID/cofy-api) instance — the open-source modular framework by [EnergyID](https://www.energieid.be/) for ingesting, standardising, and serving energy-related data.

> **Use this template:** click _"Use this template"_ on GitHub (or clone and
> rename) to start a fresh project. Then follow the steps below.

---

## Quick start

### Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) (fast Python package manager)

### 1. Install dependencies

```bash
uv sync
```

### 2. Configure environment

```bash
cp .env.example .env
# Edit .env and fill in your values
```

### 3. Enable your modules

Open `main.py` and uncomment / add the modules you need (tariff, production, …).
Each module is a self-contained block with inline documentation.

### 4. Run the dev server

```bash
poe dev          # starts FastAPI with auto-reload, reads .env
```

The API is now available at `http://localhost:8000`.
Health-check: `GET /health`

---

## Configuration

All configuration is done via environment variables. See `.env.example` for the
full list with descriptions.

| Variable | Used by | Description |
|----------|---------|-------------|
| `ENERGY_ID_COFY_API_TOKEN` | `main.py` | Bearer token for API authentication |
| `ENTSOE_API_KEY` | tariff module | ENTSO-E Transparency Platform API key |
| `ENERGY_ID_PRODUCTION_API_KEY` | production module | EnergyID production data API key |
| `ENERGY_ID_PRODUCTION_RECORD_ID` | production module | EnergyID record ID |
| `DATABASE_URL` | `db.py` | SQLAlchemy database URL (default: `sqlite:///./app.db`) |
| `REDIS_URL` | `worker.py` | Redis connection URL (default: `redis://localhost:6379`) |

---

## Development

### Code quality (pre-commit)

Pre-commit hooks are configured out of the box. Install them once:

```bash
pre-commit install
```

Every commit will automatically run:

| Tool | Task | Command |
|------|------|---------|
| **Ruff** | Linting + auto-fix | `poe lint` |
| **Ruff** | Formatting | `poe format` |
| **ty** | Type checking | `poe check` |

You can also run them manually at any time:

```bash
poe lint      # ruff check --fix
poe format    # ruff format
poe check     # ty check
```

---

## Database

The optional `db.py` scaffold wraps `CofyDB` — Alembic migrations, seeding,
and a handy CLI. To use it:

1. Make sure the `[db]` extra is installed (`cofy-api[db]` in `pyproject.toml` — already included).
2. Set `DATABASE_URL` in your `.env` (defaults to a local SQLite file).
3. Use the CLI (reads `.env` automatically):

```bash
poe db migrate    # run pending migrations
poe db reset      # drop & recreate all tables
poe db seed       # run the seed function (if defined)
poe db generate   # auto-generate a new migration
```

Each Cofy module that needs persistence owns its own Alembic migration branch.
See `db.py` for inline documentation and the
[cofy-api README](https://github.com/EnergieID/cofy-api) for full details.

---

## Worker

The optional `worker.py` scaffold wraps `CofyWorker` — a Redis + SAQ async job
queue with cron scheduling. To use it:

1. Make sure the `[worker]` extra is installed (`cofy-api[worker]` in `pyproject.toml` — already included).
2. Have a Redis instance running (or set `REDIS_URL` in `.env`).
3. Start the worker:

```bash
poe worker
```

Define scheduled jobs and lifecycle hooks directly in `worker.py`.
See the inline comments and the
[cofy-api README](https://github.com/EnergieID/cofy-api) for full details.

---

## Docker

```bash
docker build -t cofy-api .
docker run -p 8080:8080 --env-file .env cofy-api
```

The container listens on the port specified by the `PORT` environment variable
(defaults to `8080`).

---

## Project structure

```
main.py                  # App entrypoint – register your modules here
db.py                    # Database scaffold (optional)
worker.py                # Background worker scaffold (optional)
pyproject.toml           # Dependencies & tool config (ruff, ty, poe)
Dockerfile               # Multi-stage production build
.env.example             # Template environment variables
.pre-commit-config.yaml  # Pre-commit hooks (lint, format, type-check)
.github/
  workflows/
    pre-commit.yml       # CI: runs pre-commit on every push / PR
  dependabot.yml         # Dependabot for uv & GitHub Actions
```

---

## License

[MIT](LICENSE)

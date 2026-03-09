"""
Background worker scaffold for Cofy API.

Wraps CofyWorker which provides:
  - SAQ task queue (Redis and Postgres supported)
  - Cron-style scheduling
  - Startup / shutdown lifecycle hooks

Requirements:
  pip install "cofy-api[worker]"   (or add the [worker] extra in pyproject.toml)

Run the worker:
  poe worker

See https://github.com/EnergieID/cofy-api for full documentation.
"""

from os import environ

from cofy.worker import CofyWorker

# ---------------------------------------------------------------------------
# Initialise the worker
# ---------------------------------------------------------------------------
# Reads JOB_STORAGE_URL from .env so you can keep credentials out of code.
worker = CofyWorker(url=environ.get("JOB_STORAGE_URL", "redis://localhost:6379"))


# ---------------------------------------------------------------------------
# Lifecycle hooks (optional)
# ---------------------------------------------------------------------------
# @worker.on_startup
# async def startup():
#     """Runs once when the worker process starts."""
#     ...
#
# @worker.on_shutdown
# async def shutdown():
#     """Runs once when the worker process stops."""
#     ...


# ---------------------------------------------------------------------------
# Scheduled jobs
# ---------------------------------------------------------------------------
# Register recurring tasks with a cron expression.
#
# async def refresh_prices(ctx):
#     """Example: fetch new prices every hour."""
#     ...
#
# worker.schedule(refresh_prices, cron="0 * * * *")

# ---------------------------------------------------------------------------
# SAQ settings – this is the object `saq` needs to discover
# ---------------------------------------------------------------------------
settings = worker.settings

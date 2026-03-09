# cofy-api-template

Template repository for spinning up a new [cofy-api](https://github.com/EnergieID/cofy-api) instance — the open-source modular framework by [EnergyID](https://www.energieid.be/) for ingesting, standardising, and serving energy-related data.

> **Use this template:** click _"Use this template"_ on GitHub (or clone and
> rename) to start a fresh project. Then follow the steps below.


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

Open `main.py` and add the modules you need (tariff, production, …).
See [cofy-api README](https://github.com/EnergieID/cofy-api) for all available modules & options.

### 4. Run the dev server

```bash
poe dev          # starts FastAPI with auto-reload, reads .env
```

The API is now available at `http://localhost:8000`.
Health-check: `GET /health`

### 5. Add database or worker (optional)
If you need persistence or background jobs, see the `db.py` and `worker.py` scaffolds below for easy setup.
Full documentation on these features is available in the [cofy-api README](https://github.com/EnergieID/cofy-api).

Run them using:

```bash
poe db migrate    # run pending migrations
poe worker       # start the worker
```

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

You can also run them manually at any time.

## Docker

```bash
docker build -t cofy-api .
docker run -p 8080:8080 --env-file .env cofy-api
```

The container listens on the port specified by the `PORT` environment variable
(defaults to `8080`).

## License

[MIT](LICENSE)

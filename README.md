# rawlog

A FastAPI-based REST API for tracking workout sessions, exercises, and progress over time !

## Overview

This project is a personal workout tracking application that allows users to log their training sessions with detailed information.

## Tech Stack

- **Framework**: FastAPI
- **Database**: PostgreSQL 16
- **ORM**: SQLAlchemy
- **Package Manager**: uv
- **Containerization**: Docker & Docker Compose
- **Python**: 3.12


## Getting Started

### Prerequisites

- Docker and Docker Compose
- uv (optional, for local development)

### Installation

1. Clone the repository
2. Create a `.env` file by doing 
```bash
cp .env.example .env
```
Then, adjust the `.env` file with your credentials

3. Build and start the services:
```bash
docker-compose up --build
```

4. Run database migrations:
```bash
docker-compose exec web uv run alembic upgrade head
```

The API will be available at `http://localhost:8000`

## Database Migrations

Migrations are managed with Alembic. The database URL is read from the `DATABASE_URL` environment variable.

### From Docker (recommended)

```bash
# Apply all pending migrations
docker-compose exec web uv run alembic upgrade head

# Rollback the last migration
docker-compose exec web uv run alembic downgrade -1

# Check current migration state
docker-compose exec web uv run alembic current
```

### From your local machine

The `db` hostname only resolves inside Docker, so override the URL with `localhost`:

```bash
DATABASE_URL="postgresql://user:password@localhost:5432/rawlog" uv run alembic upgrade head
```

Or create a `.env.local` file with `DATABASE_URL=postgresql://...@localhost:5432/rawlog` and source it before running Alembic.

### Creating a new migration

After modifying a SQLAlchemy model, generate the migration:

```bash
docker-compose exec web uv run alembic revision --autogenerate -m "describe your change"
```

Always review the generated file in `alembic/versions/` before applying it.

## API Endpoints

### Interactive Documentation

FastAPI provides automatic interactive API documentation:

- Swagger UI: `http://localhost:8000/docs`

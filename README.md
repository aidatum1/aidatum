# AI Datum

AI Datum is a web application for aggregating and presenting recall data to consumers.

## Project Structure

```
aidatum/
├── backend/             # FastAPI backend
│   ├── aidatum/        # Main package
│   │   ├── __init__.py
│   │   ├── main.py     # FastAPI application
│   │   ├── api.py      # API routes
│   │   ├── models.py   # SQLAlchemy models
│   │   ├── schemas.py  # Pydantic schemas
│   │   ├── crud.py     # Database operations
│   │   ├── config.py   # Configuration
│   │   └── database.py # Database setup
│   ├── tests/          # Test directory
│   ├── pyproject.toml  # Poetry dependencies
│   └── requirements.txt # pip dependencies
└── frontend/           # React frontend (coming soon)
```

## Features

- RESTful API for recall data
- PostgreSQL database with SQLAlchemy ORM
- FastAPI with automatic OpenAPI documentation
- Data validation with Pydantic
- CORS support for frontend integration
- Filtering and pagination for recall data
- Modern Python practices with type hints and docstrings
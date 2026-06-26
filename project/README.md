# BiteTrack Backend v2

A production-ready, high-performance REST API built with FastAPI and PostgreSQL, serving as the modernized, rebooted backend for the BiteTrack inventory and order system.

## Features
- **User Authentication & RBAC:** Secure user registration, password hashing (bcrypt), token-based login (OAuth2 + JWT), refresh token rotation via HttpOnly cookies, and strict Role-Based Access Control (Admin, Staff, Customer).
- **Relational Inventory Schema:** Modular schemas handling Categories, Products, and Orders with ACID transactional safety during stock decrements.
- **Search, Filtering, and Pagination:** Limit-offset list query parameters, category filtering, and text-based SKU/name search.
- **Robust Integration Testing:** Over 80% test coverage using pytest with a containerized test database.
- **Deployment-Ready:** Multi-stage production Docker image configuration and automated CI actions via GitHub Actions.

## Tech Stack
- **Language:** Python
- **Framework:** FastAPI
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy (Async)
- **Migrations:** Alembic
- **Testing:** pytest
- **Containerization:** Docker & Docker Compose
- **Linting & Formatting:** Ruff

## Getting Started

### Prerequisites
- Docker & Docker Compose
- Python 3.12+ (if running locally without Docker)
- `uv` (Fast Python package installer and resolver)

### Installation
1. Clone the repository.
2. Spin up the application stack:
   ```bash
   docker compose up --build
   ```
3. Access the interactive OpenAPI docs at `http://localhost:8000/docs`.

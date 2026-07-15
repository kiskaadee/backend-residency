# BiteTrack Backend v2

BiteTrack Backend v2 is a REST API designed for small food businesses that manage perishable inventory.

The system centralizes customer management, inventory, sales, outstanding payments, inventory losses, and operational reporting into a unified platform, replacing fragmented spreadsheet-based workflows.

Its goal is to simplify daily operations while preserving historical business data that helps owners make better production and purchasing decisions.

---

## Project Docs Index

[README](./README.md) \[this documment\] → What is BiteTrack?

[SRS](./SRS.md) → Software Requirement Specification: What must BiteTrack do?

[Database](./database.md) → How is the business represented?

[API Design](./api-design.md) → How is the functionality exposed?

[Architecture](architecture.md) → How is the software organized internally?


---

## Core Features

### Authentication & Authorization
- Secure user registration and authentication
- Role-Based Access Control (Administrator, Staff)

### Customer Management
- Customer directory
- Outstanding balance tracking
- Payment history

### Inventory Management
- Product catalog
- Categories
- Stock level management
- Inventory adjustments
- Inventory loss registration

### Sales
- Sales registration
- Payment status
- Customer association
- Automatic inventory updates

### Reporting
- Sales history
- Inventory loss history
- Customer balances
- Product performance
- Operational analytics

---

## Tech Stack

- Python
- FastAPI
- SQLAlchemy (Async)
- PostgreSQL
- Alembic
- pytest
- Docker
- Ruff

---

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Run

```bash
docker compose up --build
```

Interactive documentation:

```
http://localhost:8000/docs
```


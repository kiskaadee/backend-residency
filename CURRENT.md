# Current Focus

## Current Objective
Implement Secure User Registration & CRUD (Milestone 1).

## Current Blocker
None.

## Next Action !!!!
Build one endpoint that accepts a validated request body (`POST /auth/register`).

Tactical actions for next session:
1. Complete the narrow, focused Pydantic guide skeleton in `knowledge/skills/pydantic.md`.
2. Design the `UserRegister` and `UserResponse` Pydantic models.
3. Implement `POST /auth/register` in `bitetrack-api` routes returning a dummy response.
4. Verify route validation and responses.
---

### Step 1 — Read only what you need (30–60 min) -- 

DONE 

Open the official Pydantic documentation and ignore everything except the pieces required to build request models.

Specifically answer these questions in your new guide:

- Why does Pydantic exist?
- What is `BaseModel`?
- How does automatic validation work?
- How does FastAPI use Pydantic? 
- How do I declare fields?
- How do I validate common types (`str`, `int`, `EmailStr`, etc.)?
- How do validation errors look?

---

### Step 2 — Build while reading

After every section, jump to BiteTrack.

For example:

Documentation:

```python
class User(BaseModel):
    username: str
```

Immediately write

```python
class UserRegister(BaseModel):
    ...
```

Even if it's incomplete.

---

### Step 3 — Decide API contract

Before writing routes, answer questions like:

Request

```json
{
    "email": "...",
    "password": "...",
    "full_name": "..."
}
```

Response

```json
{
    "id": "...",
    "email": "...",
    "full_name": "..."
}
```

Notice something?

This is no longer a Pydantic problem: It's API design.

---

### Step 4 — Implement a dummy endpoint

No database. No hashing. No SQLAlchemy.

Just:

```python
@app.post(...)
def register(user: UserRegister):
    ...
```

Return fake data. Your goal is to watch FastAPI validate the request automatically.
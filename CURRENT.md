# Current Focus

## Current Objective
Implement Secure User Registration & CRUD (Milestone 1).

## Current Blocker
None.

## Next Action !!!!
Implement `UserRegister` and `UserResponse` schemas and the registration endpoint with validation.

Tactical actions for today's session:
1. Design `UserRegister` and `UserResponse` Pydantic models in `src/schemas/users.py` (inheriting/extending `UserBase`).
2. Implement `POST /auth/register` in `src/routers/auth.py` to return a dummy response conforming to `UserResponse`.
3. Manually verify the endpoint's automatic type validation and `422 Unprocessable Entity` responses.
4. Draft basic validation tests in the `/tests` folder using `fastapi.testclient.TestClient`.
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
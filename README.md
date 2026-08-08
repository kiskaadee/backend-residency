# Backend Journey: 90-Day Backend Residency

Welcome to your Backend Residency. This repository is configured to organize your learning path, track progress, maintain a backlog for your flagship project, log interviews, and consolidate your personal backend engineering notes.

## Repository Structure

### Strategic Documents
- [todo.md](todo.md) — The main checklist representing the core phases, tasks, and exit criteria. (Symlinked to your home directory at `~/todo.md` for quick access!)
- [ROADMAP.md](ROADMAP.md) — The high-level strategic roadmap with phase details and exit gates.
- [WEEKLY.md](WEEKLY.md) — Index of daily journals and weekly planning.
- [SKILLS.md](SKILLS.md) — Confidence and interview readiness matrix for core backend technologies.
- [AGENTS.md](AGENTS.md) — The AI Coaching Manual and guidelines for the residency.
- [parking-lot.md](knowledge/parking-lot.md) — Backlog of future topics and concepts deferred to prevent scope creep.

### Flagship Project (External)
- [bitetrack-api](https://github.com/kiskaadee/bitetrack-api) — The implementation repository.
- [TODO.md](https://github.com/kiskaadee/bitetrack-api/blob/main/docs/TODO.md) — The operational backlog for the flagship backend project.

### Documentation & Logs (`docs/`)
- [LOG.md](docs/interview/LOG.md) — Conceptual flashcards and logs of mock/real interviews.
- [adr/](docs/adr/) — Architecture Decision Records (ADRs) detailing technology choices.
- [mistakes/template.md](docs/mistakes/template.md) — Template for logging mistakes and debugging lessons.

### Knowledge Base (`knowledge/`)
- **Skills Guides (`knowledge/skills/`)**:
  - [sql.md](knowledge/skills/sql.md) — SQL, indexes, transactions, normalization, joins.
  - [auth.md](knowledge/skills/auth.md) — JWTs, hashing, authorization, and authentication flows.
  - [testing.md](knowledge/skills/testing.md) — Unit testing, integration testing, and pytest.
  - [adrs.md](knowledge/skills/adrs.md) — Quick guide on writing Architecture Decision Records.
  - [notes-to-docs.md](knowledge/skills/notes-to-docs.md) — Reformatting raw study notes into clean documentation.
- **Python notes (`knowledge/python/`)**:
  - [pydantic.md](knowledge/python/pydantic.md) — Request validation and serialization guide.
  - [enumerate.md](knowledge/python/enumerate.md) — Enumeration loops in Python.
  - [zip.md](knowledge/python/zip.md) — Iteration and transposition using `zip()`.
- **Tools Reference (`knowledge/tools/`)**:
  - [docker.md](knowledge/tools/docker.md) — Containerization basics and multi-stage builds.
  - [tmux.md](knowledge/tools/tmux.md) — Tmux cheat sheet and session/pane management.
- **DSA Notes (`knowledge/dsa/`)**:
  - [linked-list.md](knowledge/dsa/linked-list.md) — Linked list mechanics and pointers.
  - [binary-search.md](knowledge/dsa/binary-search.md) — Binary search templates.
  - [hashmap.md](knowledge/dsa/hashmap.md) — Hash table designs and collision resolution.

### Code Practice & Logs (`practice/`)
- [00-practiced-patterns.md](practice/LeetCode/00-practiced-patterns.md) — LeetCode exercises solved in Python, indexed by pattern.

---

## Guidelines for Documentation
- Use standard relative markdown links (e.g. `[ROADMAP.md](ROADMAP.md)` or `[sql.md](knowledge/skills/sql.md)`) to connect your study materials, daily logs, and project tasks. Avoid the Obsidian custom `[[document]]` syntax.
- Keep updates concise and version-controlled. Commit your changes using Conventional Commits formats.


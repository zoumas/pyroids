# Copilot Instructions for Pyroids

## Project Overview

Pyroids is an Asteroids clone built by following the
[Build Asteroids using Python and Pygame](https://www.boot.dev/courses/build-asteroids-python)
course on boot.dev. The course covers:

1. **Pygame** — Setup and installation
2. **Game Loop** — Rendering at 60 FPS
3. **Player** — Player class with movement
4. **Asteroids** — Asteroid spawning and avoidance

## Build & Run

- **Package manager:** [uv](https://docs.astral.sh/uv/)
- **Python:** 3.13 (pinned in `.python-version`)
- **Install deps:** `uv sync`
- **Run:** `uv run python main.py`

## Conventions

- Use `uv` for all dependency and environment management — not pip or venv directly.
- Entry point is `main.py` with a `main()` function guarded by `if __name__ == "__main__"`.
- The project uses OOP: game entities (player, asteroids) are classes.

## How to Help

- Reference the boot.dev course lessons when explaining concepts.
- Review code for correctness and suggest improvements beyond the course material.
- Help the user understand *what* is being built and *why*, not just *how*.

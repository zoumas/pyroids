# Pyroids

Pyroids is a small Asteroids-style arcade game built with **Python 3.13** and **Pygame** while following the [Build Asteroids using Python and Pygame](https://www.boot.dev/courses/build-asteroids-python) course on [boot.dev](https://www.boot.dev).

This project takes us from a blank window to a playable game loop with a controllable ship, asteroid spawning, shooting, collisions, asteroid splitting, and simple runtime logging.

## What we built

- A real-time game loop running at 60 FPS
- A player ship that can rotate, move forward and backward, and fire shots
- Asteroids that spawn from the screen edges and move across the play area
- Collision detection between the player, asteroids, and shots
- Asteroid splitting logic for larger rocks
- Game-over handling when the player is hit
- JSONL logging for sampled game state and gameplay events

## What we learned

### 1. How a game loop works

The project introduced the core loop of a game:

1. Read input
2. Update game objects
3. Detect collisions
4. Draw the next frame
5. Repeat

That loop is the foundation of the whole game.

### 2. How to use delta time for smooth movement

Movement is scaled by `dt`, the elapsed time since the previous frame. That keeps motion more consistent across different machines and frame rates.

### 3. How to model a game with classes

The code uses object-oriented design for game entities:

- `CircleShape` provides shared position, velocity, radius, and collision behavior
- `Player`, `Asteroid`, and `Shot` each add their own drawing and update logic
- `AsteroidField` manages spawning rather than drawing a single object

This keeps shared behavior centralized and makes each class easier to reason about.

### 4. How vector math simplifies movement and rotation

Pygame vectors are used to:

- Rotate the ship
- Move the player in the direction it is facing
- Launch shots forward
- Give asteroids directional velocity

That makes movement code much cleaner than manually managing x/y math everywhere.

### 5. How sprite groups help organize game objects

The game uses separate groups for:

- objects that update
- objects that draw
- asteroids
- shots

This makes the main loop simple and keeps responsibilities clear.

### 6. How collisions drive gameplay

The gameplay comes from a few simple collision rules:

- asteroid + player -> game over
- asteroid + shot -> destroy shot and split asteroid

Even a small set of rules can create a complete arcade loop.

### 7. How lightweight logging helps debugging

The project also logs:

- sampled runtime state to `game_state.jsonl`
- gameplay events to `game_events.jsonl`

This is useful for inspecting what happened during a run without building a full debugging UI.

## Controls

| Action | Keys |
| --- | --- |
| Rotate left | `A` or `Left Arrow` |
| Rotate right | `D` or `Right Arrow` |
| Move forward | `W` or `Up Arrow` |
| Move backward | `S` or `Down Arrow` |
| Shoot | `Space` |

## Project structure

| File | Purpose |
| --- | --- |
| `main.py` | Sets up Pygame, sprite groups, the game loop, collisions, and rendering |
| `constants.py` | Central game tuning values such as screen size, speeds, and radii |
| `circleshape.py` | Shared base class for circular game objects |
| `player.py` | Player movement, rotation, drawing, and shooting |
| `asteroid.py` | Asteroid movement, drawing, and splitting |
| `asteroidfield.py` | Timed asteroid spawning from screen edges |
| `shot.py` | Projectile behavior |
| `logger.py` | JSONL state and event logging helpers |

## Requirements

- [uv](https://docs.astral.sh/uv/)
- Python 3.13

## Getting started

```sh
uv sync
uv run python main.py
```

## Final takeaway

Pyroids is a small project, but it covers many of the fundamentals behind 2D game development: loops, timing, input, movement, collision detection, object modeling, and incremental gameplay rules. It is a solid end-to-end example of how a simple game comes together from a handful of focused systems.

# Flooder Game

A terminal-based flood fill puzzle game built in Python using recursive graph traversal and ANSI terminal rendering.

The goal of the game is to flood the entire board with a single colour before running out of moves.

This project began as a simple nested data structure exercise and gradually evolved into a fully playable terminal game featuring dynamic difficulty, procedural board generation, recursive flood fill logic, and configurable gameplay systems.

---

# Features

- Dynamic board sizes
- Multiple difficulty presets
- Configurable colour smearing intensity
- Recursive flood fill algorithm
- Dynamic move system
- ANSI terminal rendering
- Randomized colour pools
- Type hinted codebase
- Terminal UI using Unicode box drawing characters
- Win/loss detection
- Clean modular architecture

---

# Technologies Used

- Python 3
- `bext` for terminal colours
- ANSI escape sequences for terminal control

---

# Gameplay

The player starts at the top-left tile of the board.

Each move:

1. Selects a colour
2. Flood-fills all connected neighbouring tiles of the same colour
3. Expands the controlled area

The objective is to make the entire board a single colour before running out of moves.

Difficulty affects:

- Board size
- Number of colours
- Smearing intensity
- Moves available

---

# Concepts Practiced

This project heavily focuses on:

- Recursive algorithms
- Flood fill / graph traversal
- Recursive DFS concepts
- Grid-based neighbour traversal
- Direction vector systems
- Boundary checking
- Dictionary-based board storage
- Dynamic configuration systems
- Runtime-generated game state
- Type hints and aliases
- Modular function design
- Terminal rendering

---

# Project Structure

```text
Flooder-Game/
│
├── .python-version
├── ascii_art.py
├── main.py
├── pyproject.toml
├── README.md
└── uv.lock
```

---

# How It Works

The board is internally represented as a dictionary:

```python
board[(x, y)] = "red"
```

Flood fill works recursively by:

1. Checking neighbouring tiles
2. Verifying valid boundaries
3. Replacing connected matching colours
4. Recursively expanding outward

Neighbour traversal uses direction vectors:

```python
DIRECTIONS = (
    (-1, 0),
    (0, 1),
    (0, -1),
    (1, 0),
)
```

---

# Example Difficulties

| Difficulty | Board Size | Colours | Intensity | Moves |
| ---------- | ---------- | ------- | --------- | ----- |
| Easy       | 10x8       | 4       | 4         | 22    |
| Medium     | 14x12      | 5       | 2         | 20    |
| Hard       | 18x15      | 6       | 1         | 17    |

---

# Running the Project

This project uses uv for dependency management.

Install dependencies:

```bash
uv sync
```

Run the game:

```basn
uv run main.py
```

## Requirements

- Python 3.11+
- uv

Install `uv`:

```bash
pip install uv
```

---

# Future Improvements

Planned improvements include:

- Animated flood fill
- Better board balancing
- Custom difficulty creation
- Iterative flood fill implementation
- Score system
- Save/load system
- Mouse support
- Time attack mode
- Smarter move calculation
- Better terminal responsiveness

---

# What I Learned

This project helped reinforce concepts such as:

- Recursive problem solving
- Graph traversal thinking
- State management
- Game architecture
- Dynamic configuration systems
- Clean function design
- Grid algorithms
- Boundary-safe traversal

It also demonstrated how small practice projects can gradually evolve into larger structured applications through iterative refactoring and feature expansion.

# Development Notes

This project also marked my first time using uv for Python dependency and environment management.
The project uses:

- `pyproject.toml`
- `uv.lock`
- `.python-version`

to maintain a reproducible development environment and modern Python workflow.
During development, the project gradually evolved from a small recursion exercise into a more structured terminal game featuring:

- recursive flood fill
- dynamic game configuration
- runtime-generated state
- modular game architecture
- type aliases and type hints

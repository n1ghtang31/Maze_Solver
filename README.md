# Maze_Solver

A Python program that generates a random maze and then solves it, animating both steps in a window.

## How it works

- **Generation:** starts from a grid of walled cells and knocks walls down with a randomized depth-first search (recursive backtracking), so every cell is reachable and there is exactly one path between any two cells.
- **Solving:** a depth-first search from the top-left entrance to the bottom-right exit. Moves toward the exit are drawn in red, and dead ends are redrawn in gray as the solver backs out of them.
- **Drawing:** a small graphics layer on top of Tkinter's `Canvas` (`Window`, `Point`, `Line` and `Cell` classes in `graphics.py`).

## Running it

Requires Python 3 with Tkinter (on Debian or Ubuntu: `sudo apt install python3-tk`).

```bash
python3 main.py
```

The maze size is set at the top of `main()` in `main.py`.

## Tests

```bash
python3 tests.py
```

Tests cover grid creation, the entrance and exit, and resetting cells between generation and solving.

## Background

Built as a guided project on [Boot.dev](https://www.boot.dev).

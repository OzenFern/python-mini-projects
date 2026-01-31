# Hangman Game

A terminal-based **Hangman game** written in Python. This project focuses on clean function design, modular code structure, and basic game logic.

## About

The game randomly selects a word and lets the player guess letters one at a time. Incorrect guesses reduce lives, visually represented using ASCII hangman stages. Hints are available but subject to rules: hints unlock after your first wrong guess, are disabled when only one life or only one unknown letter remains, and have a per-difficulty cap. Use `!` during play to reveal a single letter when allowed.

## Features

- ASCII art hangman visuals and a game logo.
- Difficulty selection with different hint caps and hint percentages:
  - Easy: cap 3, hint percentage 40%
  - Normal (default): cap 2, hint percentage 30%
  - Hard: cap 1, hint percentage 20%
- Hints unlock after the first wrong guess and consume one hint each time.
- Words include 5- to 8-letter options to vary difficulty and replayability.

## Files Overview

- `main.py`  - Entry point of the program; controls the game loop and player interaction.
- `hangman.py` - Core game logic, input handling, and display functions (difficulty, hints, lives, and game state).
- `words.py` - Word lists (5- to 8-letter words) used to pick the secret word.
- `ascii_art.py` - Game logo and hangman stage visuals.

## Requirements

- Python 3.x (no external libraries required)

## Notes

- Input is case-insensitive and only the first character of input is considered.
- Type `!` during a turn to attempt using a hint (reveals one letter) when allowed.
- Already guessed letters do not reduce lives and attempting them will notify the player.
- The game ends when the secret word is fully revealed or when lives reach zero. After a game ends, you can choose to play again or quit.


(Sections "License" and "How to Run" have been removed to match the latest project changes.)
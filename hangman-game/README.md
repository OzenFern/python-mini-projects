# Hangman Game

A terminal-based **Hangman game** written in Python.  
This project focuses on clean function design, modular code structure, and basic game logic.

## About

The game randomly selects a word and lets the player guess letters one at a time.  
Incorrect guesses reduce lives, visually represented using ASCII hangman stages.

The code is split into multiple files to keep responsibilities clear:
- Game logic
- Word data
- ASCII visuals
- Program entry point


## How It Works

- A random word is chosen from a predefined list.
- The player guesses one letter at a time.
- Correct guesses reveal letters in the word.
- Incorrect guesses affect lives.
- Already guessed letters do not reduce lives.
- The game ends when the word is guessed or lives reach zero.
- The player can choose to play again or quit.

## Files Overview

- `main.py`  
  Entry point of the program. Controls the game loop and player interaction.

- `hangman.py`  
  Contains the core game logic, input handling, and display functions.

- `words.py`  
  Stores the list of possible words.

- `ascii_art.py`  
  Contains the game logo and hangman stage visuals.

## Requirements

- Python (no external libraries required).


## Notes

- Input is case-insensitive.
- Input is designed such that only the first letter is accepted.
- Only alphabetic characters are accepted as guesses.
- ASCII art is used for visual feedback in the terminal.

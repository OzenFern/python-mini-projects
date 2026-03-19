# Two Player Quiz Game (Python)

A terminal-based **2-player quiz game** written in Python.  
Players take turns answering questions, earn points, and compete for the highest score.

---

## About

This program runs a quiz between two players using a predefined set of questions.  
Each player gets turns to answer, with limited attempts per question.

Scores are tracked and displayed after every round, and the winner is declared at the end.

---

## How It Works

- Two players enter their names
- A player is randomly selected to start
- Each player gets:
  - 2 attempts per question
  - Option to skip a question
- Correct answers increase the player's score
- Scores are displayed after each round
- Final winner (or draw) is declared at the end
- Option to reveal all answers after the game

---

## Features

- Turn-based 2-player system
- Scoreboard displayed after every question
- Input validation and retry attempts
- Skip option for questions
- Random starting player
- Clean terminal UI with ASCII logo

---

## Files Overview

- `main.py`  
  Handles game flow, player turns, scoring, and display.

- `quiz.py`  
  Stores all quiz questions and answers.

- `ascii_art.py`  
  Contains the game logo.

---

## Requirements

- Python  
- No external libraries required
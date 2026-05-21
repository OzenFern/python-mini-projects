# Powerball Simulator

A terminal-based Powerball simulator built with Python.

This project allows players to:

- choose their own Powerball numbers
- simulate multiple lottery draws
- track winnings and losses
- manage a virtual bankroll
- replay rounds until funds run out

The project started as simple input validation practice and gradually evolved into a small state-driven CLI application focused on:

- input validation
- reusable helper functions
- state management
- formatted terminal output
- lottery simulation logic
- clean procedural architecture

---

## Features

- Choose 5 unique white balls (`1–69`)
- Choose a Powerball number (`1–26`)
- Dynamic balance system
- Multiple attempts per round
- Tracks:
  - total winnings
  - total losses
  - remaining balance
  - total attempts played

- Strong input validation
- Clean formatted terminal UI
- Replay system until funds run out

---

## Example Gameplay

```text
Welcome Player!
  How much money would you like to start with?
> 100

  Balance of $100 added!

Enter 5 different numbers from 1 to 69
> 5 12 23 44 69

Enter Powerball number from 1 to 26
> 7

How many times do you want to play? (Max: 50)
> 5

The winning numbers are: 4, 12, 23, 50, 69  Powerball: 7     Prize: $100
The winning numbers are: 1, 9, 20, 33, 45   Powerball: 10    Prize: No win
...
```

---

## Prize Table

| White Ball Matches | Powerball Match | Prize      |
| ------------------ | --------------- | ---------- |
| 5                  | Yes             | Jackpot    |
| 5                  | No              | $1,000,000 |
| 4                  | Yes             | $50,000    |
| 4                  | No              | $100       |
| 3                  | Yes             | $100       |
| 3                  | No              | $7         |
| 2                  | Yes             | $7         |
| 1                  | Yes             | $4         |
| 0                  | Yes             | $4         |

---

## Concepts Practiced

This project heavily focuses on:

- functions
- modular program design
- reusable validation logic
- lists and sets
- set intersection
- dictionary lookups
- random number generation
- formatted string output
- derived state calculation
- game loop architecture
- terminal UX design

---

## Project Structure

```text
powerball-simulator/
│
├── main.py
├── ascii_art.py
└── README.md
```

---

## Requirements

- Python 3.10+

No external libraries required.

---

## What I Learned

Some important concepts explored while building this project:

- Why derived values should not be permanently stored
- Difference between parsing and validation
- Using sets for efficient comparisons
- Avoiding hidden state synchronization bugs
- Designing reusable input systems
- Building cleaner CLI interfaces with f-string formatting

---

## Future Improvements

Possible upgrades for the future:

- Auto-generated random tickets
- Statistics dashboard
- Save/load game data
- Leaderboard system
- Colored terminal output
- Smart betting simulations
- Win probability analysis
- GUI version using Tkinter or PyQt

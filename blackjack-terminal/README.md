# Blackjack

A terminal-based Blackjack game built in Python featuring ASCII card rendering, betting, blackjack payouts, dealer AI, and a casino-style multi-deck shoe.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Completed-success)

---

## Features

- Beautiful ASCII playing cards
- Full 52-card deck with all four suits
- Casino-style 6-deck shoe
- Automatic reshuffling at deck penetration threshold
- Betting system with balance tracking
- Blackjack detection
- 3:2 blackjack payout
- Dealer AI (hits below 17, stands on 17+)
- Hidden dealer card
- Double Down support
- Bust detection
- Push (draw) handling
- Clean terminal interface

---

## Preview

```text
Dealer: 10 ??
╔═══════╗ ╔═══════╗
║10     ║ ║▒      ║
║   ♠   ║ ║   ▒   ║
║     10║ ║      ▒║
╚═══════╝ ╚═══════╝

Player: 16
╔═══════╗ ╔═══════╗
║K      ║ ║6      ║
║   ♦   ║ ║   ♠   ║
║      K║ ║      6║
╚═══════╝ ╚═══════╝
```

---

## Rules

### Card Values

| Card    | Value      |
| ------- | ---------- |
| 2-10    | Face Value |
| J, Q, K | 10         |
| A       | 1 or 11    |

### Blackjack

A Blackjack occurs when the first two cards total 21.

Examples:

```text
A + K
A + Q
A + J
A + 10
```

Blackjack pays **3:2**.

### Dealer Rules

The dealer:

- Hits when below 17
- Stands on 17 or above

### Double Down

Players may double their bet on their first turn and receive exactly one additional card.

---

## Project Structure

```text
blackjack/
│
├── blackjack.py
├── ascii_art.py
└── README.md
```

---

## Concepts Practiced

This project focuses on:

- Functions
- Lists and list comprehensions
- Tuples
- Type hints
- Game loops
- State management
- Terminal UI design
- Randomization and shuffling
- Data modelling
- Input validation
- Blackjack game logic

---

## Future Improvements

Possible enhancements:

- Split Hands
- Insurance Bets
- Surrender Option
- Multiple Players
- Statistics Tracking
- Save/Load Balance
- Colorized Terminal Output
- Sound Effects
- Object-Oriented Refactor
- Unit Tests

---

## What I Learned

While building this project I practiced:

- Designing game flow
- Separating UI from game logic
- Managing shared state
- Working with card-based simulations
- Building reusable helper functions
- Improving terminal user experience

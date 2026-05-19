# Music Simulation App

A terminal-based Python music simulation app built to practice:

- Nested Tuples
- Tuple Unpacking
- Dynamic Table Rendering
- Enumerate & Zip
- Input Validation
- Generic Utility Functions

The app allows users to:

- Browse bands and songs
- Select songs using numeric input
- Maintain song play history
- Display formatted history tables dynamically

---

# Features

- Nested tuple data structure for albums and tracks
- Dynamic CLI table rendering
- Automatic column width calculation
- Song play history
- Serial numbering in history
- Input validation
- Reusable table utilities
- Generic width calculation system

---

# Project Structure

```text
music-simulation-app/
│
├── albums.py        # Nested tuple music data
├── ascii_art.py     # App logo/banner
├── main.py          # Main application logic
└── README.md
```

---

# Example Data Structure

```python
tracks = [
    (
        "Green Day",
        [
            "Somewhere Now",
            "Bang Bang",
            "Revolution Radio",
            "Say Goodbye",
            "Outlaws",
        ],
    ),
]
```

This project heavily focuses on working with:

- nested data structures
- tuples and lists
- nested indexing
- nested iteration
- tuple unpacking
- dynamic table rendering
- reusable utility functions

## Design Evolution

This project originally started as a nested tuple practice app.
During development, the music library structure was redesigned to use mutable nested lists for songs, making the application behave more like a realistic music management system where tracks can be added or removed dynamically.

---

# Concepts Practiced

## 1. Nested Tuples

Used to organize:

- bands
- albums
- songs

Example:

```python
band_name = tracks[0][0]
song_name = tracks[0][1][2]
```

---

## 2. Nested Tuple Unpacking

Example:

```python
for num, (band, song) in enumerate(song_history, start=1):
```

This combines:

- enumerate()
- tuple unpacking
- nested unpacking

---

## 3. Dynamic Table Rendering

The table system automatically:

- calculates column widths
- formats rows dynamically
- supports any number of columns

Example output:

```text
-----------------------------------------------
| Sr No. | Band       | Song                 |
-----------------------------------------------
| 1      | Green Day  | Bang Bang            |
| 2      | Metallica  | Battery              |
-----------------------------------------------
```

---

# Python Concepts Used

- Nested Tuples
- Tuple Unpacking
- `enumerate()`
- `zip()`
- Generator Expressions
- List Comprehensions
- Dynamic Formatting
- F-Strings
- Input Validation
- Exception Handling

---

# Lessons Learned

During development, several important Python concepts were explored:

- Difference between generators and lists
- Proper use of `append()`
- Dynamic formatting with nested f-string braces
- Using `zip(*rows)` for column extraction
- Building reusable utility functions
- Separating display logic from application state

---

# Future Improvements

Potential upgrades:

- Album support
- Search functionality
- Song duration tracking
- Pagination
- ANSI color styling
- Save history to file
- OOP refactor
- Full terminal UI using `rich` or `textual`

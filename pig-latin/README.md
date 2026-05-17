# English to Pig Latin Converter

A simple Python project that converts English text into Pig Latin while preserving capitalization and surrounding punctuation.

This project was built to practice:
- Functions
- Tuples
- String manipulation
- Loops
- List handling
- Program decomposition
- Data transformation pipelines

---

# Features

- Converts English words into Pig Latin
- Preserves leading and trailing punctuation
- Preserves capitalization of the first letter
- Leaves numbers and non-alphabetic tokens untouched
- Uses tuples to structurally separate words into:
  - prefix
  - core text
  - suffix

---

# Rules

## Consonant Rule

If a word begins with a consonant:
- Move the first letter to the end
- Add `ay`

Example:

```text
cat -> atcay
Python -> Ythonpay
```

---

## Vowel Rule

If a word begins with a vowel:
- Add `yay` to the end

Example:

```text
eat -> eatyay
I -> Iyay
```

---

## Number Rule

Numbers are not modified.

Example:

```text
542 -> 542
```

---

## Punctuation Handling

Leading and trailing punctuation is preserved.

Example:

```text
"Hello!" -> "Ellohay!"
```

Internal punctuation such as apostrophes or hyphens is intentionally ignored in this implementation.

---

# Example

## Input

```text
I love Python!
```

## Output

```text
Iyay ovelay Ythonpay!
```

---

# Project Structure

```text
get_input()       -> Handles user input
split_msg()       -> Splits message into words
word_separator()  -> Separates prefix/core/suffix
check_letter()    -> Checks vowel and capitalization
transform_text()  -> Converts word into Pig Latin
rebuild_msg()     -> Rebuilds final sentence
```

---

# How It Works

Each word is processed in multiple stages:

```text
Input
↓
Split Message
↓
Separate Punctuation
↓
Transform Core Word
↓
Rebuild Sentence
↓
Output
```

The program uses tuples to store structured word data:

```python
(prefix, core, suffix)
```

Example:

```python
('"', 'Hello', '!')
```

---

# Requirements

- Python 3.x

No external libraries are required.

---

# Future Improvements

Possible future additions:
- Preserve exact spacing
- Support contractions like:
  - don't
  - I'm
- Handle hyphenated words
- Reverse Pig Latin conversion
- File input/output support
- GUI or web version

---

# Learning Goals

This project was mainly created to practice:
- Tuple unpacking
- Immutable data handling
- Function design
- String slicing
- Program organization
- Clean data flow
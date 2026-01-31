import os
import random
import math
import words
from ascii_art import logo, hangman_stages


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def display_rules():
    print(
        """Welcome!
Try to guess the word before the hangman is completed to win. 
You can use hints to reveal a letter of the word, but hints are only unlocked after you lose a life.
Additionally, you also cannot use hint if you have only one life left and/or one letter to guess...

Good Luck!
"""
    )


def display_logo():
    print(logo)


def initialize_secret_word():
    return random.choice(words.word_list).upper()


def create_blanks_list(p_word):
    blanks = "_" * len(p_word)
    return list(blanks)


def display_blanks(p_blanks):
    print(" ".join(p_blanks), "\n")


def start_game():
    clear_screen()
    display_logo()
    display_rules()


def get_guess():
    while True:
        guess = input("Guess a letter: ").strip()
        if not guess:
            continue
        elif guess == "!":
            return guess
        elif guess.isalpha():
            return guess.upper()[:1]
        else:
            print("Please enter an alphabet")


def update_blanks(p_guess, p_blank_list, p_word):
    for i in range(len(p_word)):
        if p_word[i] == p_guess:
            p_blank_list[i] = p_guess


def initialise_lives():
    return len(hangman_stages) - 1


def display_hangman_stage(p_lives):
    index = max(0, p_lives)
    print(hangman_stages[index])


def get_difficulty():
    """
    Easy -> cap: 3, percentage: 0.4 \n
    Normal -> cap: 2, percentage: 0.3 \n
    Hard -> cap: 1, percentage: 0.2
    """
    choices_list = ["E", "N", "H", ""]
    while True:
        choice = input(
            "Select game difficulty...\n" "(E: Easy, N: Normal (Default), H: Hard): "
        )
        choice = choice.upper().strip()
        if choice in choices_list:
            if choice == "E":
                return "Easy", 3, 0.4
            elif choice == "H":
                return "Hard", 1, 0.2
            else:
                return "Normal", 2, 0.3
        else:
            print("Please type E, N or H (or press Enter for Default Mode)...")


def max_hints(p_word, p_cap, p_percentage):
    return min(max(1, math.floor(p_percentage * len(p_word))), p_cap)


def can_use_hints(p_blank_list, p_hints_left, p_lives, p_initial_lives, p_mode):
    """
    A single source of truth for checking whether, hints can be used.
    """
    if p_lives == p_initial_lives:
        return False, "\tHints unlock after your first wrong guess..."
    elif p_lives == 1:
        return False, "\tHints are disabled (only one life remaining)..."
    elif p_hints_left == 0:
        return False, f"\tNo hints left for {p_mode} difficulty..."
    elif p_blank_list.count("_") == 1:
        return False, "\tHints are disabled (only one letter left to guess)..."
    else:
        return True, ""


def hidden_unique_letters(p_word, p_blank_list):
    unguessed_letters = []
    for i in range(len(p_word)):
        if p_blank_list[i] == "_" and p_word[i] not in unguessed_letters:
            unguessed_letters.append(p_word[i])
    return unguessed_letters


def apply_hint(p_word, p_blank_list, p_hint_left):
    hidden_letters = hidden_unique_letters(p_word, p_blank_list)
    if not hidden_letters:
        return p_hint_left
    letter = random.choice(hidden_letters)
    for i in range(len(p_word)):
        if p_word[i] == letter:
            p_blank_list[i] = letter
    return max(0, p_hint_left - 1)


def decide_result(p_blanks_list, p_lives):
    if "_" not in p_blanks_list:
        return "You Win!"
    if p_lives == 0:
        return "You Lose."
    return ""


def display_game_status(
    p_lives, p_initial_lives, p_blanks, p_hints_left, p_hints_total, p_mode
):
    clear_screen()
    display_hangman_stage(p_lives)
    display_blanks(p_blanks)

    print(f"Difficulty: {p_mode}\n")
    can_hint, reason = can_use_hints(
        p_blanks, p_hints_left, p_lives, p_initial_lives, p_mode
    )
    if can_hint:
        print(
            f"Hints remaining: {p_hints_left} / {p_hints_total} for {p_mode} difficulty\n"
            "\tType '!' to use a hint (reveals one letter)\n"
        )
    else:
        print(f"{reason}\n")


def play_again():
    choice = input("\nPress 'q' to exit, or press any key to play again: ").lower()
    return False if choice == "q" else True

import os
import random
import words
from ascii_art import logo, hangman_stages

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_logo():
    print(logo)

def initialize_secret_word():
    return random.choice(words.word_list).upper()

def create_blanks_list(p_word):
    blanks = "_" * len(p_word)
    return list(blanks)
    
def display_blanks(p_blanks):
    print(" ".join(p_blanks),"\n")

def start_game():
    clear_screen()
    display_logo()

def get_guess():
    while True:
        guess = input("Guess a letter: ")
        if guess.isalpha():
            return guess.upper()[:1]
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

def display_all(p_lives, p_blanks):
    display_hangman_stage(p_lives)
    display_blanks(p_blanks)

def decide_result(p_blanks_list, p_lives):
    if '_' not in p_blanks_list:
        return "You Win!"
    if p_lives == 0:
        return "You Lose."
    return ""

def play_again():
    choice = input("\nPress 'q' to exit, or press any key to play again: ").lower()
    return False if choice == 'q' else True
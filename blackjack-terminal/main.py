import random
from ascii_art import logo

# Typing Hints
StrDict = dict[str, str]
Ranks = str | int
State = dict[str, int]

# Constants
UNICODE: StrDict = {
    "spade": chr(9824),
    "club": chr(9827),
    "heart": chr(9829),
    "diamond": chr(9830),
    "double_line": chr(9552),
    "double_pipe": chr(9553),
    "top_left": chr(9556),
    "top_right": chr(9559),
    "bottom_left": chr(9562),
    "bottom_right": chr(9565),
}


CARD_CONFIG: State = {"width": 3, "height": 3}

RANKS: set[Ranks] = {2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"}

# State
balance: int = 5000


# Function Definition
def print_message(message: str) -> None:
    """
    A customized print() to display a message to the terminal
    """
    print(f"\n\t{message}\n")


def get_input(prompt: str) -> str:
    """
    A customized input() which strips away all the whitespaces
    """
    return input(f"{prompt}\n> ").strip()


def convert_to_int(number: str) -> int | None:
    try:
        return int(number)
    except ValueError:
        return None


def num_is_between(num_to_check: int, from_num: int, to_num: int) -> bool:
    """
    Returns True if the number is between the specified range
    """
    return from_num <= num_to_check <= to_num


def get_single_number(message: str, from_num: int, to_num: int) -> int:
    while True:
        number = convert_to_int(get_input(message))
        if number is None:
            print_message("Please enter a single number!")
        elif not num_is_between(number, from_num, to_num):
            print_message(f"Please select a number from {from_num} to {to_num}!")
        else:
            return number


def build_card(rank: Ranks, suit: str) -> str:
    """
    Builds a card ascii art from a provided rank and suit
    """
    raise NotImplementedError(
        "Implement a get_card() to get parameters for this function"
    )


def check_balance() -> bool:
    global balance

    raise NotImplementedError(
        "Add docstrings, When balance is 0, print, you're broke annd exit game"
    )


def exit_game() -> None:
    import sys

    try:
        sys.exit()
    finally:
        print_message("Thanks for playing! Catch you later :D")


def run_app():
    global balance

    print(logo)
    print("Welcome to Blackjack!")
    print_message("You can press 'ctrl + c' anytime to quit...")
    print(f"Money: ${balance:,}")
    bet = get_single_number(
        f"How much do you want to bet? (1 - {balance:,})",
        1,
        balance,
    )
    print(f"Bet: {bet}")


# Driver
try:
    run_app()
except KeyboardInterrupt:
    print_message("You've pressed ctrl + C, exiting...")
    exit_game()

import random
from ascii_art import logo

# Typing Hints
StrDict = dict[str, str]
Rank = str
State = dict[str, int]
CardMap = tuple[str, str, str, str, str]
Card = tuple[Rank, str]
Deck = set[Card]
Dealer = list[Card | None]

# Constants
SUITS: StrDict = {
    "spade": chr(9824),
    "club": chr(9827),
    "heart": chr(9829),
    "diamond": chr(9830),
}

BOX: StrDict = {
    "double_line": chr(9552),
    "double_pipe": chr(9553),
    "top_left": chr(9556),
    "top_right": chr(9559),
    "bottom_left": chr(9562),
    "bottom_right": chr(9565),
    "hidden": chr(9618),
}

RANKS: set[Rank] = {"2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"}
WIDTH: int = 7

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


def build_deck() -> Deck:
    deck = set()
    for key in SUITS:
        for rank in RANKS:
            deck.add((rank, SUITS[key]))
    return deck


def get_cards(deck: Deck, num_of_cards: int) -> Deck:
    return set(random.sample(tuple(deck), k=num_of_cards))


def build_card(rank: Rank, suit: str) -> CardMap:
    """
    Returns a card ascii art from a provided rank and suit
    """
    return (
        BOX["top_left"] + BOX["double_line"] * WIDTH + BOX["top_right"],
        BOX["double_pipe"] + f"{rank:<{WIDTH}}" + BOX["double_pipe"],
        BOX["double_pipe"] + f"{suit:^{WIDTH}}" + BOX["double_pipe"],
        BOX["double_pipe"] + f"{rank:>{WIDTH}}" + BOX["double_pipe"],
        BOX["bottom_left"] + BOX["double_line"] * WIDTH + BOX["bottom_right"],
    )


def build_hidden_card() -> CardMap:
    """
    Returns a hiddden card ascii art
    """
    return (
        BOX["top_left"] + BOX["double_line"] * WIDTH + BOX["top_right"],
        BOX["double_pipe"] + f"{BOX["hidden"]:<{WIDTH}}" + BOX["double_pipe"],
        BOX["double_pipe"] + f"{BOX['hidden']:^{WIDTH}}" + BOX["double_pipe"],
        BOX["double_pipe"] + f"{BOX['hidden']:>{WIDTH}}" + BOX["double_pipe"],
        BOX["bottom_left"] + BOX["double_line"] * WIDTH + BOX["bottom_right"],
    )


def render_card(card: Card | None) -> CardMap:
    return build_hidden_card() if card is None else build_card(*card)


def display_cards(cards: Dealer) -> None:
    """
    Prints the cards passed as arguments side by side
    """
    rendered_cards = [render_card(card) for card in cards]

    for row in range(len(rendered_cards[0])):
        for card in rendered_cards:
            print(card[row], end=" ")
        print()


def count_card_value(card: Card) -> int:
    rank, _ = card
    if rank == "A":
        return calculate_ace_value()
    elif rank in {"J", "Q", "K"}:
        return 10
    return int(rank)


def calculate_ace_value() -> int:
    raise NotImplementedError("a = 11 if total + 11 < 21 else 1")


def check_win() -> bool:
    raise NotImplementedError("Return true if player won the round")


def update_balance(bet: int) -> None:
    global balance
    if check_win():
        balance += bet
    else:
        balance -= bet


def check_balance() -> None:
    """
    This function is responisble for checking balance <= zero.
    If the condition is met then it exits the game
    """
    global balance
    if balance <= 0:
        print_message("You're out of balance!")
        exit_game()


def exit_game() -> None:
    import sys

    try:
        sys.exit()
    finally:
        print_message("Thanks for playing! Catch you later :D")


def run_app() -> None:
    """
    Runs the blackgame game
    """
    global balance

    print(logo)
    print("Welcome to Blackjack!")
    print_message("You can press 'ctrl + c' anytime to quit...")
    print(f"Money: ${balance:,}")
    bet: int = get_single_number(
        f"How much do you want to bet? (1 - {balance:,})",
        1,
        balance,
    )
    print(f"Bet: {bet}")
    deck: Deck = build_deck()
    hand: Deck = get_cards(deck, 5)
    deck -= hand
    display_cards(list(hand))


# Driver
try:
    # while True:
    run_app()
except KeyboardInterrupt:
    print_message("You've pressed ctrl + C, exiting...")
    exit_game()

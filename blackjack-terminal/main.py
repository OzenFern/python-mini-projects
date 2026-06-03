import random
from ascii_art import logo

# Typing Hints
StrDict = dict[str, str]
State = dict[str, int]
CardMap = tuple[str, str, str, str, str]
Card = tuple[str, str]
Deck = set[Card]
Hand = list[Card]

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

RANKS: set[str] = {"2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"}
WIDTH: int = 7
NULL_CARD: Card = ("N", "N")

# State
balance: int = 5000
deck: Deck = set()
player_cards: Hand = []
# player_points = 0
dealer_cards: Hand = []
# dealer_points = 0


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
    """
    Converts a given into integer, returns None if the operation fails
    """
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
    """
    Returns a single interger number from the specified range
    """
    while True:
        number = convert_to_int(get_input(message))
        if number is None:
            print_message("Please enter a single number!")
        elif not num_is_between(number, from_num, to_num):
            print_message(f"Please select a number from {from_num} to {to_num}!")
        else:
            return number


def build_deck() -> Deck:
    """
    Builds a deck using SUITS & RANKS
    """
    for key in SUITS:
        for rank in RANKS:
            deck.add((rank, SUITS[key]))
    return deck


def get_cards(num_of_cards: int) -> Hand:
    """
    Get a random number of cards from the deck as specified by the argument
    """
    global deck
    if num_of_cards > len(deck):
        rebuild_deck()
    hand: Hand = random.sample(tuple(deck), k=num_of_cards)
    update_deck(hand)
    return hand


def update_deck(hand: Hand) -> None:
    """
    Updates the deck by removing the dealt cards
    """
    global deck
    deck.difference_update(hand)


def rebuild_deck() -> None:
    """
    Rebuilds a new deck when the current deck does not have sufficient cards
    """
    global deck
    deck = build_deck().difference(player_cards, dealer_cards)


def build_card(rank: str, suit: str) -> CardMap:
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


def render_card(card: Card) -> CardMap:
    return build_hidden_card() if card == NULL_CARD else build_card(*card)


def display_cards(cards: Hand) -> None:
    """
    Prints the cards passed as arguments side by side
    """
    rendered_cards = [render_card(card) for card in cards]

    for row in range(len(rendered_cards[0])):
        for card in rendered_cards:
            print(card[row], end=" ")
        print()


def calclate_total_points(person: str, cards: Hand) -> int:
    """
    Calculates the total value of a Blackjack hand.
    Aces are automatically worth 1 or 11.
    """
    total = 0
    aces = 0

    for rank, _ in cards:
        if rank == "A":
            total += 11
            aces += 1
        if rank in {"J", "Q", "K"}:
            total += 10
        else:
            total += int(rank)

    while total > 21 and aces > 0:
        total -= 10
        aces -= 1

    display_points(person, total)
    return total


def display_points(person: str, total) -> None:
    """
    Prints the points with the name of the person
    """
    print(f"{person}: {total}")


def play_round():
    """
    Show dealer's and player's cards and calculate points for both of them
    """
    dealer_cards = get_cards(1)
    dealer_points = calclate_total_points("Dealer", dealer_cards)
    display_cards(dealer_cards + [NULL_CARD])
    player_cards = get_cards(2)
    player_points = calclate_total_points("Player", player_cards)
    display_cards(player_cards)


def check_win(dealer_points: int, player_points: int) -> bool | None:
    """
    Returns true if player won the round, or None to indicate draw
    """
    raise NotImplementedError("Return true if player won the round")


def update_balance(bet: int) -> None:
    """
    Update the balance based upon the result of the round
    """
    global balance
    if check_win() is None:
        return
    elif check_win():
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
    print(f"Bet: {bet}\n")
    play_round()


# Driver
try:
    # while True:
    run_app()
except KeyboardInterrupt:
    print_message("You've pressed ctrl + C, exiting...")
    exit_game()

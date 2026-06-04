from random import shuffle
from ascii_art import logo

# Typing Hints
StrDict = dict[str, str]
State = dict[str, int]
CardMap = tuple[str, str, str, str, str]
Card = tuple[str, str]
Deck = Hand = list[Card]


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

RANKS: tuple[str, ...] = (
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "J",
    "Q",
    "K",
    "A",
)
WIDTH: int = 7
NULL_CARD: Card = ("N", "N")
RESHUFFLE_AT: int = 15

# State
balance: int = 5000
deck: Deck = []


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
            deck.append((rank, SUITS[key]))
    return deck


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


def shuffle_deck() -> None:
    """
    Shuffles the deck in place
    """
    shuffle(deck)


def deal_cards(num_of_cards: int = 1) -> Hand:
    """
    Get the number of cards specified in the argument from the top of the deck,
    when the cards go below a specified threshold the deck is rebuilt and shuffled
    By default returns a single card from the top of the deck
    """
    if len(deck) < RESHUFFLE_AT:
        build_deck()
        shuffle_deck()
    return [deck.pop() for _ in range(num_of_cards)]


def calclate_total_points(hand: Hand) -> int:
    """
    Calculates the total value of a Blackjack hand.
    Aces are automatically worth 1 or 11.
    """
    total = 0
    aces = 0

    for rank, _ in hand:
        if rank == "A":
            total += 11
            aces += 1
        elif rank in {"J", "Q", "K"}:
            total += 10
        elif rank.isdecimal():
            total += int(rank)

    while total > 21 and aces > 0:
        total -= 10
        aces -= 1

    return total


def is_blackjack(hand: Hand) -> bool:
    """
    Checks whether blacjack is hit
    """
    return len(hand) == 2 and calclate_total_points(hand) == 21


def is_bust(points: int) -> bool:
    return points > 21


def display_points(name: str, total: int) -> None:
    """
    Prints the points with the name of the person
    """
    print(f"{name}: {total}")


def display_hand(name: str, hand: Hand) -> None:
    """
    Prints the points and the name of the person along with their cards
    """
    display_points(name, calclate_total_points(hand))
    display_cards(hand)


def deal_opening_hands() -> tuple[Hand, Hand]:
    """
    Deal the opening hand to the dealer and player
    """
    dealer_hand = deal_cards(1) + [NULL_CARD]
    player_hand = deal_cards(2)

    return dealer_hand, player_hand


def display_hands(dealer_hand: Hand, player_hand: Hand) -> None:
    """
    Show dealer's and player's cards and display points for both of them
    """
    # Display Dealer Hand
    display_hand("Dealer", dealer_hand)

    print()

    # Display Player Hand
    display_hand("Player", player_hand)


def player_turn(hand: Hand) -> Hand:
    """
    Checks if hand is a blakcjack and then asks player
    """
    raise NotImplementedError("Fix other functions first")


def determine_winner(dealer_hand: Hand, player_hand: Hand) -> str:
    """
    Returns the winner or 'push' in case of draw
    """
    dealer_points: int = calclate_total_points(dealer_hand)
    player_points: int = calclate_total_points(player_hand)
    player_blackjack = is_blackjack(player_hand)
    dealer_blackjack = is_blackjack(dealer_hand)

    if player_blackjack:
        return "player"
    elif dealer_blackjack:
        return "dealer"
    elif dealer_points == player_points:
        return "push"
    elif is_bust(player_points):
        return "dealer"
    elif is_bust(dealer_points):
        return "player"
    elif dealer_points == player_points:
        return "push"
    else:
        return "dealer" if dealer_points > player_points else "player"


def update_balance(bet: int, dealer_hand: Hand, player_hand: Hand) -> None:
    """
    Update the balance based upon the result of the round
    """
    global balance
    if determine_winner(dealer_hand, player_hand) == "Push":
        return
    elif determine_winner(dealer_hand, player_hand) == "Player":
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
    dealer_hand, player_hand = deal_opening_hands()
    display_hands(dealer_hand, player_hand)
    determine_winner(dealer_hand, player_hand)
    player_hand = player_turn(player_hand)


# Driver
try:
    # while True:
    run_app()
except KeyboardInterrupt:
    print_message("You've pressed ctrl + C, exiting...")
    exit_game()

import time
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
SHOE_SIZE: int = 6  # Standard Casino Shoe
RESHUFFLE_AT: int = int(SHOE_SIZE * 52 * 0.25)  # Reshuffle at 75% Deck Penetration

# State
balance: float = 5000
bet: float = 0
deck: Deck = []


# Function Definition
def clear_terminal() -> None:
    """
    Standard ANSI escape code to reset the terminal
    Prints Balance and Bet
    """
    print("\033c", end="")


def refresh_game_screen() -> None:
    """
    CLear the terminal
    Prints Balance and Bet
    """
    clear_terminal()
    display_balance()
    print(f"Bet: ${bet:,g}\n")


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


def convert_to_float(number: str) -> float | None:
    """
    Converts a given string into float, returns None if the operation fails
    """
    try:
        return float(number)
    except (ValueError, TypeError):
        return None


def num_is_between(num_to_check: float, from_num: float, to_num: float) -> bool:
    """
    Returns True if the number is between the specified range
    """
    return from_num <= num_to_check <= to_num


def get_single_number(message: str, from_num: float, to_num: float) -> float:
    """
    Returns a single float number from the specified range
    """
    while True:
        number = convert_to_float(get_input(message))
        if number is None:
            print_message("Please enter a single number!")
        elif not num_is_between(number, from_num, to_num):
            print_message(f"Please select a number from {from_num} to {to_num}!")
        else:
            return number


def build_deck() -> Deck:
    """
    Returns a shoe using SUITS & RANKS
    """
    return [(rank, suit) for suit in SUITS.values() for rank in RANKS] * SHOE_SIZE


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
    print_message("Dealer is shuffling a new shoe...")
    time.sleep(1.5)
    shuffle(deck)


def deal_cards(num_of_cards: int = 1) -> Hand:
    """
    Get the number of cards specified in the argument from the top of the deck,
    when the cards go below a specified threshold the deck is rebuilt and shuffled
    By default returns a single card from the top of the deck
    """
    global deck
    if len(deck) < RESHUFFLE_AT:
        deck = build_deck()
        shuffle_deck()
        print_message("New shoe has been shuffled. Good Luck...!")

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


def display_points(name: str, total: str) -> None:
    """
    Prints the points with the name of the person
    """
    print(f"{name}: {total}")


def deal_opening_hands() -> tuple[Hand, Hand]:
    """
    Deal the opening hand to the dealer and player
    """

    return deal_cards(2), deal_cards(2)


def display_hand(name: str, hand: Hand) -> None:
    """
    Prints the points and the name of the person along with their cards
    """
    points = calclate_total_points(hand)
    display_points(name, str(points) + " ??" if NULL_CARD in hand else str(points))
    display_cards(hand)


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
    global balance, bet

    while True:
        player_choices: list[str] = ["(H)it", "(S)tand"]
        if len(hand) == 2 and bet <= balance:
            player_choices.append("(D)ouble down")

        next_choice: str = get_input(" ".join(player_choices)).upper()
        if next_choice == "S":
            return hand
        elif next_choice == "H":
            hand.extend(deal_cards())

            # Automatically end turn if they bust or hit 21
            if calclate_total_points(hand) >= 21:
                return hand

            # Display cards to the player
            display_hand("Player", hand)

        elif next_choice == "D" and len(hand) == 2:
            if bet >= balance:
                print_message("You don't have enough money to double down!")
            else:
                balance -= bet  # Deduct the original bet amount
                bet *= 2  # Double the existing bet
                print_message("Doubling Down...")
                input("Press Enter to continue...")
                return hand + deal_cards()
        elif next_choice == "D":
            print_message("Double down option is not available!")


def dealer_turn(hand: Hand, player_hand: Hand) -> Hand:
    """
    Hits while total is below 17
    """
    while True:
        points = calclate_total_points(hand)
        if points < 17:
            _display_hands(hand, player_hand)
            time.sleep(2)  # Pause before drawing
            hand.extend(deal_cards())

            # Clear screen and display the both hands
            _display_hands(hand, player_hand)
        else:
            return hand


def _display_hands(hand: Hand, player_hand: Hand) -> None:
    """
    Helper function to display hands for dealer's turn
    """
    refresh_game_screen()
    display_hands(hand, player_hand)
    print_message("Revealing Cards...")


def determine_winner(dealer_hand: Hand, player_hand: Hand) -> str:
    """
    Returns the winner or 'push' in case of draw
    """
    dealer_points: int = calclate_total_points(dealer_hand)
    player_points: int = calclate_total_points(player_hand)

    if dealer_points == player_points:
        return "push"
    else:
        return "dealer" if dealer_points > player_points else "player"


def print_winner(result: str) -> None:
    """
    Prints the result on the terminal
    """
    if result == "push":
        print_message("Push! It's a draw!")
    else:
        print_message(f"{result.capitalize()} wins!")


def reset_bet() -> None:
    """
    Resets the bet to zero
    """
    global bet
    bet = 0


def get_bet() -> None:
    """
    Gets the bet from the player and deducts it from the balance
    """
    global balance, bet
    bet += get_single_number(
        f"How much do you want to bet? (1 - {balance:,g})",
        1,
        balance,
    )
    balance -= bet


def update_balance(winner: str) -> None:
    """
    Update the balance based upon the result of the round
    """
    global balance, bet
    if winner == "push":
        balance += bet
    elif winner == "player":
        balance += bet * 2


def display_balance() -> None:
    """
    Displays the current balance to the user
    """
    global balance
    print(f"Money: ${balance:,g}")


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


def run_round() -> None:
    """
    Runs the blackgame game
    """
    global balance, bet

    display_balance()

    reset_bet()
    get_bet()

    refresh_game_screen()

    dealer_hand, player_hand = deal_opening_hands()
    display_hands([dealer_hand[0], NULL_CARD], player_hand)

    # Opening blackjacks
    if is_blackjack(player_hand) or is_blackjack(dealer_hand):
        display_hands(dealer_hand, player_hand)
        winner = determine_winner(dealer_hand, player_hand)

        if winner == "push":
            print_message("Blackjack! But it's a tie, No one wins!")
            balance += bet  # Return the original bet
        elif winner == "player":
            print_message("Blackjack! Player wins!")
            balance += bet * 2.5  # Bet back (1.0) + Profit (1.5)
        else:
            print_message("Dealer has Blackjack! Dealer wins!")
            # Dealer wins, bet is already deducted, no operations carried on balance

        return

    # Player turn
    player_hand: Hand = player_turn(player_hand)
    display_hands([dealer_hand[0], NULL_CARD], player_hand)

    if is_bust(calclate_total_points(player_hand)):
        print_message("Bust! Dealer wins.")
        update_balance("dealer")
        return

    # Dealer turn
    refresh_game_screen()
    print_message("Dealer reveals his cards...")
    dealer_hand: Hand = dealer_turn(dealer_hand, player_hand)
    time.sleep(2)
    refresh_game_screen()
    display_hands(dealer_hand, player_hand)

    if is_bust(calclate_total_points(dealer_hand)):
        print_message("Dealer busts!")
        update_balance("player")
        return

    winner: str = determine_winner(dealer_hand, player_hand)

    print_winner(winner)

    update_balance(winner)


# Driver
try:
    clear_terminal()
    print(logo)
    print("Welcome to Blackjack!")
    print_message("You can press 'ctrl + c' anytime to quit...")
    while True:
        check_balance()
        run_round()
        display_balance()
        input("Press 'ctrl + c' to exit or Enter to play the next round...")
        refresh_game_screen()
except KeyboardInterrupt:
    print_message("You've pressed ctrl + C, exiting...")
    exit_game()

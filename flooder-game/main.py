import bext, random, sys

# TODO:
# Make width & height dynamic
# Dynamic moves per game
# Add difficulty levels
# Add a cap to intensity

# Constants
game_state: dict = {
    "tile_colours": {
        "R": "red",
        "G": "green",
        "B": "blue",
        "P": "purple",
        "Y": "yellow",
        "C": "cyan",
    },
    "width": 20,
    "height": 12,
    "moves": 20,
    "line": chr(9472),
    "pipe": chr(9474),
    "bottom_left": chr(9492),
    "bottom_right": chr(9496),
    "top_left": chr(9484),
    "top_right": chr(9488),
    "block": chr(9608),
}
COLOUR_NAMES = list(game_state["tile_colours"].values())

DIRECTIONS = ((-1, 0), (0, 1), (0, -1), (1, 0))

# Function Definition


def clear_terminal() -> None:
    """
    Standard ANSI escape code to reset the terminal
    """
    print("\033c", end="")


def get_new_board() -> dict:
    """Creates a new board"""
    board = {}
    for x in range(game_state["width"]):
        for y in range(game_state["height"]):
            board[(x, y)] = random.choice(COLOUR_NAMES)
    return board


def smear_colours(board: dict, intensity: int = 20) -> dict:
    """
    Smear the colours vertically, by making two neighbouring blocks the same color.
    More intensity leads to more smearing.
    """
    for _ in range(game_state["width"] * game_state["height"] * intensity):
        x = random.randrange(0, game_state["width"])
        y = random.randrange(1, game_state["height"])
        board[(x, y - 1)] = board[(x, y)]
    return board


def display_board(board: dict):
    """Display colourful board"""

    # Draw the top horizontal line
    bext.fg("white")
    print(
        game_state["top_left"]
        + game_state["line"] * game_state["width"]
        + game_state["top_right"]
    )

    # Draw vertical lines + blocks
    for y in range(game_state["height"]):
        bext.fg("white")
        if y == 0:
            print(">", end="")
        else:
            print(game_state["pipe"], end="")
        for x in range(game_state["width"]):
            bext.fg(board[(x, y)])
            print(game_state["block"], end="")

        # Print the ending vertical line
        bext.fg("white")
        print(game_state["pipe"])

    # Draw the bottom horizontal line
    bext.fg("white")
    print(
        game_state["bottom_left"]
        + game_state["line"] * game_state["width"]
        + game_state["bottom_right"]
    )


def ask_player_for_colour() -> str:
    """Controls which colour is applied at the top left tile"""
    while True:
        bext.fg("white")
        print("Choose one of ", end="")

        for colour in COLOUR_NAMES:
            bext.fg(colour)
            print(f"({colour[0].upper()}){colour[1:]}", end=", ")
        choice = input("(Q)uit: ").upper()

        if choice == "Q":
            exit_game()
        elif choice in game_state["tile_colours"]:
            return game_state["tile_colours"][choice]
        else:
            print(
                "Invalid choice. Please select the first letter of the colour you want to apply..."
            )


def apply_colour(board: dict, user_colour: str) -> None:
    """
    Apply colours based on user input
    """
    original_colour = board[(0, 0)]

    if original_colour == user_colour:
        return

    _flood_fill(board, 0, 0, original_colour, user_colour)


def _flood_fill(
    board: dict, x: int, y: int, original_colour: str, new_colour: str
) -> None:
    """
    Recursive function to paint all neighbours having original_colour with new_colour
    """

    if board[(x, y)] != original_colour:
        return

    board[(x, y)] = new_colour

    for dx, dy in DIRECTIONS:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < game_state["width"] and 0 <= ny < game_state["height"]:
            _flood_fill(board, nx, ny, original_colour, new_colour)


def decrement_moves() -> None:
    game_state["moves"] -= 1
    if game_state["moves"] == 0:
        print("You have run out of moves...!!")
        exit_game()


def has_won(board: dict) -> bool:
    colour = board[(0, 0)]
    for x in range(game_state["width"]):
        for y in range(game_state["height"]):
            if colour != board[(x, y)]:
                return False
    return True


def interpret_win(board) -> None:
    if has_won(board):
        print("Congratulation! You have won the game...!!")
        exit_game()


def exit_game() -> None:
    """Exits the game and resets the terminal colours to default"""
    try:
        sys.exit()
    finally:
        bext.fg("reset")
        bext.bg("reset")
        print("Thanks for playing...")


# Driver
clear_terminal()
bext.bg("black")
new_board = get_new_board()
board = smear_colours(new_board)
while True:
    display_board(board)
    print(f"Moves left: {game_state["moves"]}")
    colour = ask_player_for_colour()
    apply_colour(board, colour)
    decrement_moves()
    interpret_win(board)
    clear_terminal()

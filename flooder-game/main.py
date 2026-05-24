import bext, random, sys

# TODO:
# Make width & height dynamic
# Dynamic moves per game
# Add difficulty levels
# Add bg("Black") in driver instead of function
# Add a cap to intensity
# Use colours list to join and print

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
    "moves_per_game": 20,
    "line": chr(9472),
    "pipe": chr(9474),
    "bottom_left": chr(9492),
    "bottom_right": chr(9496),
    "top_left": chr(9484),
    "top_right": chr(9488),
    "block": chr(9608),
}
COLOUR_NAMES = list(game_state["tile_colours"].values())


def get_new_board() -> dict:
    """Creates a new board"""
    board = {}
    for x in range(game_state["width"]):
        for y in range(game_state["height"]):
            board[(x, y)] = random.choice(COLOUR_NAMES)
    return board


def smear_colours(board: dict, intensity: int = 1) -> dict:
    """
    Smear the colours vertically, by making two neighbouring blocks the same color.
    More intensity leads to more smearing.
    """
    for _ in range(game_state["width"] * game_state["height"] * intensity):
        x = random.randrange(0, game_state["width"])
        y = random.randrange(1, game_state["height"])
        board[(x, y - 1)] = board[(x, y)]
    return board


def default_colours():
    bext.fg("white")
    bext.bg("black")


def display_board(board: dict):
    """Display colourful board"""

    # Draw the top horizontal line
    default_colours()
    print(
        game_state["top_left"]
        + game_state["line"] * game_state["width"]
        + game_state["top_right"]
    )

    # Draw vertical lines + blocks
    for y in range(game_state["height"]):
        default_colours()
        if y == 0:
            print(">", end="")
        else:
            print(game_state["pipe"], end="")
        for x in range(game_state["width"]):
            bext.fg(board[(x, y)])
            print(game_state["block"], end="")

        # Print the ending vertical line
        default_colours()
        print(game_state["pipe"])

    # Draw the bottom horizontal line
    default_colours()
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


def apply_colour(
    user_colour: str, board: dict, x: int, y: int, colour_to_change: str | None = None
):
    """
    Apply selected colour to the adjacent tiles using recursive call
    """
    # Set colour_to_change to the colour of the tile pointed by the cursor
    if not any((x, y)):
        colour_to_change = board[(x, y)]

    # If same colour exists then retrun
    if user_colour == colour_to_change:
        return

    # Assign the selected user_colour to the board
    board[(x, y)] = user_colour

    # Check for left neighbours
    if x > 0 and board[(x - 1, y)] == colour_to_change:
        apply_colour(user_colour, board, x - 1, y, colour_to_change)

    # Check for right neighbours
    if x < game_state["width"] - 1 and board[(x + 1, y)] == colour_to_change:
        apply_colour(user_colour, board, x + 1, y, colour_to_change)

    # Check for top neighbours
    if y < game_state["height"] - 1 and board[(x, y + 1)] == colour_to_change:
        apply_colour(user_colour, board, x, y + 1, colour_to_change)

    # Check for bottom neighbours
    if y > 0 and board[(x, y - 1)] == colour_to_change:
        apply_colour(user_colour, board, x, y - 1, colour_to_change)


def exit_game() -> None:
    """Exits the game and resets the terminal colours to default"""
    try:
        sys.exit()
    finally:
        bext.fg("reset")
        bext.bg("reset")
        print("Thanks for playing...")


# Driver
moves_left = game_state["moves_per_game"]
new_board = get_new_board()
board = smear_colours(new_board)
while True:
    display_board(board)
    print(f"Moves left: {moves_left}")
    colour = ask_player_for_colour()
    apply_colour(colour, board, 0, 0)
    moves_left -= 1

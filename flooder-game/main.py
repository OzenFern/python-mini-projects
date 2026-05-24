import bext, random, sys

# TODO:
# Make width & height dynamic
# Dynamic moves per game
# Add difficulty levels
# Add bg("Black") in driver instead of function
# Add a cap to intensity

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


def get_new_board() -> dict:
    """Creates a new board"""
    board = {}
    for x in range(game_state["width"]):
        for y in range(game_state["height"]):
            colours = tuple(game_state["tile_colours"].values())
            board[(x, y)] = random.choice(colours)
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

        for colour in game_state["tile_colours"].values():
            bext.fg(colour)
            print(f"({colour[0].upper()}){colour[1:]}", end=", ")
        choice = input("or (Q)uit: ").upper()

        if choice == "Q":
            exit_game()
        elif choice in game_state["tile_colours"]:
            return game_state["tile_colours"][choice]
        else:
            print(
                "Invalid choice. Please select the first letter of the colour you want to apply..."
            )


def apply_color():
    pass


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
display_board(board)
colour = ask_player_for_colour()

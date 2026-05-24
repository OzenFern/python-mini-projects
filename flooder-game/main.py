import bext, random

# TODO:
# Make width & height dynamic
# Dynamic moves per game
# Add difficulty levels

game_state = {
    "tile_colours": ("red", "green", "blue", "purple", "yellow", "cyan"),
    "width": 12,
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


def get_new_board():
    """Creates a new board"""
    board = {}
    for x in range(game_state["width"]):
        for y in range(game_state["height"]):
            board[(x, y)] = random.choice(game_state["tile_colours"])
    return board


def smear_colours(board, level=1):
    """Smear the colours horizontally, by making two neighbouring blocks the same color"""
    for _ in range(0, game_state["width"] * game_state["height"], level):
        x = random.randrange(0, game_state["width"])
        y = random.randrange(1, game_state["height"])
        board[(x, y - 1)] = board[(x, y)]
    return board


def default_colours():
    bext.fg("white")
    bext.bg("black")


def display_board(board):
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


# Driver
moves_left = game_state["moves_per_game"]
new_board = get_new_board()
board = smear_colours(new_board)
display_board(board)

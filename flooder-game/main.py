import bext, random, sys

# TODO:
# Make width & height dynamic
# Dynamic moves per game
# Add difficulty levels
# Add a cap to intensity
# Make intensity a dictionary value
# Make board global or add multiple boards for diffculty


game_state: dict[str, int] = {"width": 14, "height": 12, "moves": 20, "intensity": 1}

# Constants

board_box: dict[str, str] = {
    "line": chr(9472),
    "pipe": chr(9474),
    "bottom_left": chr(9492),
    "bottom_right": chr(9496),
    "top_left": chr(9484),
    "top_right": chr(9488),
    "block": chr(9608),
}

TILE_COLOURS: dict[str, str] = {
    "R": "red",
    "G": "green",
    "B": "blue",
    "P": "purple",
    "Y": "yellow",
    "C": "cyan",
}

COLOUR_NAMES: tuple[str, ...] = tuple(TILE_COLOURS.values())
DIRECTIONS: tuple = ((-1, 0), (0, 1), (0, -1), (1, 0))

# Board Typing Hints

Coordinate = tuple[int, int]
Board = dict[Coordinate, str]

# Function Definition


def clear_terminal() -> None:
    """
    Standard ANSI escape code to reset the terminal
    """
    print("\033c", end="")


def get_new_board() -> Board:
    """Creates a new board"""
    board: Board = {}
    for x in range(game_state["width"]):
        for y in range(game_state["height"]):
            board[(x, y)] = random.choice(COLOUR_NAMES)
    return board


def smear_colours(board: Board) -> Board:
    """
    Smear the colours vertically, by making two neighbouring blocks the same color.
    More intensity leads to more smearing.
    """
    for _ in range(
        game_state["width"] * game_state["height"] * game_state["intensity"]
    ):
        x = random.randrange(0, game_state["width"])
        y = random.randrange(1, game_state["height"])
        board[(x, y - 1)] = board[(x, y)]
    return board


def display_board(board: Board):
    """Display colourful board"""

    # Draw the top horizontal line
    bext.fg("white")
    print(
        board_box["top_left"]
        + board_box["line"] * game_state["width"]
        + board_box["top_right"]
    )

    # Draw vertical lines + blocks
    for y in range(game_state["height"]):
        bext.fg("white")
        if y == 0:
            print(">", end="")
        else:
            print(board_box["pipe"], end="")
        for x in range(game_state["width"]):
            bext.fg(board[(x, y)])
            print(board_box["block"], end="")

        # Print the ending vertical line
        bext.fg("white")
        print(board_box["pipe"])

    # Draw the bottom horizontal line
    bext.fg("white")
    print(
        board_box["bottom_left"]
        + board_box["line"] * game_state["width"]
        + board_box["bottom_right"]
    )


def ask_player_for_colour() -> str:
    """Controls which colour is applied at the top left tile"""
    while True:
        bext.fg("white")
        print("Choose one of ", end="")

        for colour in COLOUR_NAMES:
            bext.fg(colour)
            print(f"({colour[0].upper()}){colour[1:]}", end=", ")
        choice: str = input("(Q)uit: ").upper()

        if choice == "Q":
            exit_game()
        elif choice in TILE_COLOURS:
            return TILE_COLOURS[choice]
        else:
            print(
                "Invalid choice. Please select the first letter of the colour you want to apply..."
            )


def apply_colour(board: Board, user_colour: str) -> None:
    """
    Apply colours based on user input and decrement moves when a valid move is played
    """
    original_colour: str = board[(0, 0)]

    if original_colour == user_colour:
        return

    _flood_fill(board, 0, 0, original_colour, user_colour)

    decrement_moves()


def _flood_fill(
    board: Board,
    x: int,
    y: int,
    original_colour: str,
    new_colour: str,
) -> None:
    """
    Recursive function to paint all neighbours having original_colour with new_colour
    """

    if board[(x, y)] != original_colour:
        return

    board[(x, y)] = new_colour

    for dx, dy in DIRECTIONS:
        nx: int = x + dx
        ny: int = y + dy

        if 0 <= nx < game_state["width"] and 0 <= ny < game_state["height"]:
            _flood_fill(board, nx, ny, original_colour, new_colour)


def decrement_moves() -> None:
    game_state["moves"] -= 1
    if game_state["moves"] == 0:
        print("You have run out of moves...!!")
        exit_game()


def has_won(board: Board) -> bool:
    colour: str = board[(0, 0)]
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
new_board: Board = get_new_board()
board: Board = smear_colours(new_board)
while True:
    display_board(board)
    print(f"Moves left: {game_state['moves']}")
    colour: str = ask_player_for_colour()
    apply_colour(board, colour)
    interpret_win(board)
    clear_terminal()

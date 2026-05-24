import bext, random, sys
from ascii_art import logo

# Typing Hints

Coordinate = tuple[int, int]
Board = dict[Coordinate, str]

State = dict[str, int]

Colours = tuple[str, ...]

Tile_Colours = dict[str, str]
# Constants

DIFFICULTIES: dict[str, State] = {
    "easy": {
        "width": 10,
        "height": 8,
        "moves": 22,
        "intensity": 4,
        "colours": 4,
    },
    "medium": {
        "width": 14,
        "height": 12,
        "moves": 20,
        "intensity": 2,
        "colours": 5,
    },
    "hard": {
        "width": 18,
        "height": 15,
        "moves": 17,
        "intensity": 1,
        "colours": 6,
    },
}

BOARD_BOX: dict[str, str] = {
    "line": chr(9472),
    "pipe": chr(9474),
    "bottom_left": chr(9492),
    "bottom_right": chr(9496),
    "top_left": chr(9484),
    "top_right": chr(9488),
    "block": chr(9608),
}


COLOUR_NAMES: Colours = ("red", "green", "blue", "purple", "yellow", "cyan")
DIRECTIONS: tuple = ((-1, 0), (0, 1), (0, -1), (1, 0))

# Game variables derived during runtime
game_state: State = {
    "width": 14,
    "height": 12,
    "moves": 20,
    "intensity": 1,
    "colours": 6,
}

# Function Definition


def clear_terminal() -> None:
    """
    Standard ANSI escape code to reset the terminal
    """
    print("\033c", end="")


def get_input(prompt: str) -> str:
    """
    Retruns a uppercase string with no whitespaces
    """
    return input(prompt).strip().upper()


def set_difficulty() -> None:
    """
    Asks user for difficulty and updates game_state to the desired difficulty
    """
    while True:
        choice: str = get_input(
            "Select difficulty (E)asy, (M)edium, (H)ard or Enter for Default: "
        )
        if not choice:
            print("No difficulty selected, using default settings...")
            return

        mapping: dict[str, str] = {"E": "easy", "M": "medium", "H": "hard"}
        if choice in mapping:
            difficulty: str = mapping[choice]
            print(f"You've chosen {difficulty.capitalize()} difficulty...!!")
            return game_state.update(DIFFICULTIES[difficulty])
        print(
            "Invaild Choice. Please select the first letter of your desired difficulty..."
        )


def build_tile_colours() -> dict[str, str]:
    """
    Build the tile_colour dictionary based on current difficulty
    """
    return {
        colour[0].upper(): colour
        for colour in random.sample(COLOUR_NAMES, k=game_state["colours"])
    }


def get_new_board(tile_colours: Tile_Colours) -> Board:
    """Creates a new board"""
    board: Board = {}
    for x in range(game_state["width"]):
        for y in range(game_state["height"]):
            board[(x, y)] = random.choice(tuple(tile_colours.values()))
    return board


def smear_colours(board: Board, intensity: int) -> Board:
    """
    Smear the colours vertically, by making two neighbouring blocks the same color.
    More intensity leads to more smearing.
    """
    for _ in range(game_state["width"] * game_state["height"] * intensity):
        x = random.randrange(0, game_state["width"])
        y = random.randrange(1, game_state["height"])
        board[(x, y - 1)] = board[(x, y)]
    return board


def display_board(board: Board):
    """
    Display colourful board
    """

    # Draw the top horizontal line
    bext.fg("white")
    print(
        BOARD_BOX["top_left"]
        + BOARD_BOX["line"] * game_state["width"]
        + BOARD_BOX["top_right"]
    )

    # Draw vertical lines + blocks
    for y in range(game_state["height"]):
        bext.fg("white")
        if y == 0:
            print(">", end="")
        else:
            print(BOARD_BOX["pipe"], end="")
        for x in range(game_state["width"]):
            bext.fg(board[(x, y)])
            print(BOARD_BOX["block"], end="")

        # Print the ending vertical line
        bext.fg("white")
        print(BOARD_BOX["pipe"])

    # Draw the bottom horizontal line
    bext.fg("white")
    print(
        BOARD_BOX["bottom_left"]
        + BOARD_BOX["line"] * game_state["width"]
        + BOARD_BOX["bottom_right"]
    )


def ask_player_for_colour(tile_colours: Tile_Colours) -> str:
    """
    Controls which colour is applied at the top left tile
    """
    while True:
        bext.fg("white")
        print("Choose one of ", end="")

        for colour in tile_colours.values():
            bext.fg(colour)
            print(f"({colour[0].upper()}){colour[1:]}", end=", ")
        choice: str = get_input("(Q)uit: ")

        if choice == "Q":
            exit_game()
        elif choice in tile_colours:
            return tile_colours[choice]
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
print(f"{logo}\n Welcome to Flooder Game...!!")
set_difficulty()
tile_colours = build_tile_colours()
new_board: Board = get_new_board(tile_colours)
board: Board = smear_colours(new_board, game_state["intensity"])
while True:
    display_board(board)
    print(f"Moves left: {game_state['moves']}")
    colour: str = ask_player_for_colour(tile_colours)
    apply_colour(board, colour)
    interpret_win(board)
    clear_terminal()

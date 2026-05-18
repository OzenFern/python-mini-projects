from ascii_art import logo
from albums import tracks

app_state = {
    "separator": ":",
    "song_history": [],
}


def display_tracks():
    for i, band in enumerate(tracks, start=1):
        print(f"{i}. {band[0]}")
        for j, song in enumerate(band[1], start=1):
            print(f"\t{j}. {song}")
        print()


def is_separator(choices):
    return app_state["separator"] in choices


def is_len_two(choices):
    return len(choices) == 2


def is_digit(choices):
    return all(choice.strip().isdigit() for choice in choices)


def get_song(choices):
    if not is_len_two(choices):
        return (False, "Two numbers are required!")
    elif not is_digit(choices):  # Handles negative numbering too
        return (False, "Please enter a valid number!")
    else:
        band_num, song_num = list(map(int, choices))
        try:
            if 0 in (band_num, song_num):  # Don't allow zero
                raise IndexError
            band, song = tracks[band_num - 1][0], tracks[band_num - 1][1][song_num - 1]
        except IndexError:
            return (False, "Numbering out of bounds!")
        else:
            add_to_history(band, song)
            return (True, f"Playing: {song} by {band}")


def select_song():
    while True:
        choices = input(
            f"Select a band and song to play using numbers (1{app_state['separator']}1) "
        )
        if not is_separator(choices):
            display_message(f"Please use the '{app_state['separator']}' separator")
            continue
        state, reason = get_song(choices.split(app_state["separator"]))
        display_message(reason)
        if state:
            return


def calculate_width(headers, rows):
    if not rows:
        return tuple(max(len(header), 15) for header in headers)
    columns = zip(*rows)
    widths = [
        max(len(header), max(len(str(item)) for item in column))
        for header, column in zip(headers, columns)
    ]
    return tuple(widths)


def display_line(widths):
    """
    Automatic width calculation.
    1 for '|', 2 spaces per character + 1 trailing character at the end.
    Eg: "|" + "  {content} |"
    """
    print("-" * (sum(widths) + len(widths) * 3 + 1))


def display_header(headings, widths):
    print()
    display_line(widths)
    print("|", end=" ")
    for heading, width in zip(headings, widths):
        print("{:^{}} |".format(heading, width), end=" ")
    print(end="\n")
    display_line(widths)


def add_to_history(band, song):
    app_state["song_history"].insert(0, (band, song))


def display_history():
    headers = ("Sr No.", "Band", "Song")

    display_rows = [
        (i, *row) for i, row in enumerate(app_state["song_history"], start=1)
    ]
    widths = calculate_width(headers, display_rows)
    display_header(headers, widths)
    for row in display_rows:
        print("|", end=" ")
        for item, width in zip(row, widths):
            print(f"{str(item):<{width}} |", end=" ")
        print()
    display_line(widths)


def display_message(message):
    print(f"\n\t{message}\n")


def run_app():
    display_tracks()
    select_song()


def next_action():
    return (
        input(
            "Press, 'c' to change the song \n\t'h' to view history, \n\tor any key to exit: "
        )
        .strip()
        .lower()
    )


# Driver Code
print(logo)
run_app()
while True:
    state = next_action()
    if state == "h":
        display_history()
    elif state == "c":
        run_app()
    else:
        print("Exited Music App")
        break

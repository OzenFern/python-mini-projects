from ascii_art import logo
from albums import tracks

app_state = {"separator": ":", "song_history": [], "headers": ("Band", "Song")}


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
            app_state["song_history"].insert(0, (band, song))
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


def calculate_width(headers=app_state["headers"], rows=app_state["song_history"]):
    if not rows:
        return tuple([15] * len(headers))
    columns = zip(*rows)
    widths = []
    for header, column in zip(headers, columns):
        widths.append(max(len(header), max(len(str(item)) for item in column)))
    return tuple(widths)


def display_line(padding=6):
    band_width, song_width = calculate_width()
    print("-" * (band_width + song_width + padding))


def display_header(headings):
    widths = calculate_width()
    print()
    display_line()
    print("|", end=" ")
    for heading, width in zip(headings, widths):
        print("{:^{}} |".format(heading, width), end=" ")
    print(end="\n")
    display_line()


def display_history():
    band_width, song_width = calculate_width()
    display_header(app_state["headers"])
    for band, song in app_state["song_history"]:
        print(f"| {band:<{band_width}} | {song:<{song_width}} |")
    display_line()


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

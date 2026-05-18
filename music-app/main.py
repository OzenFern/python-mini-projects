from ascii_art import logo
from albums import tracks

app_state = {"separator": ":", "song_history": []}


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
    elif not is_digit(choices):
        return (False, "Please enter a valid number!")
    else:
        band, song = list(map(int, choices))
        try:
            band, song = tracks[band - 1][0], tracks[band - 1][1][song - 1]
            if any((band, song)) < 0:
                raise IndexError
        except IndexError:
            return (False, "Numbering out of bounds!")
        else:
            app_state["song_history"].append((band, song))
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


def display_line(width=45):
    print("-" * width)


def display_header(headings, width=15):
    display_line()
    print("|", end=" ")
    for heading in headings:
        print("{:^{}} |".format(heading, width), end=" ")
    print(end="\n")
    display_line()


def display_history():
    display_header(("Band", "Song"))
    for band, song in app_state["song_history"]:
        print(f"| {band:<15} | {song:<15} |")
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

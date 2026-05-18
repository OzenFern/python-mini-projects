from ascii_art import logo
from albums import tracks


def display_tracks():
    for i, band in enumerate(tracks, start=1):
        print(f"{i}. {band[0]}")
        for j, song in enumerate(band[1], start=1):
            print(f"\t{j}. {song}")
        print()


# Driver Code
print(logo)
display_tracks()

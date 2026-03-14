from ascii_art import logo
import os

# Fucntion Definition
def start_auction():
    os.system("cls" if os.name == "nt" else "clear")
    print(logo)

# Driver
start_auction()
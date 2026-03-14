from ascii_art import logo
import os


# Fucntion Definition
def start_auction():
    os.system("cls" if os.name == "nt" else "clear")
    print(logo)


def get_input(prompt):
    return input(prompt).strip()


def get_bid_amt():
    while True:
        try:
            bid_amt = int(get_input("Enter your bid: $"))
            if bid_amt < 0:
                print("Please enter a positive bid")
                continue
            return bid_amt
        except ValueError:
            print("Please enter a number")


# Driver
start_auction()
name = get_input("Enter your name: ")
get_bid_amt()

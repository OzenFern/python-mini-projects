from ascii_art import logo
import os

# Declaring an empty bidders dictionary
bidder = {}


# Fucntion Definition
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
    print(logo)


def get_input(prompt):
    return input(prompt).rstrip()


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


def append_bidder():
    while True:
        name = get_input("Enter your name: ")
        if name not in bidder:
            break
        print("Name is already registered, write a diffent name.")
    bid = get_bid_amt()
    bidder[name] = bid


def build_bidder_dict():
    while True:
        append_bidder()
        if get_input("Are there any other bidders? (Y/N): ").upper() == "N":
            break
        clear_screen()


def highest_bidder():
    if not bidder:
        print("No bids were placed")
        return
    key = max(bidder, key=bidder.get)
    print(f"The winner is {key} with a bid of ${bidder[key]}")


# Driver
clear_screen()
build_bidder_dict()
highest_bidder()

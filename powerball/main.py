from ascii_art import logo
from random import sample, randint

PRIZES = {
    (5, True): 1000000000,  # Jackpot placeholder
    (5, False): 1000000,
    (4, True): 50000,
    (4, False): 100,
    (3, True): 100,
    (3, False): 7,
    (2, True): 7,
    (2, False): 0,
    (1, True): 4,
    (1, False): 0,
    (0, True): 4,
    (0, False): 0,
}

# Function Definition


def print_message(message):
    print(f"\n\t{message}\n")


def get_input(prompt):
    return input(f"{prompt}\n> ").strip()


def convert_to_int(number):
    try:
        return int(number)
    except ValueError:
        return None


def parse_white_numbers(raw_input):
    return list(map(convert_to_int, raw_input.split()))


def has_five_numbers(numbers):
    return len(numbers) == 5


def has_unique_numbers(numbers):
    return len(set(numbers)) == 5


def check_white_balls(numbers):
    return all(1 <= x <= 69 for x in numbers)


def get_white_balls():
    while True:
        balls = get_input(
            "Enter 5 different numbers from 1 to 69, with spaces between them \n(For Example: 6 23 34 49 68)"
        )
        numbers = parse_white_numbers(balls)
        if None in numbers:
            print_message("Only numbers and spaces are allowed!")
        elif not has_five_numbers(numbers):
            print_message("Please enter exactly 5 numbers!")
        elif not has_unique_numbers(numbers):
            print_message("Please enter 5 distinct numbers!")
        elif not check_white_balls(numbers):
            print_message("Please select numbers from 1 to 69!")
        else:
            return set(numbers)


def num_is_between(num_to_check, from_num, to_num):
    return from_num <= num_to_check <= to_num


def get_single_number(message, from_num, to_num):
    while True:
        number = convert_to_int(get_input(message))
        if number is None:
            print_message("Please enter a single number!")
        elif not num_is_between(number, from_num, to_num):
            print_message(f"Please select numbers from {from_num} to {to_num:,}!")
        else:
            return number


def print_fee(attempts, cost=2):
    total_cost = attempts * cost
    print_message(
        f"It costs ${total_cost:,} to play for {attempts} time{'s' if attempts != 1 else ''}, "
        "But don't worry, I'm sure you'll win it all back."
    )
    return total_cost


def draw_white_balls():
    return sample(range(1, 70), k=5)


def draw_powerball():
    return randint(1, 26)


def play_powerball(user_white_balls, user_powerball):
    winning_white_balls = set(draw_white_balls())
    winning_powerball = draw_powerball()

    white_matches = len((user_white_balls & winning_white_balls))
    powerball_match = user_powerball == winning_powerball

    prize = PRIZES[(white_matches, powerball_match)]

    prize_text = "No win" if prize == 0 else f"${prize:,}"

    white_balls_str = ", ".join(map(str, sorted(winning_white_balls)))
    print(
        f"The winning numbers are: {white_balls_str:<20} Powerball: {winning_powerball:<5} Prize: {prize_text:<15}"
    )
    return prize


def end_game_message(total_cost, prize):
    total_winnings = sum(prize)
    profit = total_winnings - total_cost
    if total_winnings == 0:
        print_message(f"You've wasted your ${total_cost:,} :(")
    elif profit < 0:
        print_message(f"You've lost ${-profit:,}, but not all your money :|")
    else:
        print_message(
            f"Congrats! You've won ${total_winnings:,} and got a profit of ${profit:,} :)"
        )
    print("Thanks for playing! See, you again :D\n")


# Driver Code

print(logo)
white_balls = get_white_balls()
powerball = get_single_number("Enter Powerball number from 1 to 26", 1, 26)
attempts = get_single_number("How many times do you want to play? (Max: 100)", 1, 100)
total_cost = print_fee(attempts)
input("Press Enter to begin...")
prizes = [play_powerball(white_balls, powerball) for _ in range(attempts)]
end_game_message(total_cost, prizes)

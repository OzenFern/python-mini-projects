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

game_state = {
    "cost_per_attempt": 2,
    "initial_amount": 00,
    "attempts": 0,
    "amount_earned": 0,
    "amount_lost": 0,
    "total_amount": 0,
}

user_funds = (
    ("Amount Earned", "amount_earned"),
    ("Amount Lost", "amount_lost"),
    ("Balance", "total_amount"),
)

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
            print_message(f"Please select numbers from {from_num} to {to_num}!")
        else:
            return number


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


def end_round_message(total_cost, prize):
    total_winnings = sum(prize)
    profit = total_winnings - total_cost
    if total_winnings == 0:
        print_message(f"You've wasted your ${total_cost:,} this round :(")
    elif profit < 0:
        print_message(f"You've lost ${-profit:,} this round, but not all your money :|")
    else:
        print_message(
            f"Congrats! You've won ${total_winnings:,} and got a profit of ${profit:,} :)"
        )
    game_state["amount_earned"] += total_winnings


def possible_attempts():
    return game_state["total_amount"] // game_state["cost_per_attempt"]


def calculate_total_amount():
    game_state["total_amount"] = (
        game_state["initial_amount"]
        + game_state["amount_earned"]
        - game_state["amount_lost"]
    )


def calculate_fee(attempts, cost=game_state["cost_per_attempt"]):
    total_cost = attempts * cost
    return total_cost


def print_fee(attempts, total_cost):
    print_message(
        f"It costs ${total_cost} to play for {attempts} time{'s' if attempts != 1 else ''}, "
        "But don't worry, I'm sure you'll win it all back."
    )


def start_round():
    while True:
        max_attempts = possible_attempts()
        attempts = get_single_number(
            f"How many times do you want to play? (Max: {max_attempts})",
            1,
            max_attempts,
        )
        total_cost = calculate_fee(attempts)
        print_fee(attempts, total_cost)
        proceed = get_input(
            "Press Enter to begin or 'r' to re-enter attempts..."
        ).lower()
        if proceed == "r":
            print_message("Reverting...")
            continue
        if attempts <= max_attempts:
            game_state["amount_lost"] += total_cost
        else:
            print_message(
                f"You have insufficient funds to play for {attempts} attempts!"
            )
            continue
        return attempts, total_cost


def can_play_game():
    return game_state["total_amount"] > game_state["cost_per_attempt"]


def print_user_funds():
    print("\tFunds Status: ", end="")
    for txt, key in user_funds:
        print(f"{txt}: ${game_state[key]:,}", end=" | ")
    print("\n")


def powerball_app():
    white_balls = get_white_balls()
    powerball = get_single_number("Enter Powerball number from 1 to 26", 1, 26)
    attempts, total_cost = start_round()
    prizes = [play_powerball(white_balls, powerball) for _ in range(attempts)]
    end_round_message(total_cost, prizes)
    game_state["attempts"] += attempts


def continue_to_play():
    proceed = get_input("Would you like to play again? (y/n)").lower()
    if proceed != "y":
        print_message("Goodbye, hope to see you again...")
        quit()


# Driver Code

print(logo)
game_state["initial_amount"] = get_single_number(
    "Welcome Player!\n How much are you willing to bet?",
    game_state["cost_per_attempt"],
    1_000,
)
print_message(f"You've decided to bet ${game_state['initial_amount']} on Powerball!")
calculate_total_amount()
while can_play_game():
    powerball_app()
    calculate_total_amount()
    print_user_funds()
    continue_to_play()

print("Sadly you're out of funds!...")
see_attempts = get_input(
    "Would you like to see your number of attempts for powerball? (y/n)"
)
if see_attempts == "y":
    print_message(f"Total_Attempts: {game_state['attempts']}")
print("See you again...")

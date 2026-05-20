from ascii_art import logo

app_state = {
    "cost_per_attempt": 2,
    "initial_amount": 100,
    "atempts": 0,
    "amount_earned": 0,
    "amount_lost": 0,
    "total_amount": 0,
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
            return numbers


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


def calculate_total_amount():
    app_state["total_amount"] += (
        app_state["initial_amount"]
        + app_state["amount_earned"]
        - app_state["amount_lost"]
    )


def calculate_fee(attempts, cost=app_state["cost_per_attempt"]):
    total_cost = attempts * cost
    app_state["amount_lost"] += total_cost
    return total_cost


def print_fee(attempts,total_cost):
    print_message(
        f"It costs ${total_cost} to play for {attempts} time{'s' if attempts != 1 else ''}"
    )


# Driver Code

print(logo)
print_message(
    f"Welcome player! You've been given ${app_state['initial_amount']} to play Powerball!"
)
white_balls = get_white_balls()
powerball = get_single_number("Enter Powerball number from 1 to 26", 1, 26)
attempts = get_single_number(
    "How many times do you want to play? (Max: 1000000)", 1, 1000000
)
app_state["atempts"] += attempts
total_cost = calculate_fee(attempts)
print_fee(attempts, total_cost)

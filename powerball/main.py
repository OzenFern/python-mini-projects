from ascii_art import logo

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


def get_white_numbers(numbers):
    return set(map(convert_to_int, numbers.split()))


def check_len(numbers):
    return len(numbers) == 5


def check_white_balls(numbers):
    return all(1 <= x <= 69 for x in numbers)


def get_white_balls():
    while True:
        balls = get_input(
            "Enter 5 different numbers from 1 to 69, with spaces between them \n(For Example: 6 23 34 49 68)"
        )
        numbers = get_white_numbers(balls)
        if None in numbers:
            print_message("Only numbers and spaces are allowed!")
        elif not check_len(numbers):
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
        if number == None:
            print_message("Please enter a single number!")
        elif not num_is_between(number, from_num, to_num):
            print_message(f"Please select numbers from {from_num} to {to_num}!")
        else:
            return number


# Driver Code

print(logo)
white_balls = get_white_balls()
powerball = get_single_number("Enter Powerball number from 1 to 26", 1, 26)
num_of_plays = get_single_number(
    "How many times do you want to play? (Max: 1000000)", 1, 1000000
)

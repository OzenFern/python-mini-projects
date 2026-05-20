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
        return 0


def get_white_numbers(numbers):
    return set(map(convert_to_int, numbers))


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
        if 0 in numbers:
            print_message("Enter numbers only!")
        elif not check_len(numbers):
            print_message("Please enter 5 distinct numbers!")
        elif not check_white_balls(numbers):
            print_message("Please select numbers from 1 to 69!")
        else:
            return numbers


def check_powerball(number):
    return 1 <= number <= 26


def get_powerball():
    while True:
        number = convert_to_int(get_input("Enter Powerball number from 1 to 26"))
        if number == 0:
            print_message("Please enter a single number!")
        elif check_powerball(number):
            print_message("Please select numbers from 1 to 26!")
        else:
            return number


# Driver Code

print(logo)
white_balls = get_white_balls()
powerball = get_powerball()

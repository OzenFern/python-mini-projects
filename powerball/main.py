from ascii_art import logo

# Function Definition


def print_message(message):
    print(f"\n\t{message}\n")


def get_input(prompt):
    return input(prompt).strip()


def get_numbers(numbers):
    return set(map(int, numbers.split()))


def check_len(numbers):
    return len(numbers) == 5


def check_white_balls(numbers):
    return all(1 <= x <= 69 for x in numbers)


def get_white_balls():
    while True:
        balls = get_input(
            "Enter 5 different numbers from 1 to 69, with spaces between them \n (For Example: 6 23 34 49 68): "
        )
        numbers = get_numbers(balls)
        if not check_len(numbers):
            print_message("Please enter 5 distinct numbers!")
            continue
        elif not check_white_balls(numbers):
            print_message("Please select numbers from 1 to 69!")
            continue
        return numbers


def check_red_ball(number):
    return 1 <= number <= 26


def get_red_ball():
    pass


# Driver Code

print(logo)
print(get_white_balls())
get_red_ball()

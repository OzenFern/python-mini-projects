import os
from random import choice
from ascii_art import logo
from quiz import quiz

# Function Definition


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def greeting_message(no_of_questions):
    print(logo)
    print(
        f"There are a total of {no_of_questions} questions, you can skip a question anytime by typing 'skip'"
    )
    return input("Press any key to continue... ")


def initialise_players():
    """Initialise player names with along with scores"""
    while True:
        players = get_input(
            "\nEnter the names of two players separated by space: "
        ).split()
        if len(players) == 2:  # The total number of players in the game are 2
            return players, dict.fromkeys(players, 0)
        print("Please enter the names of two players!")
        continue


def get_widths(players):
    name_width = max(len("Name"), max(len(name) for name in players))
    score_width = max(len("Score"), max(len(str(score)) for score in players.values()))
    return name_width, score_width


def print_separator(width):
    print("-" * width)


def display_score(players, name_width, score_width):
    total_width = name_width + score_width + 7  # Add 7 for padding and separators
    print("\n" + "Score Board".upper().center(total_width))
    print_separator(total_width)
    print(f"| {'Name':^{name_width}} | {'Score':^{score_width}} |")
    print_separator(total_width)

    for name, score in players.items():
        print(f"| {name:^{name_width}} | {score:^{score_width}} |")
        print_separator(total_width)
    print()


def get_input(prompt):
    return input(prompt).strip().title()


def select_player(names):
    """Randomly select and return a player name (key)"""
    return choice(names)


def next_player(names, current_player):
    return names[(names.index(current_player) + 1) % len(names)]


def ask_question(question, solution, players, current_player):
    print(f"\tIt's {current_player}'s turn!\n")
    attempts = 2
    while attempts > 0:
        answer = get_input(f"Question: {question}\n\tAnswer: ")
        clear_screen()
        if answer == solution:
            print("Right Answer!")
            players[current_player] += 1  # Increment score by 1
            break
        elif answer == "Skip":
            print(f"Skipped {current_player}'s turn...")
            break
        else:
            print("Wrong Answer!")
            attempts -= 1


def run_quiz(names, players, name_width, score_width):
    current_player = select_player(names)
    for data in quiz.values():
        question = data["question"]
        solution = data["answer"]
        ask_question(question, solution, players, current_player)
        display_score(players, name_width, score_width)
        current_player = next_player(names, current_player)


def find_winner(names, players_score):
    max_score = max(players_score.values())
    winners = [name for name in names if players_score[name] == max_score]

    if len(winners) > 1:
        print(f"Draw between: {', '.join(winners)} with a score of {max_score}!")
    else:
        print(f"\t{winners[0]} is the winner, with a score of {max_score}")


def display_answers():
    for q_no, value in quiz.items():
        print(f"Question {q_no}: {value['question']}")
        print(f"\tAnswer: {value['answer']}")


def show_answers():
    checkbox = get_input("Enter 'Y' to see reveal answers of the quiz: ")
    if checkbox == "Y":
        print_separator(60)
        display_answers()
        print_separator(60)
    return


# Driver Code

# Initializing the game
clear_screen()
greeting_message(len(quiz))
names, players = initialise_players()
name_width, score_width = get_widths(players)
run_quiz(names, players, name_width, score_width)
find_winner(names, players)
show_answers()

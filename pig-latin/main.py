# Constants
VOWELS = ("A", "E", "I", "O", "U")


# Function Definition
def get_input(prompt):
    return input(prompt).strip()


def break_msg(message):
    return message.split()


def check_vowel(word: str):
    """
    Checks whether the first alphabet in the word is a vowel.
    Returns True/False based on the result.
    """
    for char in word:
        if char.isalpha():
            return char in VOWELS
    return False

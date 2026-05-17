from ascii_art import logo

# Constants
VOWELS = ("A", "E", "I", "O", "U")


# Function Definition
def get_input(prompt):
    """
    Return a string with no trailing whitespaces
    """
    return input(prompt).strip()


def split_msg(message):
    """
    Returns a list with elements split on whitespaces
    """
    return message.split()


def word_separator(word):
    """
    Splits a word into:
    prefix : leading non-alphabetic characters
    core   : alphabetic core
    suffix : trailing non-alphabetic characters
    Returns a tuple
    """
    start = 0
    end = len(word)

    # Get prefix end index
    while start < end and not word[start].isalpha():
        start += 1

    # Get suffix start index
    while end > start and not word[end - 1].isalpha():
        end -= 1

    return word[:start], word[start:end], word[end:]


def check_letter(text):
    """
    Returns three Boolean Values
    Checks if the first letter is a vowel,
    Checks if the first letter is in uppercase
    Checks if the whole word is in uppercase
    """
    return (text[0].upper() in VOWELS, text[0].isupper(), text.isupper())


def transform_text(text):
    """
    Transform text into pig latin.
    If empty return empty string.
    """

    if not text:
        return text

    vowel, is_title, is_upper = check_letter(text)
    if vowel:
        text += "yay"
    else:
        text = text[1:] + text[0] + "ay"

    if is_upper:
        return text.upper()
    elif is_title:
        return text.capitalize()
    return text


def rebuild_msg(msg_list):
    text_list = [prefix + core + suffix for prefix, core, suffix in msg_list]
    return " ".join(text_list)


# Driver Code
print(logo)
message = get_input("Enter a message in English: ")
split_message = split_msg(message)
pig_latin = []
for word in split_message:
    prefix, core, suffix = word_separator(word)
    core = transform_text(core)
    pig_latin.append((prefix, core, suffix))

print(f"Pig Latin: {rebuild_msg(pig_latin)}")

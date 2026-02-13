from logo import logo
from string import ascii_uppercase, digits

CHARACTERS = ascii_uppercase + digits

def pretty_line():
    print(f"{' _ ' * 30:^120}\n")

def get_input(prompt):
    return input(prompt).upper().strip()

def build_shift_map(shift_number):
    """
    Returns a dictionary mapping each character in CHARACTERS
    to its shifted counterpart based on shift_number.
    """
    length = len(CHARACTERS)
    shift_number %= length
    shifted_chars = CHARACTERS[shift_number:] + CHARACTERS[:shift_number]
    return dict(zip(CHARACTERS, shifted_chars))

def caesar_cipher(text, shift_number, mode):
    """
    Encrypts or decrypts a message using Caesar Cipher.
    mode: 'E' for encrypt, 'D' for decrypt
    """
    if mode == "D":
        shift_number = -shift_number
    cipher_map = build_shift_map(shift_number)
    return "".join(cipher_map.get(char, char) for char in text)

def get_mode():
    mode = get_input("Type 'E' to encrypt and 'D' to decrypt: ")
    while mode not in ("E", "D"):
        mode = get_input("Enter 'E' to encrypt and 'D' to decrypt: ")
    return mode

def get_message(mode):
    return get_input(f"Enter message to {'encrypt' if mode == 'E' else 'decrypt'}:\n")

def get_shift_number():
    while True:
        try:
            return int(get_input("Enter the shift number:\n"))
        except ValueError:
            print("Please enter an integer number")

def play_again():
    choice = get_input("Type 'N' to exit, or press any key to cipher again: ")
    return choice != "N"

# Driver Code

print(logo)
while True:
    pretty_line()
    mode = get_mode()
    message = get_message(mode)
    shift = get_shift_number()
    result = caesar_cipher(message, shift, mode)
    print(f"Your {'decoded' if mode == 'D' else 'encoded'} Caesar Cipher is: {result}")
    pretty_line()
    if not play_again():
        print("Bye, see you again!")
        break
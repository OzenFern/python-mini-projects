from logo import logo
from characters import CHARACTERS


def pretty_line():
    print(f"{' _ ' * 30:^120}\n")


def caesar_cipher(p_initial_text, p_shift_number, p_cipher_type):
    initial_list = list(p_initial_text)
    if p_cipher_type == "D":
        p_shift_number = -p_shift_number
    for i in range(len(initial_list)):
        if initial_list[i] in CHARACTERS:
            index = CHARACTERS.index(initial_list[i]) + p_shift_number
            index %= len(CHARACTERS)
            initial_list[i] = CHARACTERS[index]
    final_text = "".join(initial_list)

    return f"Your {'decoded' if p_cipher_type == 'D' else 'encoded'} Caesar Cipher is: {final_text}"


print(logo)

program_end = False
while not program_end:
    pretty_line()
    enc_dec = input("Type 'E' to encrpt and 'D' to decrypt: ").upper()
    while enc_dec != "E" and enc_dec != "D":  # Get a valid option
        enc_dec = input("Enter 'E' to encrpt and 'D' to decrypt: ").upper()
    message = input(
        f"Enter message to {'encrypt' if enc_dec == 'E' else 'decrypt'}:\n"
    ).upper()
    while True:
        try:
            shift_number = int(input("Enter the shift number:\n"))
            break
        except ValueError:
            print("Please enter an integer number")
    output = caesar_cipher(message, shift_number, enc_dec)
    print(output)
    pretty_line()
    again = input("Type 'N' to exit, or press any key to cipher again: ").upper()
    if again == "N":
        program_end = True
        print("Bye, see you again!")

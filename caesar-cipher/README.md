# Caesar Cipher

A simple Python program to **encrypt and decrypt messages** using the classic **Caesar Cipher** technique. This project is part of my mini-projects repository for practicing Python and basic cryptography.

## About

The Caesar Cipher is one of the oldest and simplest encryption methods, where each letter in a message is shifted by a fixed number of positions in the alphabet. This program allows you to:

- Encrypt messages by shifting letters forward.
- Decrypt messages by shifting letters backward.
- Choose a custom shift number.
- Run repeatedly until you choose to exit.

_Includes a fun ASCII logo to make the program more lively!_

## Usage

1. Run the program.
2. Choose `'E'` to encrypt or `'D'` to decrypt.
3. Enter your message (letters only; converted to uppercase automatically).
4. Enter the shift number.
5. See the encoded or decoded result.
6. Repeat or exit by typing `'N'`.

## Example

```
Type 'E' to encrpt and 'D' to decrypt: E
Enter message to encrypt:
Hello World
Enter the shift number:
6
Your encoded Caesar Cipher is: NKRRU CUXRJ
_  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _

Type 'N' to exit, or press any key to cipher again: Y
_  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _

Type 'E' to encrpt and 'D' to decrypt: D
Enter message to decrypt:
NKRRU CUXRJ
Enter the shift number:
6
Your decoded Caesar Cipher is: HELLO WORLD
_  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _

Type 'N' to exit, or press any key to cipher again: N
Bye, see you again!
```

## Dependencies

- **Python** (no external libraries required)

import hangman

new_game = True

while new_game:
    hangman.start_game()
    secret_word = hangman.initialize_secret_word()
    guessed_letters = []
    lives = hangman.initialise_lives()
    initial_lives = lives
    blanks = hangman.create_blanks_list(secret_word)
    mode, cap, percentage = hangman.get_difficulty()
    total_hints = hangman.max_hints(secret_word, cap, percentage)
    hints_left = total_hints
    hangman.display_game_status(
        lives, initial_lives, blanks, hints_left, total_hints, mode
    )

    while True:
        guess = hangman.get_guess()
        if guess == "!":
            can_hint, reason = hangman.can_use_hints(
                blanks, hints_left, lives, initial_lives, mode
            )
            if can_hint:
                hints_left = hangman.apply_hint(secret_word, blanks, hints_left)
            else:
                print(f"{reason}\n")
                continue
        elif guess in guessed_letters:
            print("You have already guessed this letter!")
            continue
        else:
            guessed_letters.append(guess)
            if guess in secret_word:
                hangman.update_blanks(guess, blanks, secret_word)
            else:
                lives -= 1
        hangman.display_game_status(
            lives, initial_lives, blanks, hints_left, total_hints, mode
        )
        result = hangman.decide_result(blanks, lives)
        if result:
            print(f"\n{result.center(50)}")
            break

    new_game = hangman.play_again()
    if not new_game:
        print("Thanks for playing! See you next time!")

import hangman

new_game = True

while new_game:
    hangman.start_game()
    secret_word = hangman.initialize_secret_word()
    guessed_letters = []
    lives = hangman.initialise_lives()
    blanks = hangman.create_blanks_list(secret_word)
    hangman.display_all(lives, blanks)
    play_game = True
    
    while play_game:
        guess = hangman.get_guess()
        if guess in guessed_letters:
            print("You have already guessed this letter!")
            continue
        guessed_letters.append(guess)
        
        hangman.clear_screen()
        if guess in secret_word:
            hangman.update_blanks(guess, blanks, secret_word)
        else:
            lives -= 1
        hangman.display_all(lives, blanks)
        result = hangman.decide_result(blanks, lives)
        print(result)
        play_game = True if result == '' else False

    new_game = hangman.play_again()
    if not new_game:
        print("Thanks for playing! See you next time!")

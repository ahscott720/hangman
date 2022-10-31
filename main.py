from hangman import hangman_game

if __name__=="__main__":
    while True:
        hangman_game()
        another_game = input("Do you want to paly another game? (y to continue)")
        if another_game.upper() == "Y":
            continue
        else:
            break
    
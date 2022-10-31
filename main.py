from hangman import hangman_game

if __name__=="__main__":
    hangman_game()
    while True:
        another_game = input("Do you want to play another game? (y to continue)")
        if another_game in ["Y", "y"]:
            hangman_game()
        elif another_game in ["N", "n"]:
            break
        else:
            print("The input should be y or n")

    
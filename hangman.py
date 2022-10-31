
import random
import os
import time

def print_hangman(guess_times):
    '''
    print the hangman based on the guess times
    '''
    print("----------------")
    if guess_times == 6:
        print("|       /      |")
        for i in range(1,4):
            print("|              |")
    if guess_times == 5:
        print("|      o/      |")
        for i in range(1,4):
            print("|              |")
    if guess_times == 4:
        print("|      o/      |")
        print("|      |       |")
        for i in range(1,3):
            print("|              |")
    if guess_times == 3:
        print("|      o/      |")
        print("|     /|       |")
        for i in range(1,3):
            print("|              |")
    if guess_times == 2:
        print("|      o/      |")
        print("|     /|\      |")
        for i in range(1,3):
            print("|              |")
    if guess_times == 1:
        print("|      o/      |")
        print("|     /|\      |")
        print("|     /        |")
        for i in range(1,2):
            print("|              |")
    if guess_times == 0:
        print("|      o/      |")
        print("|     /|\      |")
        print("|     / \      |")
        for i in range(1,2):
            print("|              |")
    if guess_times>1:
        print(f"| {guess_times} times left |")
    elif guess_times==1:
        print(f"|  last guess  |")
    else:
        print("|  You lose!   |" )
    
    print("----------------")

def create_guess_word(word):
    '''
    put the blank in the input "word" randomly, and preserve the original copy of the word
    return two lists
    '''
    letterList=[]
    for i, chr in enumerate(word):
        letterList.append(chr) # put the characters in a list 
    letterForGuess = letterList.copy() # make a copy of the original copy
    for i in range(5):
        letterForGuess[random.randrange(0, len(letterForGuess))]="_" # create the blank list with maxmun 5
    return letterList, letterForGuess

def random_line(file_name):
    '''
    choose a random line from a txt file
    '''
    lines = open(file_name).read().splitlines()
    return random.choice(lines)

def hangman_game():
    '''
    the base of the hangman game
    '''
    guess_times = 6
    guess_word = random_line("wordlist.txt") #fetch a word from the file
    lists = create_guess_word(guess_word) # let the word become a original and a blanked version
    word = lists[0]
    word_with_blank = lists[1]

    while guess_times > 0:  
        os.system("cls")  #start the terminal with a clear screen
        print_hangman(guess_times)
        for i, chr in enumerate(word_with_blank):  # print the word for guessing
            print(f"{chr} ", end="")
        character = input("\nplease enter a character:")
        if character in word:       # check whether the input character is in the word
            for i, chr in enumerate(word):    # replace the correct character to the blank
                if character == chr:
                    word_with_blank[i]=chr
            print("your guess is correct!")  
            time.sleep(1)           # sleep 1 second to show the print
        else:                       # if the input character is not inside
            guess_times -= 1
            print("your guess is wrong!")
            time.sleep(1)

        if word == word_with_blank:  # when the word is completed, stop the while loop 
            os.system("cls")
            print_hangman(guess_times)  # print the currect status
            print(f"The correct word is '{guess_word}'")
            print("you win")
            break

    if guess_times == 0: # when the guess is out of range, then terminate the game and show correct word 
        os.system("cls")
        print_hangman(0)
        print("You Lose!!")
        print(f"The correct word is '{guess_word}'")




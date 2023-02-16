# ----------------------------------------------------------------------
# Name:      wordle
# Purpose:   implement the wordle game
# Author(s): Nick Tang, Yuto
# Date: 2/16/23
# ----------------------------------------------------------------------
"""
This program is a CLI wordle game.

It prompts the user for a filename containing a word bank, selects a random
word from that word bank as a wordle, then prompts the user for up to six
guesses in order to guess the correct wordle.
"""

import string
import random

# Constant assignments
RED = '\033[91m'     # to print text in red: print(RED + text)
GREEN = '\033[92m'   # to print a letter in green: print(GREEN + text)
YELLOW = '\033[93m'  # to print a letter in yellow: print(YELLOW + text)
DEFAULT = '\033[0m'  # to reset the color print(DEFAULT + text)


def choose_wordle(filename):
    """
    Read the file specified and choose a random 5-letter word.
    :param filename: (string) name of the file to choose the wordle from
    :return: (string) the mystery word in uppercase
    """
    # Open file
    with open(filename) as file:
        content = file.readlines()

        # Stores all possible wordles
        all_wordles = []

        # Split lines by spaces, then add to wordle list if word is
        # alphabetical and 5 letters long
        for line in content:
            split_line = line.split()
            for word in split_line:
                if word.isalpha() and len(word) == 5:
                    all_wordles.append(word.upper())

        # Select a random 5-letter wordle from wordle list
        wordle = random.choice(all_wordles)

        return wordle


def check(wordle, guess):
    """
    Check the player's guess against the wordle and return a string
    representing the color coded feedback for the specified guess.
    Red indicates that the guessed letter is NOT in the word.
    Yellow indicates that the letter is in the word but not in the
    correct spot.
    Green indicates that the letter is in the word in the correct spot.
    :param wordle: (string) the mystery word in upper case
    :param guess: (string) the user's guess in upper case
    :return: (string) a string of red, yellow or green uppercase letters
    """
    # HINTS: create a working list of letters in the wordle
    # go over the letters in the guess and check for green matches
    # add the green matches to their correct position in an output list
    # remove the green matches from the working list
    # go over the letters in the guess again
    # compare them to the letters in working list
    # add yellow or red color and add them to their position in output
    # list
    # join the output list into a colored string

    # deconstruct wordle into letters
    wordle_list = list(wordle)
    print(wordle_list)

    for i in range(5):
        if wordle[i] == guess[i]:
            print(f'guess letter in wordle and in right place: {guess[i]}')
            wordle_list.remove(guess[i])
        elif wordle[i] != guess[i] and guess[i] not in wordle_list:
            print(f'guess letter not in wordle: {guess[i]}')
        else:
            print(f'guess letter in wordle but wrong place: {guess[i]}')
            wordle_list.remove(guess[i])


    # check for matching letters by iterating through string
        # if matching, add that letter in green to output list
        # else, add yellow or green letter to output list

    # return output list

    pass  # enter your code and take out the pass statement

def feedback(attempt):
    """
    Print the feedback corresponding to the number of attempts
    it took to guess the wordle.
    :param attempt: (integer) number of attempts needed to guess
    :return: None
    """
    print(f'Attempt {attempt}')


def prompt_guess():
    """
    Prompt the user repeatedly for a valid 5 letter guess that contains
    only letters.  Guess may be in lower or upper case.
    :return: (string) the user's valid guess in upper case
    """
    while True:
        guess = input('Please enter your 5 letter guess: ')
        if guess.isalpha():
            if guess.isupper():
                return guess
            elif guess.islower():
                return guess.upper()


def play(wordle):
    """
    Implement the wordle game with all 6 attempts.
    :param wordle: (string) word to be guessed in upper case
    :return: (boolean) True if player guesses within 6 attempts
             False otherwise
    """
    # guesses within 6 attempts
    guesses_left = 6

    # call the prompt_guess function to prompt the user for each attempt
    while guesses_left > 0:
        guess = prompt_guess()

        # check for correct guess
        if guess == wordle:
            print('congrats dude')

        # call the check function to build the colored feedback string
        feedback_str = check(wordle, guess)

        # call the feedback function to print the final feedback if the user
        if feedback_str == wordle:
            feedback(7 - guesses_left)





def main():
    # 1. prompt the player for a filename
    filename = input('Please enter the filename: ')

    # 2. call choose_wordle and get a random mystery word in uppercase
    #    from the file specified
    wordle = choose_wordle(filename)

    # 3. call play to give the user 6 tries
    play(wordle)

    # 4. if the user has not guessed the wordle, print the correct
    #    answer
    print(f'The correct answer is {wordle}')




if __name__ == '__main__':
    main()

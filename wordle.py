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
        # Split lines by spaces
        content = [line.split() for line in file.readlines()]

        # Stores all possible wordles
        all_wordles = []

        # Add to wordle list if word is alphabetical and 5 letters long
        for line in content:
            for word in line:
                word = word.strip(',".')
                if word.isalpha() and len(word) == 5:
                    # print('Accepted: ' + word)
                    all_wordles.append(word.upper())

        # print(len(all_wordles))

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
    # deconstruct wordle into list of characters
    wordle_list = list(wordle)

    # instantiate result array with fixed size
    res = [None] * 5

    # check for matching letters in correct plac
    for i in range(5):
        # if matching, add green letter to result list
        if wordle[i] == guess[i]:
            wordle_list[i] = ''
            res[i] = GREEN + guess[i]

    # check for nonmatching and matching but wrong place letters
    for i in range(5):
        # if not matching and not in wordle list, add red letter to result list
        if wordle[i] != guess[i] and guess[i] not in wordle_list:
            res[i] = RED + guess[i]
        # if not matching but in wordle list, add yellow letter to result list
        if wordle[i] != guess[i] and guess[i] in wordle_list:
            wordle_list[i] = ''
            res[i] = YELLOW + guess[i]
        # print(wordle_list)

    # combine letters and print colored string
    colored_str = ''.join(res)
    print(colored_str)

    # return output list
    return guess


def feedback(attempt):
    """
    Print the feedback corresponding to the number of attempts
    it took to guess the wordle.
    :param attempt: (integer) number of attempts needed to guess
    :return: None
    """
    match attempt:
        case 1:
            print('Genius!')
        case 2:
            print('Magnificent!')
        case 3:
            print('Impressive!')
        case 4:
            print('Splendid!')
        case 5:
            print('Great!')
        case 6:
            print('Phew!')


def prompt_guess():
    """
    Prompt the user repeatedly for a valid 5 letter guess that contains
    only letters.  Guess may be in lower or upper case.
    :return: (string) the user's valid guess in upper case
    """
    while True:
        guess = input('Please enter your 5 letter guess: ')
        if guess.isalpha() and len(guess) == 5:
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

    while guesses_left > 0:
        attempt_num = 7 - guesses_left
        print(DEFAULT + f'Attempt {attempt_num}')
        # call the prompt_guess function to prompt the user for each attempt
        guess = prompt_guess()

        # call the check function to build the colored feedback string
        feedback_str = check(wordle, guess)

        # call the feedback function to print the final feedback if the user
        if feedback_str == wordle:
            feedback(attempt_num)
            return True

        guesses_left -= 1

    return False



def main():
    # prompt the player for a filename
    filename = input('Please enter the filename: ')

    # call choose_wordle and get a random mystery word in uppercase from the
    # file specified
    wordle = choose_wordle(filename)

    #print(wordle)

    # call play to give the user 6 tries
    if not play(wordle):
        # if the user has not guessed the wordle, print the correct answer
        print(DEFAULT + f'The correct answer is {wordle}')


if __name__ == '__main__':
    main()

from colorama import init
import utils
import os
import sys
from termcolor import cprint 
from pyfiglet import figlet_format
import re
import random

# Strip colors if stdout is redirected
init(strip=not sys.stdout.isatty())

ROOT_LOCATION = os.path.dirname(os.path.realpath(__file__))
SECRET_WORDS_LIST = os.path.join(ROOT_LOCATION, "secret-words-list.txt")

def start_wordle_game():
    # Reading the secret words list and formatting it properly
    secret_words_list = utils.read_secret_words(SECRET_WORDS_LIST)

    # Picking up six words for the game
    random_picked_word = random.choice(secret_words_list)
    
    # Clearing the command line prompt
    os.system('cls' if os.name == 'nt' else 'clear')

    # Starting the game
    user_attempts = 6
    utils.prepare_wordle_game_text()
    cprint(f"=========================\nStart Guessing The Word.\n=========================\n", "cyan")
    tryagain = False

    for attempts in range(1,7):
        cprint(f"Your Attempt Number ({attempts}/6): ", "white")
        user_word = input()
        
        for word_index,word_char in enumerate(user_word):
            if word_char.lower() == random_picked_word[word_index].lower():
                user_word = user_word.replace(word_char, "\033[37;42m" + word_char + "\033[m")
            elif re.search(word_char, random_picked_word, re.IGNORECASE):
                user_word = user_word.replace(word_char, "\033[30;43m" + word_char + "\033[m")
            else:
                pass

        if tryagain:
            cprint("\n=======================================\nNot In The Word List, Please Try Again.\n=======================================\n", "yellow", attrs=["bold"])
            cprint("==================\nPress [0] To Quit.\n==================\n", "red", attrs=["bold"])
        
        print("Result: ", user_word)

        if user_word == "0":
            cprint("======================\nThank You For Playing.\n======================\n", "green", attrs=["bold"])
            sys.exit()


def main():
    # Printing menu and title
    cprint(figlet_format("MY WORDLE GAME", font="bubble", width=60), "white", attrs=["bold"])
    cprint("\nAre You Ready To Play A Game Of Wordle???\n", "white")
    cprint("[1] -> Start Game", "green")
    cprint("[0] -> Exit\n", "red")
    cprint("Choose An Option: ", "white")

    try:
        user_option = int(input())
    except ValueError:
        cprint("\n====================\nInvalid Menu Option.\n====================", "red", attrs=["bold"])
        sys.exit()

    if user_option == 0:
        cprint("\n=======================\nYou Have Left The Game.\n=======================", "red", attrs=["bold"])
        sys.exit()

    if user_option == 1:
        start_wordle_game()

if __name__ == "__main__":
    main()
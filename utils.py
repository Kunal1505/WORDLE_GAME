import random
from termcolor import cprint 
import time
import sys
import os

def read_secret_words(filename, sep='\n'):
    file_ = open(filename, 'r')
    words_list = file_.read().upper().split(sep)

    # Remove empty quotes the the words_list
    words_list = [elem for elem in words_list if elem != ""]

    file_.close()

    return words_list

def prepare_wordle_game_text():
    timer = 0
    cprint("Preparing Your Game:\n", "white")
    loading = f"[----------------------------------------]"
    backtrack = '\b'*len(loading)

    while timer < 4:
        sys.stdout.write(backtrack + loading)
        sys.stdout.flush()
        loading = loading.replace("-","/",10)
        time.sleep(1)
        timer += 1
    time.sleep(0.2)
    sys.stdout.write(backtrack)
    os.system('cls' if os.name == 'nt' else 'clear')
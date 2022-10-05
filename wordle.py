import random
import sys
from termcolor import colored

def print_menu():
    print("Let's play Wordle!")
    print("Enter a five letter word.")

def read_random_word():
    with open("words.txt") as f:
        words = f.read().splitlines()
        return random.choice(words)

word = read_random_word()

for attempt in range(1, 7):
    guess = input().lower()

    for i in range( min(len(guess), 5)):
        if guess[i] == word[i]:
            print(colored(guess[i], 'green'), end="")
import random
import sys
from colorama import Fore, Back, init
init(autoreset=True)

def print_menu():
    print("Let's play Wordle!")
    print("Enter a five letter word.")

def read_random_word():
    with open("words.txt") as f:
        words = f.read().splitlines()
        return random.choice(words)

print_menu()
word = read_random_word()


for attempt in range(1, 7):
    guess = input().lower()

    for i in range( min(len(guess), 5)):
        if guess[i] == word[i]:
            print(Back.GREEN + guess[i], end="")
        elif guess[i] in word:
            print(Back.YELLOW + guess[i], end="")
        else:
            print(guess[i], end="")

    if guess == word:
        print(Fore.BLUE + "You guessed the word in ", attempt, "tries!")
        break
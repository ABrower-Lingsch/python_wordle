import random
import sys
from colorama import Fore, Back, init
init(autoreset=True)


def print_menu():
    print(Fore.CYAN + ''' 
 __         ______     ______   ______        ______   __         ______     __  __        __     __     ______     ______     _____     __         ______       
/\ \       /\  ___\   /\__  _\ /\  ___\      /\  == \ /\ \       /\  __ \   /\ \_\ \      /\ \  _ \ \   /\  __ \   /\  == \   /\  __-.  /\ \       /\  ___\      
\ \ \____  \ \  __\   \/_/\ \/ \ \___  \     \ \  _-/ \ \ \____  \ \  __ \  \ \____ \     \ \ \/ ".\ \  \ \ \/\ \  \ \  __<   \ \ \/\ \ \ \ \____  \ \  __\      
 \ \_____\  \ \_____\    \ \_\  \/\_____\     \ \_\    \ \_____\  \ \_\ \_\  \/\_____\     \ \__/".~\_\  \ \_____\  \ \_\ \_\  \ \____-  \ \_____\  \ \_____\    
  \/_____/   \/_____/     \/_/   \/_____/      \/_/     \/_____/   \/_/\/_/   \/_____/      \/_/   \/_/   \/_____/   \/_/ /_/   \/____/   \/_____/   \/_____/    
                                                                                                                                                                 
    ''')
    print("Enter a five letter word. You get 6 guesses.\n")


def read_random_word():
    with open("words.txt") as f:
        words = f.read().splitlines()
        return random.choice(words)


play_again = ""

while play_again != "n":
    word = read_random_word()
    print_menu()
    for attempt in range(1, 7):
        guess = input().lower()

        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')

        for i in range(min(len(guess), 5)):
            if guess[i] == word[i]:
                print(Back.GREEN + guess[i], end="")
            elif guess[i] in word:
                print(Back.YELLOW + guess[i], end="")
            else:
                print(guess[i], end="")
        print()

        if guess == word:
            print(Fore.CYAN + "You guessed the word in",
                  attempt, Fore.CYAN + "tries!")
            break

        elif attempt == 6:
            print(Fore.RED + "You ran out of guesses! The word was",
                  word, Fore.RED + ". Better luck next time...")

    play_again = input(
        Fore.YELLOW + "Enter 'n' to exit or enter any other key to play again. ")
    if play_again == "n":
        print(Fore.MAGENTA + "Thanks for playing! :) <3")
        break

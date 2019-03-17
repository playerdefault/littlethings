## Core logic for the game
## 0: rock
## 1: paper
## 2: scissors

import random

def randomizer():
    return random.randint(0,2)

def main(input):
    computer_choice = randomizer()

    if (computer_choice == 0):
        print("The computer chose Rock!")
    elif (computer_choice == 1):
        print("The computer chose Paper!")
    else:
        print("The computer chose Scissors!")

    ## Return True if the human won, False if computer won, None if draw
    if input == 0:
        if computer_choice == 1:
            return False
        elif computer_choice == 2:
            return True
    elif input == 1:
        if computer_choice == 0:
            return True
        elif computer_choice == 2:
            return False
    elif input == 2:
        if computer_choice == 0:
            return False
        elif computer_choice == 1:
            return True
    elif input == computer_choice:
        return None

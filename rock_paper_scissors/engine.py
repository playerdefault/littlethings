## Core logic for the game
## 0: rock
## 1: paper
## 2: scissors

import random

def randomizer():
    return random.randint(0,2)

def main(input):
    output = randomizer()

    if (output == 0):
        print("The computer chose Rock!")
    elif (output == 1):
        print("The computer chose Paper!")
    else:
        print("The computer chose Scissors!")

    ## Return True if the human won, False if computer won, None if draw
    if input == 0:
        if output == 1:
            return False
        elif output == 2:
            return True
    elif input == 1:
        if output == 0:
            return True
        elif output == 2:
            return False
    elif input == 2:
        if output == 0:
            return False
        elif output == 1:
            return True
    elif input == output:
        return None

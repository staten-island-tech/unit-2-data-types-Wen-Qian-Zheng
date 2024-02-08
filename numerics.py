import random # we import a package named random which comes with random functions
from random import *


def guess():
    lowervalue = int(input("Gimme a lowest number rn: "))
    uppervalue = int(input("SLAY OKAY GIMME A HIGHEST NUMBER: "))
    number = randint(lowervalue, uppervalue) # randomly picks an integer ranging from 1 to 100
    attempt = 0 # variable value starts at 0
    success = False # IF THE PROGRAM HAS NOT RUN THRU SUCCESSFULLY : DEFINES THE SUCCESS VARIABLE AS FALSE
    while success == False: # while the number hasn't been guessed yet
        choice = (input("Guess a number: "))  # makes a statement and a space for you to guess your integer
        if int(choice) < int(lowervalue):
            print(f"Are you dumb the lowest is {lowervalue}")
        if int(choice) > int(uppervalue):
            print(f"Dawg r u stupid the highest is {uppervalue}")
        if int(choice) == int(number): # if your chosen number IS the random number
            print(f"SLAY U DID IT LETS GOOOO IT WAS {number}")
            print(f"U TOOK {attempt+1} TRIES LOSER")
            success = True # UH HUH AND THEN SUDDENLY THE SUCCESS VARIABLE IS TRUE SO IT NO LONGER RUNS BC THE CODE ONLY RUNS WHEN FALSE
            playagain = input("Hey gangy u wanna play again ya or na: ")
            if playagain == "ya":
                guess()
            else:
                print("what a bum")
                break
        if int(choice) < int(number):
            print("GO HIGHER DUMMY")
            attempt = attempt + 1
        if int(choice) > int(number):
            print("GO LOWER LOSER")
            attempt = attempt + 1


# "\033[1;31m This is red text")

guess()
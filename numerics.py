import random # we import a package named random which comes with random functions
from random import *

x = "\n"
print(x*10)

def guess():
    lowervalue = int(input("Gimme a lowest number: ")) # WOAH RED TEXT
    print(x)
    uppervalue = int(input("SLAY OKAY GIMME A HIGHEST NUMBER: "))
    print(x)
    number = randint(lowervalue, uppervalue) # randomly picks an integer ranging from 1 to 100
    attempt = 0 # variable value starts at 0
    success = False # IF THE PROGRAM HAS NOT RUN THRU SUCCESSFULLY : DEFINES THE SUCCESS VARIABLE AS FALSE
    while success == False: # while the number hasn't been guessed yet
        choice = (input("Guess a number: "))  # makes a statement and a space for you to guess your integer
        if int(choice) < int(lowervalue):
            print(x*2)
            print(f"Are you dumb the lowest is {lowervalue}")
        elif int(choice) > int(uppervalue):
            print(x*2)
            print(f"Dawg r u stupid the highest is {uppervalue}")
        elif int(choice) == int(number): # if your chosen number IS the random number
            print(x*2)
            print(f"SLAY U DID IT LETS GOOOO IT WAS {number}")
            print(f"U TOOK {attempt+1} TRIES LOSER")
            success = True # UH HUH AND THEN SUDDENLY THE SUCCESS VARIABLE IS TRUE SO IT NO LONGER RUNS BC THE CODE ONLY RUNS WHEN FALSE
            print(x*2)
            playagain = input("Hey gangy u wanna play again ya or na: ")
            if playagain == "ya":
                guess()
            else:
                print("what a bum")
                print(x*2)
                break
        if int(choice) < int(number):
            print("GO HIGHER DUMMY")
            print(x*2)
            attempt = attempt + 1
        elif int(choice) > int(number):
            print("GO LOWER LOSER")
            print(x*2)
            attempt = attempt + 1

guess()

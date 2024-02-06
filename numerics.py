import random # we import a package named random which comes with random functions
from random import *

def guess():
    number = randint(1, 100) # randomly picks an integer ranging from 1 to 10
    attempt = 0
    success = False
    while success == False: # while the number hasn't been guessed yet
        choice = float(input("Guess a number from 1-100: ")) # makes a statement and a space for you to guess your integer
        if int(choice) == int(number): # if your chosen number IS the random number
            print(f"SLAY U DID IT LETS GOOOO IT WAS {number}")
            print(f"U TOOK {attempt+1} TRIES LOSER")
            success = True
            playagain = input("Hey gangy u wanna play again ya or na: ")
            if playagain == "ya":
                guess()
            else:
                print("loser")
                break
        if int(choice) < int(number):
            print("GO HIGHER DUMMY")
            attempt = attempt + 1
        if int(choice) > int(number):
            print("GO LOWER :V")
            attempt = attempt + 1


guess()
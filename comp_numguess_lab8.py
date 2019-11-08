"""
Part 1: The player gets 6 tries to guess a number 
b/w 0-100.
Part 2: The computer guesses a number b/w 0-100
and the player decides win or not
"""

import random

def main():
    player = input("User or Computer: ")
    if player.lower() == "user":
        user()
    elif player.lower() == "computer":
        computer()
    
def user():
    # Part 1: player guesses the number
    # play one round until win/lose or player wants to exit
    guess = ""
    # generate random int 0-100
    my_num = random.randint(0, 100)
    tries_left = 6
    win = False
    # while tries left
    while win!=True and tries_left>0:    
        guess = input("Your Guess: ")
        if guess == "exit":
            win = None
            break
        guess = int(guess)
        # check int domain else issue warning
        if 0<=guess<=100 :
            if guess == my_num:
                print("Hooray you won! The number was %d" % my_num)
                win = True
            elif guess> my_num:
                print("Too high!")
                tries_left -= 1
            elif guess< my_num:
                print("Too low!")
                tries_left -= 1
            else:
                print("unexpected error -_-")
        else:
            print("That number is not between 0 and 100!")
        
    if win == False:
        print("You are out of guesses. The number was %d." % my_num)
   
   
        
def computer():
    # Part 2: Computer guesses the number
    # uses binary search to guess the next one
    win = False
    guess = random.randint(0, 100) # start with ranodm guess
    low = 0 # hightest low (floor)
    high = 100  # lowest high (ceiling) 
    while win!=True:
        print("Computer Guess: %d" % guess)
        high_or_low = input()
        # binary search implementation 
        if high_or_low == "+":
            if guess > low:
                low = guess
            guess = guess + ((high-guess)//2)            
        elif high_or_low == "-":
            if guess < high:
                high = guess
            guess = (guess+low)//2
        elif high_or_low == "win":
            print("Hooray the computer won!")
            win = True
        

main()
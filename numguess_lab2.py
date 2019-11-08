# This program asks the user to guess
# a number b/w [1, 20]
# The player get 6 tries and the program
# will inform if a guess is too high/low

import random

def main():
    # loop until player wants to exit
    play_again = True
    while play_again == True:
        # generate random int
        my_num = random.randint(1, 20)
        tries_left = 6
        win = False
        # while tries left and game not won yet
        while win!=True and tries_left>0:    
            guess = int(input("Enter a guess (1-20): "))
            # check int domain else issue warning
            if 1<=guess<=20 :
                if guess == my_num:
                    print("Correct! The number was %d" % my_num)
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
                print("That number is not between 1 and 20!")
            
        if win == False:
            print("You are out of guesses. The number was %d." % my_num)
        # ask for another game 
        again = input("Would you like to play again? (y/n) ")
        if again.lower() == "n":
            play_again = False
            print("GoodBye!")
        elif again.lower() == "y":
            play_again = True
        else:
            print("Not valid answer. Exiting anyways, bye! :p")
            play_again = False

main()
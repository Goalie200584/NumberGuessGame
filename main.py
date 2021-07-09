"""I want it to pick a number between 1-100 then have the player guess it until they get it right. When the players 
guesses it right it will say congradulatiosn and show the amount of times it takes for them to guess the number.
After every guess it will give the user  a hint on how close they are. It will say you are less than or equal to 25 numbers away
also will say less then or equal to 50 numbers away"""


import random
from typing import Iterator 

# Hints should take in a guess and the number randomly generated and return the distance away from that number,
# and print a message describing how close the guess was to the number 
def hints(pc_number, i):
    
    
    if i == 0:
        guess = input("We have a chosen a random number between 1 and 100. What is your first guess?")
        
        
    else:
        guess = input("What is your next guess?")
    
    guess = int(guess)

    if guess > 100 or guess < 1:
        print("This number is outside the bounds of our game. PLease try again")
        return -1

    reg_value_away = guess - pc_number
    
    value_away = abs(reg_value_away)
    
    
    

    if value_away == 0:

        print()
        print("Great job You got it!!")
        print("It took you " + str(i) +" turns to get " + str(pc_number) + ", try to go faster next time!")
        return 0

    elif value_away <= 5:
        if guess > pc_number:
            print()
            print("Your number is " + str(guess))
            print("Our number is 5 or less numbers away and is lower than your number")
            print()
        
        elif guess < pc_number:
            print()
            print("Your number is " + str(guess))
            print("Our number is 5 or less numbers away and is higher then your number")
            print()
    

        return -1
        

    elif value_away <= 10:
        if guess > pc_number:
            print()
            print("Your number is " + str(guess))
            print("Our number is 10 or less numbers away and is lower than your number")
            print()

        elif guess < pc_number:
            print()
            print("Your number is " + str(guess))
            print("Our number is 10 or less numbers away and is higher then your number")
            print()
        
        return -1
        

    elif value_away <= 25:
        if guess > pc_number:
            print()
            print("Your number is " + str(guess))
            print("Our number is 25 or less numbers away and is lower than your number")
            print()

        elif guess < pc_number:
            print()
            print("Your number is " + str(guess))
            print("Our number is 25 or less numbers away and is higher then your number")
            print()
        return -1
        

    elif value_away <= 50:
        if guess > pc_number:
            print()
            print("Your number is " + str(guess))
            print("Our number is 50 or less numbers away and is lower than your number")
            print()

        elif guess < pc_number:
            print()
            print("Your number is " + str(guess))
            print("Our number is 50 or less numbers away and is higher then your number")
            print()
        return -1
        

    else:
        if guess > pc_number:
            print()
            print("Your number is " + str(guess))
            print("Our number is between 50 and 100 numbers away from yours \nand is lower than your number")
            print()

        elif guess < pc_number:
            print()
            print("Your number is " + str(guess))
            print("Our number is between 50 and 100 numbers away from yours \nand is higher then your number")
            print()
        return -1
        
        
    
        

def perform():
    iterator = 0
    chosen_num = random.randint(1,100)
    # print(chosen_num)
    hints_status = hints(chosen_num, iterator)
    while hints_status == -1:
        iterator += 1
        hints_status = hints(chosen_num, iterator)

# Run hints to get the distance away
# If the distance away != 0, run it again until distance away = 0ss

    





if __name__ == '__main__':
    i = 0
    while i == 0:
        perform()
        play_again = input("Do you want to play again? (Y/N)")

        if play_again.upper() == "Y":
            print()
        
        elif play_again.upper() == "YES":
            print()
        
        else:
            i += 1 

    
    
    
    # Do something when the loop ends

    
        




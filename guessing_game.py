"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""
import random


def start_game():
    print("Welcome to the Number Guessing Game!")
    attempts = 0
    random_num = random.randint(1,10)
    
    
    
    while True:
        prompt_for_guess = int(input("Guess the random 1-10 number here:  "))  
        if prompt_for_guess > random_num:
            attempts += 1
            print("It's Lower!")
            prompt_for_guess
            
        elif prompt_for_guess < random_num:
            attempts += 1
            print("It's Higher!")
            prompt_for_guess
            
        elif prompt_for_guess == random_num:
            attempts += 1
            print("You've got it!")
            print("It took you {} tries!".format(attempts))
            break
            
    while True:
        restart_game = input("Would you like to play again? [y]es/[n]o:  ")
        
        if restart_game.lower() == "y":
            print("High Score is {}".format(attempts))
            start_game()
        elif restart_game.lower() == "n":
            print("Thanks for playing! See ya next time!")
            break
            return False
        else:
            print("{} is not a valid response. please type 'y' for yes or 'n' for no.".format(restart_game))
            restart_game
    
start_game()
    
    
    
      
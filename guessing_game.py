
"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""
import random

highScore = []


def start_game():
    highScore
    print("Welcome to the Number Guessing Game!")
    attempts = 0
    random_num = random.randint(1,10)
    
    
    
    while True:
        try:
            prompt_for_guess = int(input("Guess the random 1-10 number here:  "))
        except ValueError:
            print("Not a valid response. Please guess again.....with a number this time. -_- ")
            continue
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
            highScore.append(attempts)
            break
            
    while True:
        restart_game = input("Would you like to play again? [y]es/[n]o:  ")
        
        if restart_game.lower() == "y": 
            print("High Score is {}".format(min(highScore)))
            start_game()
        elif restart_game.lower() == "n":
                #highScore only kept track of while player continues to restart game
            print("High Score is {}".format(min(highScore)))
            print("Thanks for playing! See ya next time!")
            break
            return False
        else:
            print("{} is not a valid response. please type 'y' for yes or 'n' for no.".format(restart_game))
            restart_game
    
start_game()
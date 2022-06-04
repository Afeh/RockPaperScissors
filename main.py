#importing the python random and sys module 
import random, sys

#List to store the possible choices of the computer
computer_options = ["Rock", "Paper", "Scissors"]
available_options = ["Rock", "Paper", "Scissors", "Quit"]

#Using random.choice() to select the computers choice by random
# cpu_choice = random.choice(available_options)
# print(cpu_choice)

#The main loop of the game
while True:
    cpu_choice = random.choice(computer_options)
    print("Welcome to Rock Paper Scissors!")
    
    #Taking input for the player's choice
    player_choice = input("What is your choice? Type in [Rock, Paper, Scissors or Quit (if you want to exit)]: ")

    #Making sure the player's input corresponds to the availble options 
    player_choice = player_choice.capitalize()
    
    if player_choice not in available_options:
        print("Error... You didn't enter a required option")
        continue
    
    #If the player decides to quit
    if player_choice == "Quit":
        print("Byeeee")
        
        sys.exit()

    #Displaying the choice of the Player and the computer
    print("Player ({}) : CPU ({})".format(player_choice, cpu_choice))
    
        
    #In the case of a tie
    if cpu_choice == player_choice:
        print("It's a Tie! ")
        
        #Play again Option
        play_again = input("Would you love to play again? [y/n] ")
        if play_again == "y":
            continue
        else:
            break

    #Rock v Paper
    if cpu_choice == "Rock" and player_choice == "Paper":
        print("You win!")

    elif player_choice == "Rock" and cpu_choice == "Paper":
        print("Awww.. You lost.")
        play_again = input("Would you love to play again? [y/n] ")
        if play_again == "y":
            continue
        else:
            sys.exit()
    
    #Rock v Scissors
    elif cpu_choice == "Rock" and player_choice == "Scissors":
        print("Awww.. You lost.")
        play_again = input("Would you love to play again? [y/n] ")
        if play_again == "y":
            continue
        else:
            sys.exit()
    
    elif player_choice == "Rock" and cpu_choice == "Scissors":
        print("You win!")

    #Scissors v Paper
    elif cpu_choice == "Scissors" and player_choice == "Paper":
        print("Awww.. You lost.")
        play_again = input("Would you love to play again? [y/n] ")
        if play_again == "y":
            continue
        else:
            sys.exit()
    elif cpu_choice == "Paper" and player_choice == "Scissors":
        print("You win!")

    #End of the Conditions.
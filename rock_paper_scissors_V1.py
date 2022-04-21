import random

while True:
#--------------------------------------------------------------------------------------------  
# choices  
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)

    player = None

#-------------------------------------------------------------------------------------------- 
# player choice   
    
    while player not in choices:
        player = input("rock, paper, or scissors? ").lower()

#-------------------------------------------------------------------------------------------- 
# in case of tie  

    if player == computer:
        print("--------------------------------------")
        print(f"Computer: {computer}")
        print(f"Player: {player}")
        print("Tie")

#-------------------------------------------------------------------------------------------- 
# checking the winner

    elif player == 'rock':
        if computer == 'paper':
            print("--------------------------------------")
            print(f"Computer: {computer}")
            print(f"Player: {player}")
            print("You lose!")

        if computer == 'scissors':
            print("--------------------------------------")
            print(f"Computer: {computer}")
            print(f"Player: {player}")
            print("You win!")

#-------------------------------------------------------------------------------------------- 
# checking the winner

    elif player == 'paper':
        if computer == 'rock':
            print("--------------------------------------")
            print(f"Computer: {computer}")
            print(f"Player: {player}")
            print("You win!")

        if computer == 'scissors':
            print("--------------------------------------")
            print(f"Computer: {computer}")
            print(f"Player: {player}")
            print("You lose!")

#-------------------------------------------------------------------------------------------- 
# checking the winner

    elif player == 'scissors':
        if computer == 'paper':
            print("--------------------------------------")
            print(f"Computer: {computer}")
            print(f"Player: {player}")
            print("You win!")

        if computer == 'rock':
            print("--------------------------------------")
            print(f"Computer: {computer}")
            print(f"Player: {player}")
            print("You lose!")

#-------------------------------------------------------------------------------------------- 
# Play Again

    responses = ['Y', 'N']
    playAgain = None
    while playAgain not in responses:
        print("--------------------------------------")
        playAgain = input("Do you want to play again? (Y/N) ").upper()
    if playAgain == 'N':
        break
    else:
        pass
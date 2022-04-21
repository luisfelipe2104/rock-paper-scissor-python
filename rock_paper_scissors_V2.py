import random

def play():
    choices = ['r', 'p', 's']
    user = None
    while user not in choices:
        user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n").lower()
        
    computer = random.choice(choices)
    
    if user == computer:
        return "it's a tie!"
    
    
    if is_win(user, computer):
        return "You won!"
    
    return "You lost!"    # if is_win and tie return false, the game will return 'You lost'

#---------------------------------------------------

# return True if player wins
def is_win(player, oponent):
    if (player == 'r' and oponent == 's') or (player == 's' and oponent == 'p') or (player == 'r' and oponent == 's'):
        return True

#---------------------------------------------------

# game loop
while True:
    print(play())
    responses = ['Y', 'N']
    playAgain = None
    while playAgain not in responses:
        playAgain = input("Do you want to play again? (Y/N) ").upper()
        
    if playAgain == 'N':
        break
    else:
        pass
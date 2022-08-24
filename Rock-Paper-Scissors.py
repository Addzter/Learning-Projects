import random


def play():
    print("Lets play Rock, Paper, Scissors!")
    print()
    user = input("Make a choice!\n"
                 "'r' for Rock!\n"
                 "'p' for Paper!\n"
                 "'s' for Scissors!\n"
                 "Choose here: ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        if user == 'r':
            return "I choose Rock! It\'s a Draw!"
        elif user == 'p':
            return "I choose Paper! It\'s a Draw!"
        else:
            return "I choose Scissors! It\'s a Draw!"

    
    if is_win(user, computer):
        if user == 'r':
            return "I choose Scissors! Damn! You win!"
        elif user == 'p':
            return "I choose Rock! Damn! You win!"
        else:
            return "I choose Paper! Damn! You win!"

    else:
        if user == 'r':
            return "I choose Paper! You lost! Sorry!"
        elif user == 'p':
            return "I choose Scissors! You lost! Sorry!"
        else:
            return "I choose Rock! You lost! Sorry!"


# r > s, s > p, p > r
def is_win(player, opponent):
    # returns true if player wins
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or \
            (player == 'p' and opponent == 'r'):
        return True


print(play())

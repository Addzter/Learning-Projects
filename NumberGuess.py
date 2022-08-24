from random import randint

# From a FreeCodeCamp Youtube tutorial

def guess(x):
    ran_num = randint(1, x)
    user_guess = 0
    turn = 0
    while turn < 5:
        user_guess = int(input(f"Guess a number between 1 and {x}: "))
        if user_guess > x:
            print("That's higher than the boundary, dummy. You lose automatically.")
            turn += 6
            break
        if user_guess < ran_num:
            turn += 1
            print("Wrong! You guessed too low.")
            print("You have " + str(5 - turn) + " guesses left.")
            print()
        elif user_guess > ran_num:
            turn += 1
            print("Wrong! You guessed too high.")
            print("You have " + str(5 - turn) + " guesses left.")
            print()
        else:
            print(f"Correct!! The answer was: {ran_num}")
            turn += 6
            break
    else:
        print(f"You're out of guesses! You lose. It was {ran_num}")
        

from random import randint

# From FreeCodeCamp 12 Projects Tutorial

def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = randint(low, high)
        else:
            guess = low   # can also be high
        feedback = input(f"Is {guess} too high(H), too low(L), or correct(C)?").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'Haha! I win! You can never fool me! I got {guess}!')



computer_guess(100)

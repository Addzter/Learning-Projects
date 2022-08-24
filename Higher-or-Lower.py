import random

# First Fully built solo project

def is_higher(card, next_card):
    # Checks to make sure its not a tie. Ties = lose
    if card == next_card:
        return False

    # Block deals with both cards being numbers
    elif type(card) == int and type(next_card) == int:
        if card > next_card:
            return True
        elif card < next_card:
            return False
    # Block deals with a number going against a picture card
    elif type(card) == int and type(next_card) == str:
        return False

    # Below deals with picture vs number (always win)
    elif type(card) == str and type(next_card) == int:
        return True

    # Below deals with all picture vs picture scenarios
    elif type(card) == str and type(next_card) == str:
        if card != "A":
            if card == "K":
                if next_card == "A":
                    return False
                else:
                    return True
            elif card == "Q":
                if next_card == "K" or next_card == "A":
                    return False
                else:
                    return True
            elif card == "J":
                return False
        else:
            return True


def play():
    has_lost = False
    choice = ""
    score = 0
    player_card = random.choice(["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"])

    print("Welcome to Play Your Cards Right!")
    print()

    while not has_lost:
        choice_card = random.choice(["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"])

        print(f"Your card is {player_card}. Will the next card be:")
        choice = input("Higher('H') or Lower('L'): ")

        # Check if cards aren't the same. Same = loss
        if choice_card != player_card:
            # If the next card is higher
            if is_higher(choice_card, player_card):
                if choice.lower() == "h":
                    print(f"Correct! It was {choice_card}!")
                    print()
                    player_card = choice_card
                    score += 1
                elif choice.lower() == "l":
                    print(f"Wrong! It was {choice_card}. You lose.")
                    print(f"Your score: {score}")
                    has_lost = True
                    break
            # If it's not higher
            elif not is_higher(choice_card, player_card):
                if choice.lower() == "l":
                    print(f"Correct! It was {choice_card}!")
                    print()
                    player_card = choice_card
                    score += 1
                elif choice.lower() == "h":
                    print(f"Wrong! It was {choice_card}. You lose.")
                    print(f"Your score: {score}")
                    has_lost = True
                    break
        else:  # If cards are the same
            print(f"Unlucky! It was {choice_card}. Ties get you nothing. Sorry!")
            print(f"Your score: {score}")
            has_lost = True

(play())

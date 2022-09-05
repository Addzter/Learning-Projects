import random

card_shoe = [
    'A','A','A','A','K','K','K','K','Q','Q','Q','Q','J','J','J','J',2,2,2,2,3,3,3,3,
4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,'A','A','A','A','K','K','K','K','Q','Q','Q','Q','J','J','J','J',2,2,2,2,3,3,3,3,
4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,'A','A','A','A','K','K','K','K','Q','Q','Q','Q','J','J','J','J',2,2,2,2,3,3,3,3,
4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,'A','A','A','A','K','K','K','K','Q','Q','Q','Q','J','J','J','J',2,2,2,2,3,3,3,3,
4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,'A','A','A','A','K','K','K','K','Q','Q','Q','Q','J','J','J','J',2,2,2,2,3,3,3,3,
4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,]

# Initializing essential functions

balance = 1000.00

dealer_hand = []

player_hand = []


# Selects 1 card and removes it from the shoe. Returns the card
def take_card():

    selection = random.choice(card_shoe)
    card_shoe.remove(selection)

    if type(selection) == int:
        return selection
    else:
        return selection


# Returns dealers initial hand
def deal_dealer():
    dealer_hand = []
    dealer_hand.append(take_card())
    return dealer_hand


# Returns player initial hand
def deal_player():
    player_hand = []
    player_hand.append(take_card())
    player_hand.append(take_card())
    return player_hand


# Returns total as a LIST of a given hand, takes a hand (list) as input
def starting_total(hand):
    cards_of_ten = ['J', 'Q', 'K']
    total = []
    ace_total = []
    running_total = 0

    # Function deals with a hand of 1 card differently to hands of more
    if len(hand) == 1:
        if type(hand[0]) == int:  # Card is 1 number
            total.append(hand[0])
            return total
        elif hand[0] in cards_of_ten:  # Hands of J,Q,K
            total.append(10)
            return total
        else:  # Hands of 1 A
            ace_total.append(1)
            ace_total.append(11)
            return ace_total
    # Deals with hands of 2 or more below--------------
    else:  # Only for 2 cards
        # Both 2 cards are int
        if type(hand[0]) == int and type(hand[1]) == int:
            running_total += (hand[0] + hand[1])
            total.append(running_total)
            return total
        # 1 card is int and 1 is str
        elif (type(hand[0]) == int and type(hand[1]) == str) or (type(hand[0]) == str and type(hand[1]) == int):
            # If card 2 is JQK
            if hand[1] in cards_of_ten:
                running_total += (hand[0] + 10)
                total.append(running_total)
                return total
            # If card 1 is JQK
            elif hand[0] in cards_of_ten:
                running_total += (10 + hand[1])
                total.append(running_total)
                return total
            # If card 2 is A
            elif hand[1] == 'A':
                ace_total.append(1)
                ace_total.append(11)
                ace_total[0] += hand[0]
                ace_total[1] += hand[0]
                return ace_total
            # If card 1 is A
            elif hand[0] == 'A':
                ace_total.append(1)
                ace_total.append(11)
                ace_total[0] += hand[1]
                ace_total[1] += hand[1]
                return ace_total
        # Both cards are str
        else:
            # Both cards are JQK
            if hand[0] in cards_of_ten and hand[1] in cards_of_ten:
                running_total += 20
                total.append(running_total)
                return total
            # One card is JQK, 1 card is A
            elif hand[0] in cards_of_ten or hand[1] in cards_of_ten:
                running_total += 21
                total.append(running_total)
                return total
            # Both cards are A
            else:
                ace_total.append(2)
                ace_total.append(12)
                return ace_total


# Returns new total as a list. Only use after deal
def running_total(total, new_card):
    new_total = []
    cards_of_ten = ['J', 'Q', 'K']

    # When total is a list with only 1 value (normal)
    if len(total) == 1:
        # New card is an int
        if type(new_card) == int:
            new_total.append(total[0])
            new_total[0] += new_card
            return new_total
        # New card is JQK
        elif new_card in cards_of_ten:
            new_total.append(total[0])
            new_total[0] += 10
            return new_total
        # New card is A
        else:
            new_total.append(total[0])
            new_total.append(new_total[0])
            new_total[0] += 1
            new_total[1] += 11
            return new_total
    # When total is a list with 2 values (A situations)
    else:
        new_total.append(total[0])
        new_total.append(total[1])
        # If new card is a number
        if type(new_card) == int:
            new_total[0] += new_card
            new_total[1] += new_card
            if new_total[1] > 21:
                new_total.pop(1)
            return new_total
        # If new card is JQK
        elif new_card in cards_of_ten:
            new_total[0] += 10
            new_total[1] += 10
            if new_total[1] > 21:
                new_total.pop(1)
            return new_total
        # If new card is A
        else:
            new_total[0] += 1
            new_total[1] += 11
            if new_total[1] > 21:
                new_total[1] -= 10
            return new_total


# Deals the dealer and players hands.
def deal_game():
    dealer_hand = deal_dealer()
    dealer_total = starting_total(dealer_hand)

    player_hand = deal_player()
    player_total = starting_total(player_hand)

    print()
    print('Dealer hand:', ' '.join(map(str, dealer_hand)), 'Total:', dealer_total)
    print('Player hand:', ' '.join(map(str, player_hand)), 'Total:', player_total)


# Returns player final TOTAL after choosing hit or stick, deals with logic for busts
# high numbers. Returns player hand as 0 if bust
def player_hit_or_stick(hand):
    current_hand = list((hand))

    total = starting_total(hand)

    player_choice = input('Hit or Stick: ')
    player_choice = player_choice.lower()
    has_stuck = False

    while not has_stuck:
        if player_choice.lower() == 's':
            print('Player Sticks with', total[-1])
            has_stuck = True
            return total
        elif player_choice.lower() == 'h':
            current_hand.append(take_card())
            total = running_total(total, current_hand[-1])
            print()
            print('Dealing new card...')
            print(f'You get a {current_hand[-1]}.')
            if len(total) == 1:  # If total is just 1 digit
                if total[0] > 21: # Player busts
                    print('Bust!', total, 'is too high.')
                    total = 0
                    return total
                else:
                    print('Player hand:', ' '.join(map(str, current_hand)), 'Total:', total)
                    print(f'Dealer has {dealer_total}. Hit(h), or Stick(s) with your {total}?')
                    player_choice = input('Hit or Stick: ')
            else:  # If total is 2 digits (1, 11)
                if total[-1] > 21:
                    total.pop(-1)
                    print('Player hand:', ' '.join(map(str, current_hand)), 'Total:', total)
                    print(f'Dealer has {dealer_total}. Hit(h), or Stick(s) with your {total}?')
                    player_choice = input('Hit or Stick: ')
                else:
                    print('Player hand:', ' '.join(map(str, current_hand)), 'Total:', total)
                    print(f'Dealer has {dealer_total}. Hit(h), or Stick(s) with your {total}?')
                    player_choice = input('Hit or Stick: ')

        else:
            print('You need to type "s" or "h"!')
            player_choice = input('Hit or Stick: ')

# Game starts here
while balance > 0:

    print()
    print('Welcome to Blackjack!')
    print(f'Your balance: {balance}')
    print('How much would you like to wager?')

    # Takes a wager from a user and subtracts from balance
    wager_accepted = False
    while not wager_accepted:
        wager = input('Enter here: ')

        if wager.isnumeric():
            wager = int(wager)
            if wager > balance:
                print(f'You don\'t have enough! Please bet less than your balance of {balance}.')
            else:
                print(f'Bet accepted for {wager}.')
                balance -= wager
                wager_accepted = True
        else:
            print('Please enter a valid whole number.')

    dealer_hand = deal_dealer()
    dealer_total = starting_total(dealer_hand)

    player_hand = deal_player()
    player_total = starting_total(player_hand)


    print()
    print('Dealer hand:', ' '.join(map(str, dealer_hand)), '?', 'Total:', dealer_total)
    print('Player hand:', ' '.join(map(str, player_hand)), 'Total:', player_total)
    print()

    # Checks for Blackjack -> instant win 2.5 bet if BJ.
    if player_total[-1] == 21:
        winnings = wager * 2.5
        balance += winnings
        print(f'Blackjack! You win {winnings}')
        print(f'New balance: {balance}')

    # If not Blackjack, continue with rest of the game.
    else:
        print(f'Dealer has {dealer_total}. Hit(h), or Stick(s) with your {player_total}?')

        # Runs Hit or Stick function to receive a final total.
        final_hand = player_hit_or_stick(player_hand)
        player_total = final_hand

        # If player hasn't bust and has a FINAL total
        if final_hand != 0:
            dealer_has_bust = False
            # Dealer still HAS to take cards
            while dealer_total[-1] <= 16:
                dealer_has_bust = False
                dealer_hand.append(take_card())  # Dealer takes a new card and adds to end of list
                dealer_total = running_total(dealer_total, dealer_hand[-1])  # Dealer new total
                print()
                print('Dealing card to dealer...')
                print(dealer_hand[-1])
                # When dealer total is 17 or more BUT less than or EQUAL to 21.
                if dealer_total[-1] <= 21:
                    print(f'Dealer has {dealer_total}.')
                    # Exits out of While Loop
                # Dealer has gone over 21, player must win.
                else:
                    print()
                    print(f'Bust! Dealer busts with {dealer_total[-1]}.')
                    print('Player wins!')
                    print()
                    winnings = wager * 2
                    balance += winnings
                    dealer_has_bust = True
                    print(f'Player receives {winnings}.')
                    print(f'New balance: {balance}')

            # Dealer 17 or over. HAS to stick.
            else:
                if not dealer_has_bust:
                    print(f'Dealer sticks on {dealer_total[-1]}.')

                    # If dealer sticks on same total as player
                    if player_total[-1] == dealer_total[-1]:
                        balance += wager
                        print()
                        print('Push!')
                        print(f'Dealer has {dealer_total[-1]} and player has {player_total[-1]}')
                        print(f'You receive your wager of {wager} back.')

                    # If player has higher final total than dealer
                    elif player_total[-1] > dealer_total[-1]:
                        winnings = wager * 2
                        balance += winnings
                        print(f'Player wins! {player_total[-1]} beats {dealer_total[-1]}.')
                        print(f'Player receives {winnings}.')
                        print(f'New balance: {balance}')

                    # Dealer final total higher than player final total
                    else:
                        print(f'You lost! Dealer wins with {dealer_total[-1]}.')
                        print('Better luck next time!')

        # If player has bust
        else:
            print()
            print('Dealer wins! Better luck next time!')
            print(f'Current balance: {balance}')

# Fix bug where dealer can bust by pulling an Ace at 15. 15-> 26 = bust. but 15 -> 16 should be fine

import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words)  # randomly chooses a word from words list
    while '-' in word or ' ' in word:
        word = random.choice(words)
        # iterating through words while an invalid character is in it
        # if it stops, must mean it is a word without - or " "

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has already guessed

    lives = 8

    # get user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        print('Remaining lives:', lives)
        print('You have used these letters: ', ' '.join(used_letters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        print()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives -= 1  # takes away life if incorrect guess
                print(f'{user_letter} isn\'t correct!')
                print()

        elif user_letter in used_letters:
            print('You have already guessed that letter. Try again: ')

        else:
            print('Invalid Character. Please enter a letter: ')

    if lives == 0:
        print('You\'re out of lives! They hung him! The word was', word)
    else:
        print('You win!! You saved the man!')
        print(f'It was {word}.')


hangman()

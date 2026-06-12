# Problem Set - hangman.py

import random
import string


WORDLIST_FILENAME = "words.txt"

def load_words():
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    return random.choice(wordlist)


def choose_help():
    while True:
        choice = input("Press 'y' to play with help enabled and 'n' to play without help: ").strip().lower()

        if choice == 'y':
            print("Press '!' anytime for hints.")
            return True

        if choice == 'n':
            return False

        print("Invalid choice. Please enter 'y' or 'n'.")

# ---------------------------------------------------------
#              helper functions below-
# ---------------------------------------------------------
def has_player_won(secret_word, letters_guessed):
    for i in secret_word:
        if i not in letters_guessed:
            return False
    return True


def get_word_progress(secret_word, letters_guessed):
    word_progress = ""
    for letter in secret_word:
        if letter in letters_guessed:
            word_progress += letter
        else:
            word_progress += "*"
    return word_progress

def get_available_letters(letters_guessed):
    available = string.ascii_lowercase
    for letter in letters_guessed:
        available = available.replace(letter,"")
    return available


def get_help_letter(secret_word , available_letters):
    choose_from = [ i for i in secret_word if i in available_letters]
    new = random.randint(0, len(choose_from)-1)
    revealed_letter = choose_from[new]
    return revealed_letter


def hangman(secret_word, with_help):       

    length_word = len(secret_word)
    guesses_left = 10
    letters_guessed = []
    vowels = "aeiou"
    print("Welcome to Hangman!")
    print(f"I am thinking of a word that is {length_word} letters long.")


    while(guesses_left > 0) and not has_player_won(secret_word,letters_guessed):
        print("-------------------")
        print(f"You have {guesses_left} guesses left.")
        available_letters = get_available_letters(letters_guessed)
        print("Available letters:",available_letters)
        input_letter = input("Please guess a letter: ").strip().lower()
        
        if input_letter == "":
            print("Oops! That is not a valid letter. Please input a letter from the alphabet: ",end = '')
        elif input_letter == "!" and with_help:
            if guesses_left >= 3:
                guesses_left -= 3
                revealed_letter = get_help_letter(secret_word,available_letters)
                letters_guessed.append(revealed_letter)
                print(f"Letter revealed: {revealed_letter}")
            else:
                print("Oops! Not enough guesses left:",end = '')
        elif input_letter in letters_guessed:
            print("Oops! You've already guessed that letter:")
        elif input_letter not in string.ascii_letters or len(input_letter)>1:
            print("Oops! That is not a valid letter. Please input a letter from the alphabet: ",end = '')
        elif input_letter not in secret_word:
            letters_guessed.append(input_letter)
            print("Oops! That letter is not in my word: ",end = '')
            if input_letter in vowels:
                guesses_left -=2
            else:
                guesses_left -= 1
        else:
            letters_guessed.append(input_letter)
            print("good guess: ",end = '')
            
        print(get_word_progress(secret_word,letters_guessed))

    if has_player_won(secret_word,letters_guessed):
        print("--------------\n","Congratulations, you won!")
        total_score = (guesses_left + 4*len(set(secret_word))) + (3*length_word)
        print(f"Your total score for this game is: {total_score}") 
    else:
        print(f"Sorry, you ran out of guesses. The word was {secret_word}")


if __name__ == "__main__":
    wordlist = load_words()
    secret_word = choose_word(wordlist)
    with_help = choose_help()
    hangman(secret_word, with_help)



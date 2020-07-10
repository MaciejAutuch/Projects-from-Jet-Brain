# special thanks to rorydph who posted part of this solution on JetBrains :)

import random

def valid_input(txt, guess_set):
    if txt in guess_set:
        print('You already typed this letter')
    elif len(txt) != 1:
        print('You should input a single letter')
    elif txt < 'a' or txt > 'z':
        print('It is not an ASCII lowercase letter')
    else:
        return True

def the_game():
    options = ('python', 'java', 'kotlin', 'javascript', 'tennis', 'forehand', 'backhand', 'smash', 'volley', 'serve')
    word = random.choice(options)
    mask = '-' * len(word)
    guesses = set()
    wrong = 0
    while wrong != 8:
        print('\n' + mask)
        letter = input('Input a letter: ')
        if valid_input(letter, guesses):
            if letter in word and letter not in guesses:
                guesses.add(letter)
                mask = ''.join(char if char in guesses else '-' for char in word)
            elif letter not in word:
                guesses.add(letter)
                print('No such letter in the word')
                wrong += 1
        if '-' not in mask:
            print(mask)
            print('You guessed the word!')
            print('You survived!')
            break
    if '-' in mask:
        print('You are hanged!')

def loop_game():
    while True:
        print("H A N G M A N")
        user_input = input('Type "play" to play the game, "exit" to quit:\n')
        if user_input == 'play':
            the_game()
        elif user_input == 'exit':
            quit()

loop_game()
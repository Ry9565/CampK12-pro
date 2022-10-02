import random

name = input("What is your name:")

print('Good Luck', name)

words = ['rainbow', 'computer', 'science', 'programming', 'python', 'mathamatics', 'player', 'condition', 'reverse', 'water', 'board', 'garden', 'football']

word = random.choice(words)

print('Guess the character of the word!')

guesses = ''

turns = 12

while turns > 0:
    failed = 0

    for char in word:

        if char in guesses:
            print(char)

        else:
            print("_")

            failed += 1

    if failed == 0:
        print('You win, Congarulations')

        print('The word is:',word)
        break

    guess = input("guess the character:")

    guesses += guess

    if guess not in word:

        turns -=1
        
        print('Wrong')

        print('You have', + turns,' more gusses')

        if turns == 0:
            print('You lost better luck next time!')
            print('The word is:',word)
# Coreen Yuen
# fun little guessing game program

from random import *

# global constant
RANGE = 100

#introduction
def intro():
    print('It is time to play')
    print('A fun, simple guessing game')
    print('Now...guess the number!')

# plays one game with user, asks if want to play again
def again():
    counter = 0
    gameNum = 0
    minimum = 10000
    answer = 'y'
    while(answer.upper() == 'Y'):
        guesses = game()
        response = input('Do you want to play again? ')
        answer = response[0]

        counter += guesses
        gameNum += 1

        if(guesses < minimum):
            minimum = guesses

    if(answer.upper() == 'N'):
        report(gameNum, counter, minimum)

# guessing game user plays
def game():
    guesses = 1
    number = randint(1, RANGE)
    print(number)
    print()
    print("I'm thinking of a number between 1 and ", RANGE, "...")
    guess = int(input('Your guess? '))

    if(guess == number):
        print('You got it right in 1 guess')
    else:   # user guesses more than once to get correct
        while(guess != number):
            if(guess > number):
                print("It's lower.")
            else:   # guess < number
                print("It's higher.")
            guess = int(input('Your guess? '))
            guesses += 1
        print('You got it right in ', guesses, 'guesses')

    return guesses

# reports results of guessing game to user
def report(gameNum, counter, minimum):
    print()
    print('Overall results:')
    print('    total games   = ', gameNum)
    print('    total guesses = ', counter)
    average = float(10 * (counter / gameNum) / 10.0)
    print('    guesses/game  = ', average)
    print('    best game     = ', minimum)

# main
intro()
again()

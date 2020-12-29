# This is a guess the number game
import random

print ('Hello! What is your name?')
name = input()

print('Well, ' + name + ', I am thinking of a number between 1 and 10')
secretNumber = random.randint(1, 10)

for guessTaken in range (1, 7):
    try:
        print('Take a guess.')
        guess = int(input())

        if guess < secretNumber:
            print('Your guess is too low.')
        elif guess > secretNumber:
            print('Your number is too high.')
        else:
            break # This condition is for the correct guess!
    except ValueError:
        print('You did not enter a number.')
        
if guess == secretNumber:
    print('Good job ' + name + '! You guessed my number in ' + str(guessTaken) + ' guesses.')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))

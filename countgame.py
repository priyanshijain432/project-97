import random
print('Number Guessing Game')
number = random.randint(1,9)
print('Guess a number between 1 to 9')
chances=0
while chances<5:
    guess = int(input('Enter your guesses'))
    if guess == number:
        print('Congrats You Win')
        break
    elif guess<number :
        print('your guess was too low, guess a number higher than',guess)
    else :
        print('your guess was too high, guess a number lower than',guess)
    chances= chances+1
if not chances<5:
    print('You Lose')
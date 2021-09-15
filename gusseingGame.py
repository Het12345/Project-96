import random
number=random.randint(1,9)
chances=0>5
while chances < 5:
    guess=int(input('enter the number'))
    if number==guess:
        print('YUPPE You Won')
        break
    elif number < guess:
        print('guess is smaller number')
    else:
        print('Guess a larger number')
    chances=chances+1
if chances>=5:
    print('oops you lose.The answer is ', number)
import random

secret_number = random.randrange(1, 100)

while True:
    guess = int(input('Guess a number between 1 and 100: '))

    if guess == secret_number:
        print('Well done, you got it. You donkey!')
        break

    if guess < secret_number:
        print('Too low!')
    else:
        guess > secret_number
        print('Too high!')




# this is a guess game

import random

secret_Number = random.randint(0, 21)

# think a number in between 20

print('Think a number it could be !!')

# ask the player to guess for 5 times

for guessesTaken in range(1, 6):
    print('Take a guess!!')
    guess = int(input('My guess is : '))

    if guess < secret_Number:
        print('Your guess is too low.')
    elif guess > secret_Number:
        print('Your guess is too high.')
    else:
        break

if guess == secret_Number:
    print('Good job! You guessed my number just in ' + str(guessesTaken) + ' guess!')
else:
    print('Nope. The number I was thinking of was : ' + str(secret_Number))
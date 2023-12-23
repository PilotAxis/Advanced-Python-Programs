import random
secretnum = random.randint(1, 100)
guessNum = int(input("Guess a number between 1 and 100 inclusive :"))
while guessNum != secretnum:
    if guessNum < secretnum:
        print('Your guess is too low!')
    else:
        print('Your guess is too high!')
    guessNum = int(input("Guess a number between 1 and 100 inclusive:"))
print("Congratulations! You guessed the number correctly!")
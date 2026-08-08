# Guessing Game
import random
jackpot = random.randint(1,100)
guess = int(input("Guess the number between 1 and 100: "))
counter = 1

while guess != jackpot:
    if guess < jackpot:
        print("guess higher")
    else:
        print("guess lower")

    guess = int(input("Guess the number between 1 and 100: "))
    counter += 1

print("Congratulations! You guessed the correct number:", jackpot)
print("It took you", counter, "guesses.")
import random
realNum = random.randint(0,10)
guess = 11
while guess != realNum:
    guess = int(input("Guess a number between 0 and 10: "))
    if guess < realNum:
        print("Too low.")
    elif guess > realNum:
        print("Too high.")
print("You win!")

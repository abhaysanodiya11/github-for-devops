import random

number = random.randint(1, 100)
tries = 0

print("I'm thinking of a number between 1 and 100.")

while True:
    try:
        guess = int(input("Your guess: "))
    except ValueError:
        print("Please enter a number!")
        continue

    tries += 1

    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print(f"You got it in {tries} tries!")
        break
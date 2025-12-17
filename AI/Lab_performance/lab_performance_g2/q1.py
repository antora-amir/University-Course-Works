import random

secret_number = random.randint(1, 20)
attempts = 0

while True:
    user_input = input("Guess a number between 1 and 20 (0 to exit): ")

    if not user_input.isdigit():
        print("Please enter a valid number.")
        continue

    guess = int(user_input)

    if guess == 0:
        print("Game exited.")
        break

    attempts += 1

    if guess > secret_number:
        print("Too high")
    elif guess < secret_number:
        print("Too low")
    else:
        print("Correct!")
        print("Number of attempts:", attempts)
        break

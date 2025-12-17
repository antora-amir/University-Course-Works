# Lab Performance G2

## Overview
This lab contains two Python programs: a number guessing game and a program that separates even and odd numbers.

## Question 1: Number Guessing Game
A game where the computer generates a random number between 1 and 20, and the user tries to guess it.

### How it Works
1. Computer generates random number
2. User inputs guesses
3. Program gives hints: "Too high" or "Too low"
4. Counts attempts until correct guess
5. User can exit by entering 0

### Source Code (q1.py)
```python
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
```

### Sample Input/Output
**Input:**
```
10
15
12
```

**Output:**
```
Too low
Too high
Correct!
Number of attempts: 3
```

## Question 2: Even Odd Separator
A program that takes a tuple of numbers and separates them into even and odd lists.

### How it Works
1. Defines a tuple of numbers 1-10
2. Iterates through each number
3. Checks if even or odd using modulo operator
4. Appends to respective lists
5. Prints the lists and total count

### Source Code (q2.py)
```python
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

even_numbers = []
odd_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
print("Total count:", len(numbers))
```

### Sample Output
```
Even numbers: [2, 4, 6, 8, 10]
Odd numbers: [1, 3, 5, 7, 9]
Total count: 10
```

### Requirements
- Python 3.x

### How to Run
1. For q1.py: `python q1.py`
2. For q2.py: `python q2.py`

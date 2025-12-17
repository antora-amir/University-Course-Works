# Lab Performance C2

## Overview
This lab contains two Python programs: one for generating multiplication tables and another demonstrating a simple bank account system using classes.

## Question 1: Multiplication Table Generator
A program that takes a number from the user and prints its multiplication table from 1 to 10.

### How it Works
1. Prompts user for a number
2. Uses a loop to calculate and print multiplication from 1 to 10

### Source Code (q1.py)
```python
num = int(input("Enter a number: "))

print(f"Multiplication Table of {num}:")

for i in range(1, 11):
    print(num, "x", i, "=", num * i)
```

### Sample Input/Output
**Input:**
```
5
```

**Output:**
```
Multiplication Table of 5:
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
```

## Question 2: Bank Account System
A program that simulates basic bank account operations using a class.

### Classes
- **BankAccount**: Manages balance with deposit, withdraw, and show_balance methods.

### Source Code

**bank_account.py**
```python
class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    def show_balance(self):
        print("Current Balance:", self.balance)
```

**main.py**
```python
from bank_account import BankAccount

account = BankAccount()

account.deposit(1000)
account.show_balance()

account.withdraw(500)
account.show_balance()

account.withdraw(700)
```

### Sample Output
```
Deposited: 1000
Current Balance: 1000
Withdrawn: 500
Current Balance: 500
Insufficient balance
```

### Requirements
- Python 3.x

### How to Run
1. For q1.py: `python q1.py`
2. For q2: Navigate to q2/ directory, run `python main.py`

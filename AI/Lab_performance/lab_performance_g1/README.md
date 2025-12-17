# Lab Performance G1

## Overview
This lab contains two Python programs: one for word frequency analysis and another demonstrating inheritance with Person and Employee classes.

## Question 1: Word Frequency Counter
A program that takes a sentence from the user and counts the frequency of each word.

### How it Works
1. Prompts user for a sentence
2. Splits into words and converts to lowercase
3. Uses a dictionary to count occurrences
4. Prints each word and its count

### Source Code (q1.py)
```python
sentence = input("Enter a sentence: ")

words = sentence.split()
word_count = {}

for word in words:
    word = word.lower()         
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Word Frequency:")
for word, count in word_count.items():
    print(word, ":", count)
```

### Sample Input/Output
**Input:**
```
hello world hello python world
```

**Output:**
```
Word Frequency:
hello : 2
world : 2
python : 1
```

## Question 2: Employee Management System
A program demonstrating inheritance where Employee class inherits from Person class.

### Classes
- **Person**: Base class with name and age
- **Employee**: Derived class with additional salary attribute

### Source Code

**person.py**
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_person_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
```

**employee.py**
```python
from person import Person

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def show_details(self):
        self.show_person_details()
        print("Salary:", self.salary)
```

**main.py**
```python
from employee import Employee

emp = Employee("Ahmad", 22, 35000)
emp.show_details()
```

### Sample Output
```
Name: Ahmad
Age: 22
Salary: 35000
```

### Requirements
- Python 3.x

### How to Run
1. For q1.py: `python q1.py`
2. For q2: Navigate to q2/ directory, run `python main.py`

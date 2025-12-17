# Lab Performance C1

## Overview
This lab contains two Python programs demonstrating basic programming concepts including user input handling, list operations, and object-oriented programming with classes.

## Question 1: Integer Analyzer
A program that takes a list of integers from user input, finds the largest and smallest numbers, and calculates their difference.

### How it Works
1. Prompts user to enter integers separated by spaces
2. Splits the input string and converts to integers
3. Uses built-in `max()` and `min()` functions to find extremes
4. Calculates difference between largest and smallest

### Source Code (q1.py)
```python
userInput = input("Enter integers separeted by spaces: ")

values = userInput.split()

numbers = list(map(int,values))

largest_number = max(numbers)
smallest_number = min(numbers)

difference = largest_number-smallest_number

print("Largest number: ", largest_number)
print("Smallest number: ", smallest_number)
print("Difference: ",difference)
```

### Sample Input/Output
**Input:**
```
3 6 5 4 8 9
```

**Output:**
```
Largest number:  9
Smallest number:  3
Difference:  6
```

## Question 2: Student Management System
A program that demonstrates class creation and usage by managing student information with marks and calculations.

### Classes
- **Student**: A class with name, marks1, marks2, and methods to calculate total and average marks.

### Source Code

**student_class.py**
```python
class Student:
    def __init__(self, name, marks1, marks2):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2

    def total(self):
        return self.marks1 + self.marks2

    def average(self):
        return self.total() / 2
```

**main.py**
```python
from student_class import Student  

students = []

for i in range(3):
    print(f"\nEnter details for Student {i+1}")
    name = input("Name: ")
    marks1 = int(input("Marks 1: "))
    marks2 = int(input("Marks 2: "))
    
    s = Student(name, marks1, marks2)
    students.append(s)

print("\nStudent Results:")
for s in students:
    print("Name:", s.name)
    print("Total Marks:", s.total())
    print("Average Marks:", s.average())
    print("----------------------")
```

### Sample Output
```
Enter details for Student 1
Name: Alice
Marks 1: 85
Marks 2: 90

Enter details for Student 2
Name: Bob
Marks 1: 78
Marks 2: 82

Enter details for Student 3
Name: Charlie
Marks 1: 92
Marks 2: 88

Student Results:
Name: Alice
Total Marks: 175
Average Marks: 87.5
----------------------
Name: Bob
Total Marks: 160
Average Marks: 80.0
----------------------
Name: Charlie
Total Marks: 180
Average Marks: 90.0
----------------------
```

### Requirements
- Python 3.x

### How to Run
1. For q1.py: `python q1.py`
2. For q2: Navigate to q2/ directory, run `python main.py`

# Lab Performance H1

## Overview
This lab contains two Python programs: one for counting vowels and consonants in a string, and another for grading students based on scores.

## Question 1: Vowel and Consonant Counter
A program that takes a string input and counts the number of vowels and consonants.

### How it Works
1. Defines vowels as "aeiou"
2. Iterates through each character in the input
3. Checks if alphabetic, then if vowel or consonant
4. Returns counts

### Source Code (q1.py)
```python
def count_vowels_consonants(text):
    vowels_count = 0
    consonants_count = 0
    
    
    vowels = "aeiou"
    
    for char in text:
        if char.isalpha():  
            if char.lower() in vowels:
                vowels_count += 1
            else:
                consonants_count += 1
                
    return vowels_count, consonants_count


user_input = input("Enter a string: ")
v, c = count_vowels_consonants(user_input)

print("-" * 20)
print(f"Vowels: {v}")
print(f"Consonants: {c}")
```

### Sample Input/Output
**Input:**
```
Hello World
```

**Output:**
```
--------------------
Vowels: 3
Consonants: 7
```

## Question 2: Student Grading System
A program that takes details for 10 students and assigns letter grades based on scores.

### How it Works
1. Defines grade function: A (>=80), B (>=70), C (>=60), F (<60)
2. Loops 10 times for student input
3. Stores name and grade in dictionary
4. Prints the dictionary

### Source Code (q2.py)
```python
def find_grade(score):
    """Returns a letter grade based on the score."""
    if score >= 80:
        return 'A'
    elif score >= 70:
        return 'B'
    elif score >= 60:
        return 'C'
    else:
        return 'F'


student_grades = {}

print("--- Enter details for 10 students ---")


for i in range(10):
    print(f"\nStudent {i+1}:")
    name = input("Enter Name: ")
    score = int(input("Enter Score: "))
    
    
    grade = find_grade(score)
    student_grades[name] = grade

print("\n--- Final Grade Dictionary ---")
print(student_grades)
```

### Sample Output
```
--- Enter details for 10 students ---

Student 1:
Enter Name: Alice
Enter Score: 85

... (for 10 students)

--- Final Grade Dictionary ---
{'Alice': 'A', 'Bob': 'B', ...}
```

### Requirements
- Python 3.x

### How to Run
1. For q1.py: `python q1.py`
2. For q2.py: `python q2.py`

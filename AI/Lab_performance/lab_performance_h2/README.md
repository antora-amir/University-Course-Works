# Lab Performance H2

## Overview
This lab contains two Python programs: one for matrix operations and another for safe division with exception handling.

## Question 1: Matrix Sum Calculator
A program that creates a 3x3 matrix from user input and calculates the sum of each row and column.

### How it Works
1. Prompts user for 9 elements to fill 3x3 matrix
2. Prints the matrix
3. Calculates sum of each row using sum()
4. Calculates sum of each column by iterating

### Source Code (q1.py)
```python
matrix = []

print("--- Enter the elements for the 3x3 matrix ---")

for i in range(3):
    row = []
    for j in range(3):
        
        val = int(input(f"Enter element for position [{i}][{j}]: "))
        row.append(val)
    matrix.append(row)

print("\n--- The Matrix ---")
for row in matrix:
    print(row)

print("\n--- Results ---")

for i in range(3):
    
    row_sum = sum(matrix[i]) 
    print(f"Sum of Row {i+1}: {row_sum}")

for j in range(3):
    col_sum = 0
    for i in range(3):
        
        col_sum += matrix[i][j]
    print(f"Sum of Column {j+1}: {col_sum}")
```

### Sample Input/Output
**Input:**
```
1 2 3
4 5 6
7 8 9
```

**Output:**
```
--- The Matrix ---
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]

--- Results ---
Sum of Row 1: 6
Sum of Row 2: 15
Sum of Row 3: 24
Sum of Column 1: 12
Sum of Column 2: 15
Sum of Column 3: 18
```

## Question 2: Safe Division Calculator
A program that performs division with proper exception handling for division by zero and invalid inputs.

### How it Works
1. Prompts for numerator and denominator
2. Attempts division
3. Catches ZeroDivisionError and ValueError
4. Always prints completion message

### Source Code (q2.py)
```python
print("--- Division Calculator ---")

try:
    
    num1 = float(input("Enter the numerator: "))
    num2 = float(input("Enter the denominator: "))

   
    result = num1 / num2

    
    print(f"Result: {result}")

except ZeroDivisionError:
   
    print("Error: You cannot divide a number by zero.")

except ValueError:
    
    print("Error: Please enter valid numbers only.")

finally:
    print("--- Execution Complete ---")
```

### Sample Input/Output
**Input:**
```
10
2
```

**Output:**
```
Result: 5.0
--- Execution Complete ---
```

**Error Case:**
```
10
0
```

**Output:**
```
Error: You cannot divide a number by zero.
--- Execution Complete ---
```

### Requirements
- Python 3.x

### How to Run
1. For q1.py: `python q1.py`
2. For q2.py: `python q2.py`

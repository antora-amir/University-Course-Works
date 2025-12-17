# Integer Analyzer (Python)

## 📌 Overview

This simple Python program takes a list of integers from the user, then:

* Finds the **largest number**
* Finds the **smallest number**
* Calculates the **difference** between them

It is designed to be **easy to understand**, beginner-friendly, and runs directly from the terminal.

---

## 🛠️ How the Program Works

1. The user enters integers separated by spaces.
2. The input string is split into individual values.
3. Each value is converted into an integer.
4. The program calculates:

   * Maximum value
   * Minimum value
   * Difference (max − min)
5. The results are displayed in a clean format.

---

## 📄 Source Code

```python
userInput = input("Enter integers separeted by spaces: ")

values = userInput.split()

numbers = list(map(int, values))

largest_number = max(numbers)
smallest_number = min(numbers)

difference = largest_number - smallest_number

print("Largest number: ", largest_number)
print("Smallest number: ", smallest_number)
print("Difference: ", difference)
```

---

## ▶️ Sample Input

```
3 6 5 4 8 9
```

## 📤 Sample Output

```
Largest number:  9
Smallest number:  3
Difference:  6
```

---

## ✅ Requirements

* Python 3.x

---

## 🚀 How to Run

1. Save the code in a file (e.g., `q1.py`)
2. Open a terminal or command prompt
3. Run the file using:

   ```bash
   python q1.py
   ```
4. Enter integers separated by spaces when prompted

---

## 🎯 Learning Outcome

* Taking user input
* Working with lists
* Using built-in functions (`max()`, `min()`, `map()`)
* Basic arithmetic operations

---

**Author:** Syeda Farzan Amir Antora

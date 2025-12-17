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


userInput = input("Enter integers separeted by spaces: ")

values = userInput.split()

numbers = list(map(int,values))

largest_number = max(numbers)
smallest_number = min(numbers)

difference = largest_number-smallest_number

print("Largest number: ", largest_number)
print("Smallest number: ", smallest_number)
print("Difference: ",difference)



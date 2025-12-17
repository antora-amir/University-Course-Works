
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
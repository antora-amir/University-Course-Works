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
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

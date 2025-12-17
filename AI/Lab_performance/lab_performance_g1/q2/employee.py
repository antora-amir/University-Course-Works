from person import Person

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def show_details(self):
        self.show_person_details()
        print("Salary:", self.salary)

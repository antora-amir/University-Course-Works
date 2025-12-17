class Student:
    def __init__(self, name, marks1, marks2):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2

    def total(self):
        return self.marks1 + self.marks2

    def average(self):
        return self.total() / 2

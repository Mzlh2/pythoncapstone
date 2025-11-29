class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)

# Derived Class 1
class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)  # calling Person constructor
        self.course = course

    def display_student(self):
        print("Course:", self.course)

# Derived Class 2 (from Student)
class Exam(Student):
    def __init__(self, name, age, course, m1, m2, m3):
        super().__init__(name, age, course)  # calling Student constructor
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.total = m1 + m2 + m3

    def display_exam(self):
        print("Marks:", self.m1, self.m2, self.m3)
        print("Total Marks:", self.total)

e1 = Exam("Shruti", 20, "BCA", 85, 90, 88)

print("\nStudent Details")
e1.display_person()
e1.display_student()
e1.display_exam()

class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

    def __repr__(self):
        return f"Student(name='{self.name}', roll_number='{self.roll_number}', cgpa={self.cgpa})"


def sort_students(students):
    students.sort(key=lambda x: x.cgpa, reverse=True)


# Test the function
students_list = [
    Student("Alice", "A001", 3.8),
    Student("Bob", "B002", 3.5),
    Student("Charlie", "C003", 3.9),
]

print("Before sorting:")
for student in students_list:
    print(student)

sort_students(students_list)

print("\nAfter sorting by CGPA (descending order):")
for student in students_list:
    print(student)
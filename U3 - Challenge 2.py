class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students

# Test the sort_students function
students_list = [
    Student("Alice", "A001", 9.5),
    Student("Bob", "B002", 7.2),
    Student("Charlie", "C003", 4.8),
    Student("David", "D004", 4.6)
]

sorted_students = sort_students(students_list)

print("Sorted Students based on CGPA:")
for student in sorted_students:
    print(f"{student.name} - {student.roll_number} - CGPA: {student.cgpa}")

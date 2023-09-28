class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students
if __name__ == "__main__":
    students = [
        Student("Gowtham", "A123", 3.9),
        Student("Anisha", "B456", 3.7),
        Student("Chinnu", "C789", 4.0),
        Student("Rathish", "D987", 3.5),
    ]
    sorted_students = sort_students(students)
    print("Sorted Students by CGPA (descending order):")
    for student in sorted_students:
        print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")

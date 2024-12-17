# print_all_students.py

from student import students

def print_all_students():
    """
    Prints details of all students.
    """
    if not students:
        print("No students found.")
    else:
        print("List of all students:")
        for student in students:
            print(student)

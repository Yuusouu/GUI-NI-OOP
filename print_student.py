

from student import students

def print_student(student_id):
    """
    Prints details of a specific student by ID.
    """
    for student in students:
        if student.student_id == student_id:
            print("Student found:")
            print(student)
            return student
    print(f"No student found with ID: {student_id}")

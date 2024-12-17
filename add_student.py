from student import Student, students

def add_student(name, age, student_id, email, phonenum):
    """
    Adds a new student to the students list with ID, name, email, and phone number.
    """
    new_student = Student(name, age, student_id, email, phonenum)
    students.append(new_student)
    print(f"Student {name} (ID: {student_id}) added successfully.")

    try:
        with open('studnetlsit.txt', 'a+') as file:
            file.write(f"{new_student.name}, {new_student.age}, {new_student.student_id}, {new_student.email}, {new_student.phonenum}\n")
    except Exception as e:
        print(f"Error: Failed to save data to file. {e}")


def add_student_from_database():
        try:
            with open("studnetlsit.txt", 'r') as file:
                lines = file.readlines()
                print(lines)
                if len(lines) == 0:
                    print('Warning: No student data found in database.')
                for line in lines:
                    name, age, student_id, email, phonenum = line.strip().split(', ')
                    new_student = Student(name, age, student_id, email, phonenum)
                    students.append(new_student)
                    print(f"Student {name} (ID: {student_id}) added successfully.")
        except FileNotFoundError:
            print('Error: File does not exitst.')
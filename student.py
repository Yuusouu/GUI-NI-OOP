# student.py

class Student:
    def __init__(self, name, age, student_id, email, phonenum):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.email = email
        self.phonenum = phonenum


    def __str__(self):
        return (
            f"Name: {self.name}, Age: {self.age}, "
            f"StudentID: {self.student_id}, email: {self.email}, Contacts: {self.phonenum}"
        )


# Shared student list to store all students
students = []

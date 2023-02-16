from User import User
from Student import Student
from Faculty import Faculty
from Models import DB
from Exceptions import *

import time

class StudentController():
    def __init__(self):
        self.__student = Student(None, None, None, None, None)
        self.__db = DB()

    @property
    def student(self):
        return self.__student

    @student.setter
    def student(self, student):
        self.__student = student

    def login(self):
        try:
            print("-"*45)
            print("Welcome to the Student Login Portal")
            print("-"*45)
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            user = self.__db.get_user(username, password)
            if user != None:
                student = self.__db.get_student_by_user_id(user.userID)
                if student != None:
                    self.student = student
                    self.student.username = user.username
                    self.student.password = user.password
                    self.student.userID = user.userID
                    return True
                else:
                    print("Invalid credentials")
                    time.sleep(1)
                    return False

            else:
                print("Invalid credentials")
                return False
        except Exception as e:
            print(e)
            return False

    def register(self):
        try:
            print("-"*45)
            print("Welcome to the Student Registration Portal")
            print("-"*45)
            username = input("Enter your username: ")
            print("Checking if username is available...")

            time.sleep(1)

            if self.__db.if_username_available(username):
                password = input("Enter your password: ")
                self.__student.username = username
                self.__student.password = password
                self.__student.semester = input("Enter your semester: ")
                self.__student.cgpa = input("Enter your cgpa: ")
                self.__student.major = input("Enter your major: ")

                if self.student.username == "" or self.student.password == "" or self.student.semester == "" or self.student.cgpa == "" or self.student.major == "":
                    print("Invalid input, please try again")
                    self.register()
                else:
                    id = self.__db.register_user(
                        self.student.username, self.student.password)
                    if id != -1:
                        self.student.userID = id
                        self.__db.register_student(
                            self.student.semester, self.student.cgpa, self.student.major, self.student.userID)
                        print("Registration successful")
                        time.sleep(1)
                        return True
                    else:
                        print("Registration failed")
                        time.sleep(1)
                        return False
            else:
                print("\nUsername not available\n")
                self.register()
        except Exception as e:
            print(e)
            return False

    def view_profile(self):
        print("-"*45)
        print(f"{self.student.username}'s Profile")
        print("-"*45)
        print("Password: ".ljust(20), self.student.password)
        print("Semester: ".ljust(20) + self.student.semester)
        print("CGPA: ".ljust(20) + self.student.cgpa)
        print("Major: ".ljust(20) + self.student.major)
        print("-"*45)

    def edit_profile(self):
        print("-"*45)
        print(f"Editing {self.student.username}'s Profile")
        print("-"*45)
        print("Enter 0 to skip")
        semester = input("Enter your semester: ")
        if semester != "0":
            self.student.semester = semester
        cgpa = input("Enter your cgpa: ")
        if cgpa != "0":
            self.student.cgpa = cgpa
        major = input("Enter your major: ")
        if major != "0":
            self.student.major = major

        self.__db.update_student(self.student)

    def delete_profile(self):
        print("-"*45)
        print(f"Deleting {self.student.username}'s Profile")
        print("-"*45)
        self.__db.delete_user(self.student.userID)
        print("Profile deleted successfully")
        self.student = Student(None, None, None, None, None)

class FacultyController():
    def __init__(self):
        self.__faculty = Faculty(None, None, None, None)
        self.__db = DB()

    @property
    def faculty(self):
        return self.__faculty

    @faculty.setter
    def faculty(self, faculty):
        self.__faculty = faculty

    def login(self):
        try:
            print("-"*45)
            print("Welcome to the Faculty Login Portal")
            print("-"*45)
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            user = self.__db.get_user(username, password)
            if user != None:
                self.faculty = self.__db.get_faculty_by_user_id(user.userID)
                self.faculty.username = user.username
                self.faculty.password = user.password
                self.faculty.userID = user.userID
                return True
            else:
                print("Invalid credentials")
                return False
        except Exception as e:
            print(e)
            return False

    def register(self):
        try:
            print("-"*45)
            print("Welcome to the Faculty Registration Portal")
            print("-"*45)
            username = input("Enter your username: ")
            print("Checking if username is available...")

            time.sleep(2)

            if self.__db.if_username_available(username):
                password = input("Enter your password: ")
                self.__faculty.username = username
                self.__faculty.password = password
                self.__faculty.subjectTeaching = input("Enter subject you teach: ")
                self.__faculty.designation = input("Enter your designation: ")

                if self.faculty.username == "" or self.faculty.password == "" or self.faculty.subjectTeaching == "" or self.faculty.designation == "":
                    print("Invalid input, please try again")
                    self.register()
                else:
                    id = self.__db.register_user(
                        self.faculty.username, self.faculty.password)
                    if id != -1:
                        self.faculty.userID = id
                        self.__db.register_faculty(
                            self.faculty.subjectTeaching, self.faculty.designation, self.faculty.userID)
                        print("Registration successful")
                        return True
                    else:
                        print("Registration failed")
                        self.__db.delete_user(self.faculty.userID)
                        return False
            else:
                print("\nUsername not available\n")
                self.register()
        except Exception as e:
            print(e)
            return False

    def view_profile(self):
        print("-"*45)
        print(f"{self.faculty.username}'s Profile")
        print("-"*45)
        print("Password: ".ljust(20), self.faculty.password)
        print("Subject Taught: ".ljust(20) + self.faculty.subjectTeaching)
        print("Designation: ".ljust(20) + self.faculty.designation)
        print("-"*45)

    def edit_profile(self):
        print("-"*45)
        print(f"Editing {self.faculty.username}'s Profile")
        print("-"*45)
        print("Enter 0 to skip")
        newPass = input("Enter new password: ")
        if newPass != "0":
            self.faculty.password = newPass
        subject = input("Enter your subject to teach: ")
        if subject != "0":
            self.faculty.subjectTeaching = subject
        designation = input("Enter your designation: ")
        if designation != "0":
            self.faculty.designation = designation

        self.__db.update_faculty(self.faculty)

    def delete_profile(self):
        print("-"*45)
        print(f"Deleting {self.faculty.username}'s Profile")
        print("-"*45)
        self.__db.delete_user(self.faculty.userID)
        print("Profile deleted successfully")
        self.faculty = Faculty(None, None, None, None)
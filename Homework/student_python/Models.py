from User import User
from Faculty import Faculty
from Student import Student
from Exceptions import *

import pymysql


class DB:
    def __init__(self):
        self.connection = pymysql.connect(host='localhost', user='root', password='kamran', db='hwsef20')

    def register_user(self, username, password):
        '''
            @param username: username of the user
            @param password: password of the user
            @return: user_id of the user
            @return: -1 if user already exists
        '''
        try:
            with self.connection.cursor() as cursor:
                sql = "INSERT INTO `users` (`username`, `password`) VALUES (%s, %s)"
                cursor.execute(sql, (username, password))
                self.connection.commit()
                return cursor.lastrowid
        except Exception as e:
            UserAlreadyExistsException("User already exists :/ <exception in DB.register_user>")
            return -1

    def register_faculty(self, subjectTeaching, designation, user_id):
        '''
            @param subjectTeaching: subjectTeaching of the faculty
            @param designation: designation of the faculty
            @param user_id: user_id of the faculty
            @return: faculty_id of the faculty
            @return: -1 if faculty already exists
        '''
        try:
            with self.connection.cursor() as cursor:
                sql = "INSERT INTO `faculty` (`subject`, `designation`, `user_id`) VALUES (%s, %s, %s)"
                cursor.execute(sql, (subjectTeaching, designation, user_id))
                self.connection.commit()
                return cursor.lastrowid
        except Exception as e:
            DBException("<exception in DB.register_faculty>")
            return -1

    def register_student(self, semester, cgpa, major, user_id):
        '''
            @param semester: semester of the student
            @param cgpa: cgpa of the student
            @param major: major of the student
            @param user_id: user_id of the student
            @return: student_id of the student
            @return: -1 if student already exists
        '''
        try:
            with self.connection.cursor() as cursor:
                sql = "INSERT INTO `students` (`semester`, `cgpa`, `major`, `user_id`) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, (semester, cgpa, major, user_id))
                self.connection.commit()
                return cursor.lastrowid
        except Exception as e:
            DBException("<exception in DB.register_student>")
            return -1
            
    def get_user(self, username, password):
        '''
            @param username: username of the user
            @param password: password of the user
            @return: user object
            @return: None if user not found
        '''
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM `users` WHERE `username`=%s AND `password`=%s"
                cursor.execute(sql, (username, password))
                result = cursor.fetchone()
                if result is None:
                    UserNotFoundException("User not found :/ <exception in DB.get_user>")
                    return None
                user = User(result[1], result[2])
                user.userID = result[0]
                return user
        except Exception as e:
            DBException("<exception in DB.get_user>")
            return None

        
    def get_faculty(self, username, password):
        '''
            @param username: username of the faculty
            @param password: password of the faculty
            @return: faculty object
            @return: None if faculty not found
        '''
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM `users` WHERE `username`=%s AND `password`=%s"
                cursor.execute(sql, (username, password))
                result = cursor.fetchone()
                if result is None:
                    UserNotFoundException("User not found :/ <exception in DB.get_faculty>")
                    return None
                else:
                    user = User(result[1], result[2])
                    user.userID = result[0]

                    sql = "SELECT * FROM `faculty` WHERE `user_id`=%s"
                    cursor.execute(sql, (user.userID))
                    result = cursor.fetchone()
                    if result is None:
                        UserNotFoundException("User not found :/ <exception in DB.get_faculty>")
                        return None
                    else:
                        faculty = Faculty(username, password, result[1], result[2])
                        faculty.facultyID = result[0]
                        return faculty
        except Exception as e:
            DBException("<exception in DB.get_faculty>")
            return None

    def get_student(self, username, password):
        '''
            @param username: username of the student
            @param password: password of the student
            @return: student object
            @return: None if student not found
        '''
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM `users` WHERE `username`=%s AND `password`=%s"
                cursor.execute(sql, (username, password))
                result = cursor.fetchone()
                if result is None:
                    UserNotFoundException("User not found :/ <exception in DB.get_student>")
                    return None
                else:
                    user = User(result[1], result[2])
                    user.userID = result[0]

                    sql = "SELECT * FROM `students` WHERE `user_id`=%s"
                    cursor.execute(sql, (user.userID))
                    result = cursor.fetchone()
                    if result is None:
                        UserNotFoundException("User not found :/ <exception in DB.get_student>")
                        return None
                    else:
                        student = Student(username, password, result[1], result[2], result[3])
                        student.studentID = result[0]
                        return student
        except Exception as e:
            DBException("<exception in DB.get_student>")
            return None

    def get_faculty_by_user_id(self, user_id):
        '''
            @param user_id: user_id of the faculty
            @return: faculty object
            @return: None if faculty not found
        '''
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM `faculty` WHERE `user_id`=%s"
                cursor.execute(sql, (user_id))
                result = cursor.fetchone()
                if result is None:
                    UserNotFoundException("User not found :/ <exception in DB.get_faculty_by_user_id>")
                    return None
                else:
                    faculty = Faculty("", "", result[1], result[2])
                    faculty.facultyID = result[0]
                    return faculty
        except Exception as e:
            DBException("<exception in DB.get_faculty_by_user_id>")
            return None

    def get_student_by_user_id(self, user_id):
        '''
            @param user_id: user_id of the student
            @return: student object
            @return: None if student not found
        '''
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM `students` WHERE `user_id`=%s"
                cursor.execute(sql, (user_id))
                result = cursor.fetchone()
                if result is None:
                    UserNotFoundException("User not found :/ <exception in DB.get_student_by_user_id>")
                    return None
                else:
                    student = Student("", "", result[1], result[2], result[3])
                    student.studentID = result[0]
                    return student
        except Exception as e:
            DBException("<exception in DB.get_student_by_user_id>")
            return None

    def update_faculty(self, faculty):
        '''
            @param faculty: faculty object
            @return: True if faculty updated successfully
            @return: False if faculty not updated
        '''
        try:
            with self.connection.cursor() as cursor:
                sql = "UPDATE `users` SET `password`=%s WHERE `username`=%s"
                cursor.execute(sql, (faculty.password, faculty.username))
                self.connection.commit()

                user = self.get_user(faculty.username, faculty.password)
                if user is None:
                    UserNotFoundException("User not found :/ <exception in DB.update_faculty>")
                    return None
                else:
                    sql = "UPDATE `faculty` SET `subject`=%s, `designation`=%s WHERE `user_id`=%s"
                    cursor.execute(sql, (faculty.subjectTeaching, faculty.designation, user.userID))
                    self.connection.commit()
                    return True
        except Exception as e:
            DBException("<exception in DB.update_faculty>")
            return False


    def update_student(self, student):
        '''
            @param student: student object
            @return: True if student updated successfully
            @return: False if student not updated
        '''
        try:
            with self.connection.cursor() as cursor:
                sql = "UPDATE `users` SET `password`=%s WHERE `username`=%s"
                cursor.execute(sql, (student.password, student.username))
                self.connection.commit()

                user = self.get_user(student.username, student.password)
                if user is None:
                    UserNotFoundException("User not found :/ <exception in DB.update_student>")
                    return None
                else:
                    sql = "UPDATE `students` SET `semester`=%s, `cgpa`=%s, `major`=%s WHERE `user_id`=%s"
                    cursor.execute(sql, (student.semester, student.cgpa, student.major, user.userID))
                    self.connection.commit()
                    return True
        except Exception as e:
            DBException("<exception in DB.update_student>")
            return False

    def get_all_faculty(self):
        '''
            @return: list of all faculty objects
        '''
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM `faculty`"
                cursor.execute(sql)
                result = cursor.fetchall()
                if result is None:
                    UserNotFoundException("User not found :/ <exception in DB.get_all_faculty>")
                    return None
                else:
                    facultyList = []
                    for row in result:
                        faculty = Faculty()
                        faculty.id = row[0]
                        faculty.subjectTeaching = row[1]
                        faculty.designation = row[2]
                        faculty.userID = row[3]
                        facultyList.append(faculty)
                    return facultyList
        except Exception as e:
            DBException("<exception in DB.get_all_faculty>")
            return None

    def get_all_students(self):
        '''
            @return: list of all student objects
        '''
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM `students`"
                cursor.execute(sql)
                result = cursor.fetchall()
                if result is None:
                    UserNotFoundException("User not found :/ <exception in DB.get_all_students>")
                    return None
                else:
                    studentList = []
                    for row in result:
                        student = Student()
                        student.id = row[0]
                        student.semester = row[1]
                        student.cgpa = row[2]
                        student.major = row[3]
                        student.userID = row[4]
                        studentList.append(student)
                    return studentList
        except Exception as e:
            DBException("<exception in DB.get_all_students>")
            return None

    def get_all_users(self):
        '''
            @return: list of all user objects
        '''

        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM `users`"
                cursor.execute(sql)
                result = cursor.fetchall()
                if result is None:
                    UserNotFoundException("User not found :/ <exception in DB.get_all_users>")
                    return None
                else:
                    userList = []
                    for row in result:
                        user = User()
                        user.userID = row[0]
                        user.username = row[1]
                        user.password = row[2]
                        userList.append(user)
                    return userList
        except Exception as e:
            DBException("<exception in DB.get_all_users>")
            return None

    def delete_user(self, userID):
        '''
            @param userID: user id
            @return: True if user deleted successfully
            @return: False if user not deleted
        '''

        try:
            with self.connection.cursor() as cursor:
                sql = "DELETE FROM `users` WHERE `id`=%s"
                cursor.execute(sql, (userID))
                self.connection.commit()
                return True
        except Exception as e:
            DBException("<exception in DB.delete_user>")
            return False

    def delete_student(self, studentID):
        '''
            @param studentID: student id
            @return: True if student deleted successfully
            @return: False if student not deleted
        '''

        try:
            with self.connection.cursor() as cursor:
                sql = "DELETE FROM `students` WHERE `id`=%s"
                cursor.execute(sql, (studentID))
                self.connection.commit()
                return True
        except Exception as e:
            DBException("<exception in DB.delete_student>")
            return False

    def delete_faculty(self, facultyID):
        '''
            @param facultyID: faculty id
            @return: True if faculty deleted successfully
            @return: False if faculty not deleted
        '''

        try:
            with self.connection.cursor() as cursor:
                sql = "DELETE FROM `faculty` WHERE `id`=%s"
                cursor.execute(sql, (facultyID))
                self.connection.commit()
                return True
        except Exception as e:
            DBException("<exception in DB.delete_faculty>")
            return False

    def if_username_available(self, username):
        '''
            @param username: username
            @return: True if username available
            @return: False if username not available
        '''

        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM `users` WHERE `username`=%s"
                cursor.execute(sql, (username))
                result = cursor.fetchone()
                if result is None:
                    return True
                else:
                    return False
        except Exception as e:
            DBException("<exception in DB.if_username_available>")
            return False
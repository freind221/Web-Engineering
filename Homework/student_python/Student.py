from User import User

class Student(User):
    def __init__(self, username, password, semester, cgpa, major):
        super().__init__(username, password)
        self.__studentID = None
        self.__semester = semester
        self.__cgpa = cgpa
        self.__major = major

    @property
    def studentID(self):
        return self.__studentID

    @studentID.setter
    def studentID(self, value):
        self.__studentID = value

    @property
    def semester(self):
        return str(self.__semester)

    @semester.setter
    def semester(self, semester):
        self.__semester = semester

    @property
    def cgpa(self):
        return str(self.__cgpa)

    @cgpa.setter
    def cgpa(self, cgpa):
        self.__cgpa = cgpa

    @property
    def major(self):
        return self.__major

    @major.setter
    def major(self, major):
        self.__major = major

    def __str__(self):
        return f"ID: {self.__studentID}, Username: {self.username}, Password: {self.password}, Semester: {self.__semester}, CGPA: {self.__cgpa}, Major: {self.__major}"
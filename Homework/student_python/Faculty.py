from User import User

class Faculty(User):
    def __init__(self, username, password, subjectTeaching, designation):
        super().__init__(username, password)
        self.__facultyID = None
        self.__subjectTeaching = subjectTeaching
        self.__designation = designation

    @property
    def facultyID(self):
        return self.__facultyID

    @facultyID.setter
    def facultyID(self, value):
        self.__facultyID = value

    @property
    def subjectTeaching(self):
        return self.__subjectTeaching

    @subjectTeaching.setter
    def subjectTeaching(self, subjectTeaching):
        self.__subjectTeaching = subjectTeaching

    @property
    def designation(self):
        return self.__designation

    @designation.setter
    def designation(self, designation):
        self.__designation = designation

    def __str__(self):
        return f"ID: {self.__facultyID}, Username: {self.username}, Password: {self.password}, Subject Teaching: {self.__subjectTeaching}, Designation: {self.__designation}"
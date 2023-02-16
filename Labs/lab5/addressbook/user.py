class User():
    def __init__(self,  email, password):
        self.__userID = None
        self.__password = password
        self.__email = email

    @property
    def userID(self):
        return self.__userID

    @userID.setter
    def userID(self, value):
        self.__userID = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email
    
    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

    def __str__(self):
        return f"ID: {self.__userID}, email: {self.__email}, password: {self.__password}"
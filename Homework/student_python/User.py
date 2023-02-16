class User():
    def __init__(self, username, password):
        self.__userID = None
        self.__username = username
        self.__password = password

    @property
    def userID(self):
        return self.__userID

    @userID.setter
    def userID(self, value):
        self.__userID = value

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username):
        self.__username = username

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

    def __str__(self):
        return f"ID: {self.__userID}, Username: {self.__username}, Password: {self.__password}"
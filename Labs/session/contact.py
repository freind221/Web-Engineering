class Contact():
    def __init__(self, name, mobileno, city, profession):
        self.__contactID = None
        self.__name = name
        self.__mobileno = mobileno
        self.__city = city
        self.__profession = profession

    @property
    def contactID(self):
        return self.__contactID

    @contactID.setter
    def contactID(self, value):
        self.__contactID = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def mobileno(self):
        return self.__mobileno

    @mobileno.setter
    def mobileno(self, mobileno):
        self.__mobileno = mobileno

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, city):
        self.__city = city
    
    @property
    def profession(self):
        return self.__profession

    @profession.setter
    def profession(self, profession):
        self.__profession = profession

    def __str__(self):
        return f"ID: {self.__contactID}, name: {self.__name}, mobileno: {self.__mobileno}, city: {self.__city}, profession: {self.__profession}"
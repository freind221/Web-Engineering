class Student():
    def __init__(self,r,n,s,c):
        self.__name=n
        self.__rollno=r
        self.rollno = r
        self.cgpa=c
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,n):
        if n!=None and n!="":
            self.__name=n
        else:
            self.__name = "default"


    def printString(self):
        print("Name:",self.__name,"RollNo:",
              self.__rollno,"CGPA:",self.__cgpa)
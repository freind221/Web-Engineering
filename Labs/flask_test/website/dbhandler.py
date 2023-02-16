from Exceptions import DBError
import pymysql
from User import User
from Student import Student
class DBHandler:
    def __init__(self,host,user,password,database):
        self.host=host
        self.user = user
        self.password=password
        self.database=database

    def printStudents(self):
        mydb = None
        mydbCursor=None
        try:
            # Get DB Connection
            mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            # Get cursor object
            mydbCursor = mydb.cursor()
            # sql="Select * from students"
            sql = "Select rollno,name,semmester from students"
            mydbCursor.execute(sql)
            myresults = mydbCursor.fetchall()
            for r in myresults:
                print(r)
                # print("id:",r[0],"Rollno:",r[1],"Name:",r[2],"Semmester:",r[3],"CGPA:",r[4])
                print("Rollno:", r[0], "Name:", r[1], "Semmester:", r[2])

        except Exception as e:
            print(str(e))
        finally:
            if mydbCursor != None:
                mydbCursor.close()
            if mydb != None:
                mydb.close()

    def getAllStudents(self):
        mydb = None
        studentsList = []
        try:
            # Get DB Connection
            mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            # Get cursor object
            mydbCursor = mydb.cursor()
            # sql="Select * from students"
            sql = "Select rollno,name,semmester ,cgpa from students"
            mydbCursor.execute(sql)
            myresults = mydbCursor.fetchall()
            for r in myresults:
                #print(r)
                # print("id:",r[0],"Rollno:",r[1],"Name:",r[2],"Semmester:",r[3],"CGPA:",r[4])
                #print("Rollno:", r[0], "Name:", r[1], "Semmester:", r[2])
                #obj=User(r[0],r[1],r[2],r[3])
                studentsList.append(Student(r[0],r[1],r[2],r[3]))
        except Exception as e:
            print(str(e))
        finally:
            if mydb != None:
                mydb.close()
            return studentsList
    def insertStudent(self,student):
        mydb = None
        try:
            # Get DB Connection
            mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            # Get cursor object
            mydbCursor = mydb.cursor()
            sql = "insert into students (rollnumber,name,semmester,cgpa) values(%s,%s,%s,%s)"
            args = (student.roll, rollno)
            mydbCursor.execute(sql, args)
            mydb.commit()
        except Exception as e:
            print(str(e))
        finally:
            if mydb != None:
                mydb.close()


    def updateStudentSemmesterByRollno(self,rollno, semmester):
        mydb = None
        try:
            # Get DB Connection
            mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            # Get cursor object
            mydbCursor = mydb.cursor()
            sql = "update students set semmester=%s where rollno=%s"
            args = (semmester, rollno)
            mydbCursor.execute(sql, args)
            mydb.commit()
        except Exception as e:
            print(str(e))
        finally:
            if mydb != None:
                mydb.close()

    def selectAllUsers(self):
        mydb=None
        try:
            mydb = pymysql.connect(host=self.host,user=self.user,password=self.password,database=self.database)
            # DB Connection Cursor
            mycursor = mydb.cursor()
            # Using Cursor execute queries
            mycursor.execute("SELECT id,name,city,mobile FROM users")
            # Using CurosrObject fetch all rows which are selected after the exection of query
            myresult = mycursor.fetchall()
            for x in myresult:
                # print(x)
                print("ID:", x[0], "Name:", x[1], "City:", x[2], "Mobile:", x[3])
        except Exception as e:
            print(str(e))
            raise DBError("Error Select data from table users",str(e))
        finally:
            if mydb!=None:
                mydb.close()
    def provideAllUsers(self):
        mydb=None
        usersList = []
        try:
            mydb = pymysql.connect(host=self.host,user=self.user,password=self.password,database=self.database)
            # DB Connection Cursor
            mycursor = mydb.cursor()
            # Using Cursor execute queries
            mycursor.execute("SELECT id,name,city,mobile FROM users")
            # Using CurosrObject fetch all rows which are selected after the exection of query
            myresult = mycursor.fetchall()
            for x in myresult:
                # print(x)
                usersList.append(User(x[0],x[1],x[2],x[3]))
                print("ID:", x[0], "Name:", x[1], "City:", x[2], "Mobile:", x[3])
        except Exception as e:
            print(str(e))
            raise DBError("Error Select data from table users",str(e))
        finally:
            if mydb!=None:
                mydb.close()
                return usersList

    def updateUserCityByName(self, name, city):
        try :
            mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            # DB Connection Cursor
            mycursor = mydb.cursor()
            sql = 'update  users  set city_ = %s where name=%s'
            args = (city, name)
            #print(sql)
            mycursor.execute(sql, args)
            mydb.commit()
        except Exception as e:
            print(str(e))
            raise DBError("Error updateUserCityByName data from table users",str(e))
        finally:
            if mydb!=None:
                mydb.close()
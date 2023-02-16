from Exceptions import *
from contact import Contact
from user import User
import mysql.connector
import pymysql

class DB:
    def __init__(self):
        self.connection = pymysql.connect(host='localhost', user='root', password='kamran', db='testing')
        if(self.connection):
            print("Connection")
        else:
            print("Not connected")
    def register_contact(self, name, mobileno, profession, userId):
        try:
            with self.connection.cursor() as cursor:
                sql = "INSERT INTO `newcontacts` (`name`, `mobileno`,`user_id`, `profession`) VALUES ( %s,%s,%s,%s)"
                cursor.execute(sql, (name, mobileno,userId , profession))
                self.connection.commit()
                return True
        except Exception as e:
            print(e)
            ContactAlreadyExistsException("Contact already exists :/ <exception in DB.register_user>")
            return False

    def register_user(self, email, password):
        try:
            with self.connection.cursor() as cursor:
                sql = "INSERT INTO `contactuser` (`email`, `password`) VALUES (%s, %s)"
                cursor.execute(sql, (email, password))
                self.connection.commit()
                return True
        except Exception as e:
            print(e)
            ContactAlreadyExistsException("User already exists :/ <exception in DB.register_user>")
            return False
        

    def get_contact(self, name):
       
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM `newcontacts` WHERE `name`=%s"
                cursor.execute(sql, (name))
                result = cursor.fetchone()
                if result is None:
                    ContactNotFoundException("Contact not found :/ <exception in DB.get_student>")
                    return None
                else:
                    contact = Contact(result[1], result[2], result[3], result[4])
                    contact.contactID = result[0]
                    print(result[1])
                    return contact
        except Exception as e:
            DBException("<exception in DB.get_contact>")
            return None
    
    def login(self, email, password):
       
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM `contactuser` WHERE `email`=%s AND `password`=%s"
                cursor.execute(sql, (email, password))
                result = cursor.fetchone()
                # print(result)
                if result is None:
                    ContactNotFoundException()
                    return False
                else:
                    user = User(result[1], result[2])
                    user.userID = result[0]
                    print(user)
                    return True
        except Exception as e:
            DBException("<exception in DB.get_contact>")
            return False

    def getUserId(self, email, password):
       
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM `contactuser` WHERE `email`=%s AND `password`=%s"
                cursor.execute(sql, (email, password))
                result = cursor.fetchone()
                print(result)
                if result is None:
                    ContactNotFoundException("user not found :/ <exception in DB.get_student>")
                    return None
                else:
                    user = User(result[1], result[2])
                    user.userID = result[0]
                    print(result[1])
                    return result[0]
        except Exception as e:
            DBException("<exception in DB.get_contact>")
            return None

    def getAllContacts(self):
        sql = "SELECT * FROM `contactuser`"
        self.cursor.execute(sql)
        return self.cursor.fetchall() 
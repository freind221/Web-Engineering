import pymysql
from exceptions import *
from contact import Contact
from user import User

class DBHandler:
    # class level / Static attrs
    users = []
    students = []
    faculties = [] 
    
    def __init__(self,host,user,passwd,database) -> None:
        try:
            self.users = []
            self.contacts = []
            self.connection = pymysql.connect(host=host,user=user,passwd=passwd,database=database)
            # pymysql.cursors.DictCursor will automatically map columsn names to items of items at respective indexes
            self.connection.autocommit(True)
            
            self.cursor = self.connection.cursor(pymysql.cursors.DictCursor)
            self.getAllContacts()
            self.getAllUsers()
            print("Connected ")
        except:
            print("ERRROR: Connected ")
            try: 
                raise DatabaseConnectivityError
            except DatabaseConnectivityError:
                return
    
    
    def getAllContacts(self):
        sql = "SELECT * FROM `newcontacts`"
        self.cursor.execute(sql)
        return self.cursor.fetchall()   
     
    def getAllUsers(self):
        sql = "SELECT * FROM `contactuser`"
        self.cursor.execute(sql)
        self.users =  self.cursor.fetchall()
        return self.users
    
    
    def checkUser(self,user:User):
        for x in self.users:
            if user.email.strip() == str(x.get("email")).strip():
                return x
        return False
    
    def insertNewUser(self,user:User):
        if not self.checkUser(user=user):
            sql = f"INSERT INTO `contactuser` (`id`, `email`, `password`) VALUES (NULL, '{user.email}', '{user.password}');"
            self.cursor.execute(sql)
            self.connection.commit()
            self.getAllUsers()
            return True
        else:
            return "Email Already Exists"    
        
        
    def loginUser(self,user:User):
        res =  self.checkUser(user=user)
        if res and res.get("password")==user.password:
            return res
        else:
            return False
    
    def insertContact(self,contact:Contact): 
        try:
            sql = f"INSERT INTO `newcontacts` (`id`,`user_id`, `name`, `mobileno`, `city`, `profession`) VALUES (NULL, '{contact.user_id}','{contact.name}', '{contact.mobileno}', '{contact.city}', '{contact.profession}');"
            self.cursor.execute(sql)
            self.connection.commit()
            return True
        except:
            try:
                raise contactInsertionError
            except contactInsertionError:
                return False    
            
    def updateContact(self,contact:Contact): 
        try:
            sql = f"UPDATE `newcontacts` SET `user_id` = '{contact.user_id}', `name` = '{contact.name}', `mobileno` = '{contact.mobileno}', `city` = '{contact.city}', `profession` = '{contact.profession}' WHERE `contacts`.`id` = {contact.id}"
            self.cursor.execute(sql)
            self.connection.commit()
            self.getAllContacts()
            return True
        except:
            return False
        
    def deleteContact(self,id,user_id):
        sql = f"DELETE FROM `newcontacts` WHERE `contacts`.`id` = {id} AND  `contacts`.`user_id` = {user_id} "
        self.cursor.execute(sql)
        self.connection.commit()
        self.getAllContacts()
        
        
if __name__=="__main__": 
    db = DBHandler(host="localhost",user="root",passwd="",database="test")
    
    print(db.getAllContacts())
    # print(db.get_student(username="ali",password="ali"))
    
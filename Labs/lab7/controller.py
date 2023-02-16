from db import DBHandler


_db = DBHandler(host="localhost",user="root",passwd="",database="testing")


class ContactController:
    def __init__(self) -> None:
        pass
    
    def getAllContacts(self):
        return _db.getAllContacts()
    
    def insertConatct(self,contact):
        return _db.insertContact(contact)   
    
    def updateContact(self,contact):
        return _db.updateContact(contact)   
    
     
    def insertNewUser(self,user):
        return _db.insertNewUser(user)   
    
      
    def loginUser(self,user):
        return _db.loginUser(user) 
    
         
    def deleteContact(self,id,user_id):
        return _db.deleteContact(id,user_id)
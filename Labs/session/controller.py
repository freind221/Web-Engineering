from contact import Contact

from db import DB
class ContactController():
    def __init__(self):
        # self.__contact = Contact(None, None, None, None, None)
        self.__db = DB()
    
    
    def register(self, db, name, mobileno, profession, userId):
        check = db.register_contact(name, mobileno , profession, userId)
        return check

    def search(self, db, name):
        
        print(db.get_contact(name))
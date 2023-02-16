from .db import  db

class Product(db.Document):
    name=db.StringField(required=True)
    price=db.StringField(required=True)
    desc=db.StringField(required=True)


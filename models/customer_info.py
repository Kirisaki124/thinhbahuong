from mongoengine import *
class Customer(Document):
    name = StringField()
    phone = StringField()
    email = StringField()
    package = IntField() # Cơ bản 1, Nâng cao 2, Dài hạn 3
    address = StringField()
    note = StringField()

class Service_Package(Document):
    name = StringField()
    description = StringField()
    price = IntField()

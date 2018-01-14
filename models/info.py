from mongoengine import Document, StringField, IntField, BooleanField

class Package(Document):
    name = StringField()
    choice = BooleanField()

class Customer(Document):
    package = IntField()
    name = StringField()
    phone = StringField()
    address = StringField()
    email = StringField()
    message = StringField()

from mongoengine import Document, StringField, IntField, BooleanField

class Package(Document):
    name = StringField()
    choice = BooleanField()

class Customer(Document):
    package = StringField()
    name = StringField()
    address = StringField()
    email = StringField()
    message = StringField()

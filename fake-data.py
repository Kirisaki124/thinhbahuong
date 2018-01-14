from mlab import mlab_connect
from models.info import *
from faker import Faker
from random import randint, choice

name_faker = Faker()
mlab_connect()

for _ in range(10):
    services = Customer(
                        name = name_faker.name(),
                        address = choice(["q","w","e"]),
                        email = choice(["@123","@456","@789"]),
                        message = choice(["1","2","3"]),
                        package = choice(["p1", "p2", "p3"]))
    services.save()

from mlab import mlab_connect
from models.customer_info import *
from faker import Faker
from random import randint, choice

name_faker = Faker()
mlab_connect()

for _ in range(10):
    services = Customer(
                        name = name_faker.name(),
                        note = choice(["q","w","e"]),
                        email = choice(["kirisaki124@yahoo.com"]),
                        package = choice([1, 2, 3]))
    services.save()

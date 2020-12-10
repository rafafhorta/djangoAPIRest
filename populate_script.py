import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from faker import Faker
import random
from favproducts.models import Client

def creating_clients(clients_number):
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(clients_number):
        name = fake.name()
        email = '{}@{}'.format(name.lower(),fake.free_email_domain())
        email = email.replace(' ', '')
        p = Client(name=name, email=email)
        p.save()

creating_clients(50)
print('Sucesso!')
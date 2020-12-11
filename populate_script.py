import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aplicacao.settings')
django.setup()

from faker import Faker
import random
from favproducts.models import Client, Product

def creating_clients(clients_number):
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(clients_number):
        name = fake.name()
        email = '{}@{}'.format(name.lower(),fake.free_email_domain())
        email = email.replace(' ', '')
        c = Client(name=name, email=email)
        c.save()

title_list = [
    'Relógio','Xícara','Teclado',
    'Quebra-cabeça','Bola','Tênis',
    'Bermuda','Camisa','Escova',
    'Lâmpada','Livro','Lapiseira','Almofada' ]

brand_list = [
    'Casio','Nadir','Logitech',
    'Estrela','Fila','All Star',
    'Adidas','Levis','Ricca',
    'Positivo','Rocco','Pentel','Artex' ]

def creating_products(products_number):
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(products_number):
        price = "{}".format(random.randrange(20, 150))
        image = fake.image_url()
        brand = fake.word(ext_word_list=brand_list)
        title = fake.word(ext_word_list=title_list)
        reviewScore = "{}".format(random.randrange(0, 10))
        p = Product(price=price, image=image, brand=brand, title=title, reviewScore=reviewScore,)
        p.save()

creating_clients(40)
creating_products(40)
print('Sucesso!')
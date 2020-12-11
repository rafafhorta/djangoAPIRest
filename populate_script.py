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

img_url = ['https://www.escuelapython.com/wp-content/uploads/2018/07/Django-instalacion-workspace.jpg']


def creating_products(products_number):
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(products_number):
        price = "{}".format(random.randrange(20, 150))
        image = fake.word(ext_word_list=img_url)
        brand = fake.word(ext_word_list=brand_list)
        title = fake.word(ext_word_list=title_list)
        reviewScore = "{}".format(random.randrange(0, 10))
        p = Product(price=price, image=image, brand=brand, title=title, reviewScore=reviewScore,)
        p.save()

creating_clients(20)
creating_products(20)
print('Sucesso!')
##Django API
Esta é uma API de Produtos Favoritos, onde é possível criar clientes, produtos e cada cliente pode adicionar produtos a sua lista de produtos favoritos.
Utilizaremos o banco de dados do PostgreSQL.

##Instalação 
1- clonar o repositório
2- criar o ambiente virtual: python -m venv ./venv
3- ativando o venv (na powershell): venv\Scripts\Activate.ps1
4- instalar todos os módulos necessários: pip install -r requirements.txt
5- selecionar o interpretador python da venv
6- copiar o conteúdo do arquivo settings.example.py criar um arquivo chamado settings.py na pasta aplicacao com o conteúdo copiado
7- para gerar a secret key rodar o comando: python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
8- copiar a secret key gerada e atualizar em SECRET_KEY (dentro das aspas simples) no arquivo settings.py
9- criar uma tabela no banco de dados Postgre e configurar no arquivo settings.py  o NAME, USER e PASSWORD conforme foi criado no Postgre
10- rodar a aplicação: python manage.py runserver

Em outro terminal
11- verificar se há migrações para serem feitas: python manage.py makemigrations
12- fazer as migrações: python manage.py migrate
13- criar um super usuário para utilizar a aplicação: python manage.py createsuperuser
14- criar clientes e produtos com o faker: python populate_script.py
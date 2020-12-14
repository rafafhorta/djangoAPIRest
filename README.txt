##Django API
Esta é uma API de Produtos Favoritos, onde é possível criar clientes, produtos e cada cliente pode adicionar produtos a sua lista de produtos favoritos.
Utilizaremos o banco de dados do PostgreSQL.

##Instalação 
1- clonar o repositório
2- criar o ambiente virtual: python -m venv ./venv
3- ativando o venv (na powershell): venv\Scripts\Activate.ps1
4- instale todos os módulos necessários: pip install -r requirements.txt
5- copie o conteúdo do arquivo settings.example.py e crie um arquivo chamado settings.py na pasta aplicacao com o conteúdo copiado
6- para gerar a secret key rode o comando: python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
7- copie a secret key gerada e atualize em SECRET_KEY (dentro das aspas simples) no arquivo settings.py
8- crie uma tabela no banco de dados Postgre e configure no arquivo settings.py  o NAME, USER e PASSWORD conforme foi criado no Postgre
11- verifique se há migrações para serem feitas com o comando: python manage.py makemigrations
11- faça as migrações com o comando: python manage.py migrate
12- crie um super usuário para utilizar a aplicação: python manage.py createsuperuser
13- crie clientes e produtos com o faker: python populate_script.py
14- rode a aplicação: python manage.py runserver
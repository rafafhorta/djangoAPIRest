##Django API
Esta é uma API de Produtos Favoritos, onde é possível criar clientes, produtos e cada cliente pode adicionar produtos a sua lista de produtos favoritos.

##Instalação 
1- clonar o repositório
2- criar o ambiente virtual: python -m venv ./venv
3- ativando o venv (na powershell): venv\Scripts\Activate.ps1
4- instalar todos os módulos necessários: pip install -r requirements.txt
5- selecionar o interpretador python da venv
6- criar uma tabela no banco de dados Postgre e configurar no arquivo settings.py  o NAME, USER e PASSWORD conforme foi criado no Postgre
7- rodar a aplicação: python manage.py runserver

Em outro terminal
8- verificar se há migrações para serem feitas: python manage.py makemigrations
9- fazer as migrações: python manage.py migrate
10- criar um super usuário para utilizar a aplicação: python manage.py createsuperuser
11- criar clientes e produtos com o faker: python populate_script.py
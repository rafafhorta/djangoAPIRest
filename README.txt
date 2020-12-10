Para inicializar o projeto: 
1- criar o ambiente virtual: python -m venv ./venv
2- ativando o venv (na powershell): venv\Scripts\Activate.ps1
3- instalar todos os módulos necessários: pip install -r requirements.txt
4- selecionar o interpretador python da venv
5- rodar a aplicação: python manage.py runserver
Em outro terminal
6- verificar se há migrações para serem feitas: python manage.py makemigrations
7- fazer as migrações: python manage.py migrate
8- criar um super usuário para utilizar a aplicação: python manage.py createsuperuser
9- criar clientes e produtos com o faker: python populate_script.py
##Django API
Esta é uma API de Produtos Favoritos, onde é possível criar clientes, produtos e cada cliente pode adicionar produtos a sua lista de produtos favoritos.
É necessário já ter instalado o Python 3.9 e o banco de dados PostgreSQL.

##Instalação 
1- clonar o repositório
2- instalar a virtual env: pip install virtualenv
3- criar o ambiente virtual: python -m venv_aplicacao ./venv
    ou virtualenv venv_aplicacao
4- ativando o venv na powershell: venv_aplicacao\Scripts\Activate.ps1
    no cmd: venv_aplicacao\Scripts\activate.bat
    ou no linux e mac: source venv_aplicacao/bin/activate
5- instale todos os módulos necessários: pip install -r requirements.txt
6- copie o conteúdo do arquivo settings.example.py e crie um arquivo chamado settings.py na pasta aplicacao com o conteúdo copiado
7- para gerar a secret key rode o comando: python -c "import secrets; print(secrets.token_urlsafe())"
8- copie a secret key gerada e atualize em SECRET_KEY (dentro das aspas simples) no arquivo settings.py
9- crie uma tabela no banco de dados Postgre e configure no arquivo settings.py  o NAME, USER e PASSWORD conforme foi criado no Postgre
10- verifique se há migrações para serem feitas com o comando: python manage.py makemigrations
11- faça as migrações com o comando: python manage.py migrate
12- crie um super usuário para utilizar a aplicação: python manage.py createsuperuser
13- crie clientes e produtos com o faker: python populate_script.py
14- rode a aplicação: python manage.py runserver

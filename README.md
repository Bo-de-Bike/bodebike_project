
## 1 - COMEÇANDO O PROJETO

### 1.1 SSH

https://help.github.com/articles/generating-ssh-keys/

OBS : Se der esse erro quando vc for subir suas alterações : 

" fatal: Could not read from remote repository.
Please make sure you have the correct access rights
and the repository exists. "

rode o comando : git remote set-url origin git@github.com:Projeto-BD/vacinou_project.git

### 1.2 - Clone

criem uma pasta Projeto e dentro dela:

### HTTPS:

$ git clone https://github.com/Projeto-BD/vacinou_project.git

### SSH

$ git clone git@github.com:Projeto-BD/vacinou_project.git

## 2 - Configurando o Projeto 

  2.1 - Primeiro passo, configure a virtualenvwrapper e o pip ( se ja tiver pula para o passo 2.1.2 )
  
    2.1.1 - sudo apt-get install python-pip
    2.1.2 - sudo apt-get install python-virtualenv
    2.1.3 - sudo pip install virtualenvwrapper
    
  2.2 - Após instalar o virtualenvwrapper, adicionar o código abaixo ao .bashrc
  
    if
      [ -d "$HOME/.local/bin" ]; then
      PATH="$HOME/.local/bin:$PATH"
    fi
    
      # Add virtualenvwrapper variables
      export WORKON_HOME=$HOME/Envs
      export PROJECT_HOME=$HOME/Projects
      source virtualenvwrapper.sh
  
    OBS: se der erro nesta parte : 
  
    " /usr/bin/python: No module named virtualenvwrapper
      virtualenvwrapper.sh: There was a problem running the initialization hooks. 

      If Python could not import the module virtualenvwrapper.hook_loader,
      check that virtualenv has been installed for
      VIRTUALENVWRAPPER_PYTHON=/usr/bin/python and that PATH is
      set properly. "
      
    Execute : 1 - sudo easy_install pip
              2 - sudo pip install --upgrade virtualenvwrapper

  2.3 - Ainda com o ambiente virtual...
  
    2.3.1 - Criar um novo ambiente virtual
      - mkvirtualenv nome_da_virtualenv
    2.3.2 - Remover a virtualenv
      - rmvirtualenv nome_da_virtualenv
    2.3.3 - Ativa o ambiente 
      - workon nome_da_virtualenv
    2.3.4 - Desativa o ambiente 
      - deactivate
      
  2.4 - Instalando as detendencias do projeto 
  
    2.4.1 - Entre na pasta raiz do projeto e rode o comando : make deps
  
  2.5 - Configurando o Postgre com Django: 
    
    2.5.1 - sudo apt-get install libpq-dev python-dev
    2.5.2 - sudo apt-get install postgresql postgresql-contrib
    
    2.5.3 - Criando o usuário no psql
    
    Abra o terminal e digite:
    
    - sudo su postgres
    - postgres~$ psql
    - postgres=# CREATE USER vacinou WITH PASSWORD 'vacinou123' LOGIN CREATEDB;
    - postgres=# CREATE DATABASE vacinou OWNER vacinou;
    
    2.5.4 - Gere as Tabelas
    
      No terminal (na raiz do projeto), rode o comando:
        
       ~$ make setup
    
  2.6 - Atalhos 
  
    2.6.1 - Rodar o projeto : make run
    2.6.2 - Reseta o banco e cria um superusuário : make restart
    2.6.3 - Para fazer a migração do banco de dados : make setup
    
    
    
## PRONTO - PODE CODAR !


## 3 - Links

Virtualenv : 

3.1 - http://blog.tiveron.mitgnu.com/2011/05/virtualenvwrapper/

How To Install and Configure Django with Postgres, Nginx, and Gunicorn:

3.2 - https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-django-with-postgres-nginx-and-gunicorn

Git:

3.3 Documentação Oficial: http://git-scm.com/documentation

Django:

3.4 Class Based Views: http://ccbv.co.uk/projects/Django/1.5/django.views.generic.list/ListView/

3.5 Documentação Oficial: https://docs.djangoproject.com/en/1.6/

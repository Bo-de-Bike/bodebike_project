
## 1 - COMEÇANDO O PROJETO

### 1.1 SSH

Primeiro passo, verifique se existe ssh em seu computador:

ls -al ~/.ssh
se existe um arquivo chamado "id_rsa.pub", abra o arquivo copie e pule para o ultimo passo.

Segundo passo, gere uma ssh key:

ssh-keygen -t rsa -C "email@example.com"
aperte ENTER e digite sua senha.

depois:

ssh-add ~/.ssh/id_rsa

Ultimo passo:

gedit ~/.ssh/id_rsa.pub
após abrir o arquivo, copie o código e vá em: Settings > SSH Keys > Add Key e adicione o código.

### 1.2 - Clone

criem uma pasta Projeto e dentro dela:

### HTTPS:

$ git clone https://github.com/Bo-de-Bike/bodebike_project.git

### SSH

$ git clone git@github.com:Bo-de-Bike/bodebike_project.git

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
  
    2.4.1 - entre na pasta raiz do projeto e rode o comando : make deps
    
    
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


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

## 2 - Links

Git:

2.1 Documentação Oficial: http://git-scm.com/documentation

Django:

2.1 Class Based Views: http://ccbv.co.uk/projects/Django/1.5/django.views.generic.list/ListView/

2.2 Documentação Oficial: https://docs.djangoproject.com/en/1.6/

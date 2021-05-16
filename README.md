# Medicar

## Descrição do projeto
Projeto fullstack de criação de agendas médicas e marcação de consultas.

A descrição de detalhes desse desafio e do objetivo está neste [link](https://github.com/Intmed-Software/desafio).

O projeto contém duas pastas para separar a estrutura da aplicação: *backend* feito utilizando [Django REST framework](https://www.django-rest-framework.org/) e *frontend* utilizando [Angular](https://angular.io/).

## Backend - Django REST

### Executando o projeto localmente

#### Requisitos

 - Python 3 instalado.
 
#### Instruções
Após baixar o projeto, entre na pasta **backend** e execute os seguintes comandos:

      #cria o ambiente virtual
      python -m venv env
	  
	  #ativa o ambiente (Linux)
	  source env/bin/activate
	  #ativa o ambinente (Windows - Powershell)
	  .\env\Scripts\activate
	  
	  #instale as dependências (Windows - Powershell)
	  python -m pip install -r requirements.txt
	  
	  #instale as dependências (Linux)
	  pip install -r requirements.txt
	  
	  #Django - Rodando o projeto (Windows - Powershell)
	  py .\manage.py makemigrations
	  py .\manage.py migrate
	  py .\manage.py runserver
	  
	  #Django - Rodando o projeto (Linux)
	  py manage.py makemigrations
	  py manage.py migrate
	  py manage.py runserver
	
  ### Aplicação publicada
  
 A estrutura *backend* foi publicada utilizando o [Heroku](https://www.heroku.com/)  e está disponível no seguinte endereço:
https://teste-api-medicar.herokuapp.com/.


### Estrutura 
O projeto foi dividido em **contextos** para melhor organizar o código, cada contexto tem um ***app***  definido com sua devida responsabilidade, portanto realizam as validações e demais operações definidas nas especificações do [desafio](https://github.com/Intmed-Software/desafio/tree/master/backend). Os contextos são:

 - Agenda;
 - Consulta;
 - Medico;
 - Usuário;

### Recursos (Endpoints)
 Os recursos estão de acordo com o especificado no [desafio](https://github.com/IntmedSoftware/desafio/tree/master/backend) incluindo todas as estruturas de resposta e envio de informações definidas.

A única mudança feita foi realizada no ato de criar um usuário. A rota continua a mesma porém é preciso passar um *json* com as seguintes informações:

    {
		"first_name":"Seu nome",
		"last_name":"Seu sobrenome",
		"username":"seu_usuario",
		"email":"exemplo@email.com",
		"password":"Sua senha"
    }

>O *body* teve que ser alterado para que o nome fosse retornado ao logar na aplicação.
 
 ### Observações
 Ao ser publicada no  [Heroku](https://www.heroku.com/), as validações de fuso horário podem apresentar um problema, devido a localização do servidor ser nos Estados Unidos. Para os testes com a API publicada, deve-se levar em conta a diferença de **+3 horas** em relação ao nosso horário local.


## Frontend (Em construção)

![](https://image.flaticon.com/icons/png/128/2973/2973702.png)

> Written with [StackEdit](https://stackedit.io/).

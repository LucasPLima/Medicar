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

    #Cria o ambiente virtual
    python -m venv env
    
    #Ativa o ambiente virtual
    .\env\Scripts\activate
    
    #Instale as dependências
    python -m pip install -r requirements.txt
    
    #Django - Executa as migrations 
    py .\manage.py migrate
	
	#Opcional - Populando o banco
    py .\manage.py loaddata fixtures/initial_data.json
    
    #Django - Roda o servidor
    py .\manage.py runserver
    
    
    
> Caso utilize o comando opcional de popular o banco com dados iniciais, a fixture já cria um super usuário, 2 especialidades, 4 médicos, 4 agendas (uma para cada médico) e 3 horários para cada agenda.
> As credenciais do superusuário são:  admin/admin.
	
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
 

## Frontend - Angular

O frontend da aplicação foi desenvolvido seguindo as especificações listadas neste [link](https://github.com/Intmed-Software/desafio/tree/master/frontend).

A aplicação conta com as ações de:
 - Criação de usuário;
 - Login na aplicação;
 - Visualização de consultas marcadas;
 - Criação e exclusão de consultas.

O projeto não foi publicado, portanto deve ser rodado localmente.

### Executando a aplicação localmente
Após realizar o clone do projeto, entre na diretório"*frontend/medicar*" e execute os comandos abaixo:

    # Se você utiliza yarn
    yarn install
    
    # Se você utiliza npm
    npm install
	
	# Após baixar as dependências, execute o projeto
	yarn start
	#ou
	npm run start

A aplicação irá rodar na porta **4200** e irá se comunicar com a API na porta **8000** (porta padrão do Django REST).

### Observações

- Diferente da referência para a criação do frontend, durante o login do usuário só poderá ser utilizado o **username**.
- Na criação de usuário foram incluídas duas informações para identificação do usuário, "Nome" e "Sobrenome".


> Written with [StackEdit](https://stackedit.io/).

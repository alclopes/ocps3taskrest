<div id='top'/>

# Projeto   

* Este projeto foi iniciado em Python==3.4 e Django==1.8 enquanto fazia curso no site Udemy.
* Apos este curso o projeto foi ampliado com novas bibliotecas, funcionalidades, controles e migrado para versões mais novas do Python (3.7) e Django (2.2.4)  

* [Próximos Passos](#nextsteps)
* [Atividades Concluídas](#done)
* [Lista de Tabelas e funcionalidades do projeto](#services)
* [Boas Práticas/Cuidados](#atention)
* [Conheça o projeto](#see)


<div id='nextsteps'/>

## Próximos Passos - Plan  


### Importação de dados referentes a cursos de parceiros 
* Utilizar JSON/Rest para importar dados referentes a cursos de parceiros 
* Aguardando

### Deploy - AWS (Cloud IAAS)
* Aguardando

### Deploy - Puppet/Docker/Travis
* Puppet/Ansible (provisionamento de maquina scripts de preparação do servidor, provisionamento da maquina.
* Docker (Virtualização por containeres)rodar a aplicação localmente com a exata configuração do ambiente de produção) 
* Aguardando

[Voltar ao topo](#top)


<div id='done'/>


## Atividades Concluídas - Done

### Deploy - Git + Travis + Heroku
* Travis (gerenciador de tarefas) usado fazer testes automatizados da aplicação antes do deploy
* DONE - by Andre Carvalho

### Importando cursos de parceiros
* Usar JSON para importar cursos de parceiros para a aplicação.
* DONE - by Andre Carvalho

### Ajustes nos testes
* DONE - by Andre Carvalho

### Tradução do README
* Disponibilizar README em Inglês e Português
* DONE - by Andre Carvalho

### API / Rest Framework
* Disponibilizar APIs para uso de serviços
    * Users End Point: "http://127.0.0.1:8000/users/v1" => Acesso só para administrador
    * Categories End Point: "http://127.0.0.1:8000/categories/v1/" => Acesso Livre de leitura.
    * Courses End Point: "http://127.0.0.1:8000/v1/courses/v1/" => Acesso se logado no sistema
    * Teacher End Point: "http://127.0.0.1:8000/v1/teacher/v1/" => Acesso se logado no sistema
* DONE - by Andre Carvalho

### Deploy - Heroku (Cloud PAAS)
* DONE - by Andre Carvalho

### Inclusão no GitHub
* DONE - by Andre Carvalho
  
### Inclusão de static no S3 AWS (Cloud IAAS)
* DONE - by Andre Carvalho

### Migração para Python e Django versões atuais
* DONE - by Andre Carvalho

### Script de carga de dados nas tabelas usando OCR
* DONE - by Andre Carvalho
* Necessidade para migrar para Heroku - postgres

### Incrementando Views de Curso
* No curso foi feito na threadView (permite o mesmo usuário na mesma sessão incrementar varias vezes)
* Agora foi feito para CourseView baseado na sessão do usuário, incrementa baseado apenas em uma nova sessão
* DONE - by Andre Carvalho

### Requisito para inclusão de material
* A inclusão de material via admin só pode conter um tipo de anexo ou um texto incorporado.
* Anteriormente o modulo admin aceitava um anexo e um texto incorporado no mesmo material
e ao acessar este material, o sistema ignorava o anexo mostrando apenas o texto incorporado.
* DONE - by Andre Carvalho

### Fix Insert the course  by WebApp
* DONE - by Andre Carvalho

### Tradução usando Google para português e espanhol
* DONE - by Andre Carvalho

### Correção e Configuração dos parâmetros de envio de email usando decouple
* DONE - by Andre Carvalho
* Situações em que ocorre envio de email:
1. Reinicializar senha de usuário (DONE)
    => Usa no corpo do email um template/HTML pré-formatado
    => Usa como sender do email os dados de usuário fornecidos na página HTML
    => Comando: send_mail_template(subject, template_name, context,[user.email]) / Módulo: Account
2. Usuário solicita contato com o responsável pelo portal (NEW)
    => Usa no corpo do email e como sender do email os dados de usuário fornecidos na página HTML
    => Comando: send_mail_template(subject, template_name, context, [settings.CONTACT_EMAIL]
3. Usuário tem dúvida sobre o conteúdo do curso. (DONE)
    => Usa no corpo do email e como sender do email os dados de usuário fornecidos na página HTML
    => Comando: send_mail_template(subject, template_name, context, [settings.CONTACT_EMAIL] / Módulo: Account
4. Usuário lançou uma propaganda no curso.
    => Usa como sender o usuário da maquina (DONE)
    => Comando: send_mail_template(subject, template_name, context, recipient_list) / Módulo: Account

### Ajuste de templates para tamanho de tela no formato celular
* DONE - by Andre Carvalho

### Attribute Name from Lesson and Material tabels set to UNIQUE  **)
* DONE - by Andre Carvalho

### Attribute Name from Lesson and Material tabels set to UNIQUE  **)
* DONE - by Andre Carvalho

### Inclusão de Professores para os Cursos (Relação **)
* DONE - by Andre Carvalho
* Um professor pode atuar em vários cursos.
* Um curso pode ter vários professores.

### Inclusão de Categorias de Curso (Relação 1*)
* DONE - by Andre Carvalho
* Uma categoria definirá a característica de diversos cursos.
* Exemplos de categorias: Tecnologia da Informação, Gestão de Empresas, Gestão de Projetos...

### Reutilizar painel que esta repetido em dois templates
* DONE - by Andre Carvalho

### Alterar Front End de PURE para Bootstrap
* DONE - by Andre Carvalho

### Segurança - Configuração final do decouple
* DONE - by Andre Carvalho
* Configuração do decouple para incluir no GitHUB.

### Remoção de Biblioteca de Terceiros
* DONE - by Andre Carvalho
* Foi substituída biblioteca de CSS de terceiros por gerar ERRO500 por regra de segurança do browser.  

### Inclusão de Internacionalização
* DONE - by Andre Carvalho
* Escolha o idioma do projeto - Inglês, Espanhol e Português do Brasil

### Framework CSS
* Curso Udemy professor Gileno Alves Santa Cruz Filho - Situação Concluído
* Foi usado o "PURECSS" com a opção de layout "Landing Page"

### Inclusão de ícones no HTML
* Curso Udemy professor Gileno Alves Santa Cruz Filho - Situação Concluído
* Foi adicionado no projeto o CSS de fonte de ícones (font-awesome 3.1.0)

#### Utilizar domínios pré definidos para campos de tabelas (model)
* Curso Udemy professor Gileno Alves Santa Cruz Filho - Situação Concluído
* Verificar o model Enrollment,

### Alterações no modulo administrativo do Django
* Curso Udemy professor Gileno Alves Santa Cruz Filho - Situação Concluído
* Foi criada uma classe USER ACCOUNTS herdada da classe USER do Django.
* Assim o Django deixará de usar seu user auth padrão, e irá usar a classe USER Accounts para:
    <ul>
    <li>fazer acesso ao modulo admin
    <li>criar o super user
    </ul>
* Desta maneira poderemos fazer com que o campo email da tabela de usuário seja único, o que nesta versão do Django permite redundância e também poderemos incluir mais campos de controle de usuário.

### Configuração para envio de email
* Curso Udemy professor Gileno Alves Santa Cruz Filho - Situação Concluído

### Templates Tag
* Curso Udemy professor Gileno Alves Santa Cruz Filho - Situação Concluído
* Foi utilizado na app curses template tag para reutilização de uma classe em mais de um HTML.

### Uso de signals
* Curso Udemy professor Gileno Alves Santa Cruz Filho - Situação Concluído
* O Django oferece um serviço de signals para quando determinados eventos ocorrerem possam ser emitidos avisos, mensagens...
* Ver na app courses => courses.model.py => pos_save / pos_delete
* Ver na app Forum => Thread.model.py => pos_save / pos_delete

### Uso de decorator personalizado
* Curso Udemy professor Gileno Alves Santa Cruz Filho - Situação Concluído
* Criamos um decorator para verificar se o usuário tem permissão para acessar determinados módulos/recursos da app
* Ver decorator.py => def enrollment_required()

### Migração para o servidor de produção usando local_settings.py
* Curso Udemy professor Gileno Alves Santa Cruz Filho - Situação Concluído
* Este método é bem simples para sobrescrever o ambiente local sobre o de produção
* Note que o arquivo local_settings esta no gitignore, logo não será migrado para o servidor o que fará com que o try abaixo falhe e portanto não ocorrerá o sobre inscrição no ambiente de produção.

### ListView paginado com menu lateral
* Curso Udemy professor Gileno Alves Santa Cruz Filho - Situação Concluído
* Para a tela de fórum

### Inclusão das variáveis do request no template
* Curso Udemy professor Gileno Alves Santa Cruz Filho - Situação Concluído
* Algumas recargas de tela alguns dados podem não são atualizados, como por exemplo um novo índice de ordenação de paginação para um determinado objeto, dai é interessante incluir as variáveis do request no contexto nas recargas para atualizá-las.
* Verificar no settings TEMPLATE_CONTET_PROCESSORS

### Inclusão de uma view que é chamada por duas URLS diferentes
* Curso Udemy professor Gileno Alves Santa Cruz Filho - Situação Concluído
* Ver class ForumFilter(ListView)

### Uso de model mommy nos teste
* Curso Udemy professor Gileno Alves Santa Cruz Filho - Situação Concluído
* Utilizado para criar dados automatizados para realização dos testes.
* Visualizar a utilização nos testes dos models.

### Uso de JS Aja JQuery
* Curso Udemy professor Gileno Alves Santa Cruz Filho - Situação Concluído
* Ver controle dos botões pagina thread.html

[Voltar ao topo](#top)

    
<div id='services'/>

##  Lista de Tabelas e funcionalidades do projeto  

| Module | Model | Administration     |  API/Rest   |  Detalhe/Principais informações |
| --- | --- | --- | --- | --- |
|  Accounts   |   User  |  Admin  |  yes    | Ultimo Login, Usuario, Senha, Data Joined | 
|  Courses    |  Categories |  Admin, App |  yes    | Categoria de Cursos |
|  Courses    |  Courses    |  Admin, App |  yes    | Nome Curso |
|  Courses    |  Teachers   |  Admin  |  yes    | Usuario Vinculado |
|  Courses    |  Teacher_course   |  Admin  |  yes    | Vinculo de professor e curso |
|  Courses    |  Lessons    |  Admin  |     |  Lições do curso, Curso Vinculado |
|  Courses    |  Materials  |  Admin, App |     | Material do curso, Lição Vinculada |
|  Courses    |  Enrollments    |  Admin, App |     | Matricula de Usuario ao Curso |
|  Courses    |  Announcement    |  Admin, App |     | Advertisements, Avisos do Curso, Curso Vinculado |
|  Courses    |  Comments   |  Admin, App |     | Discusão (Announcement), Usuario Vinculado |
|  Forum  |  Forum_reply |  Admin, App |     | Respostas do Forum, Pergunta do Forum Vinculada, Usuário Vinculado |
|  Forum  |  Forum_thread  |  Admin  |     | Tópico do Forum, Usuário Vinculado |
|  Courses  |  Courseupload  |  Admin  |     | Carga Json de cursos |


| Module | Func |
| --- | --- |
|  Access |  Logout | 
|  Access |  Login  | 
|  Access |  Change Language    | 
|  Access |  Register new user  | 
|  Contact    |  Speak with us (geral)  | 
|  Courses    |  List advertisement | 
|  Courses    |  Comment advertisement  | 
|  Courses    |  View course's details  | 
|  Courses    |  Make your enrollment   | 
|  Courses    |  Speak with us (courses)    | 
|  Courses    |  Add teacher    | 
|  Forum  |  Forum - View filter by more recently   | 
|  Forum  |  Forum - View filter by more views  | 
|  Forum  |  Forum - View filter by more comments   | 
|  Forum  |  Forum - Add answers    | 
|  Lesson and Materials   |  List Lessons   | 
|  Lesson and Materials   |  Access lesson  | 
|  Lesson and Materials   |  List materials of Lesson   | 
|  Lesson and Materials   |  Access materials of Lesson | 
|  My Panel   |  List my courses    | 
|  My Panel   |  Edit account   | 
|  My Panel   |  Edit password  | 
|  My Panel   |  Access my courses  | 
|  My Panel   |  Cancel enrollment  | 


* Outros cadastros necessários para o projeto disponíveis via módulo Admin 


[Voltar ao topo](#top)


<div id='atention'/>

## Boas Práticas/Cuidado
Além de boas práticas e cuidados apontados em outros projetos, lembrar que: 

1. Quando utilizamos o S3 para armazenar os arquivos estáticos devemos lembrar de incluir a atualização dos mesmos ao processo automático de atualização continua. 


[Voltar ao topo](#top)


<div id='see'/>

## Conheça o projeto

Meet this application on [Heroku] (https://ocps3task.herokuapp.com/).
Meet API of the application on [Heroku] https://ocps3task.herokuapp.com/api/

Perfis de login:
 
| User | Password |
| --- | --- |
| admin | admin |
| user01 | user |
| teacher01 | teacher |


[Voltar ao topo](#top)


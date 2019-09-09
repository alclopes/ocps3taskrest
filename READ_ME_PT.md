<div id='top'/>

# Projeto   

* Este projeto foi iniciado em Python==3.4 e Django==1.8 enquanto fazia curso no site Udemy.
* Apos este curso o projeto foi ampliado com novas bibliotecas, funcionalidades, controles e migrado para versões mais novas do Python e Django.  

* [Proximos Passos](#nextsteps)
* [Atividades Concluídas](#done)
* [Lista de Serviços disponibilizados](#services)
* [Boas Práticas/Cuidados](#atention)
* [Conheça o projeto](#see)


<div id='nextsteps'/>

## Proximos Passos - Plan  

### Evitar sobre carga de servidor
1. Encaminhar emails de inclusão no forum via tarefa assincrona. (substituir oi cron)
2. Apos 3 anos da data de vencimento de um curso propor apagagar os dadios do curso

### Importação de dados referentes a cursos de parceiros 
* Utilizar JSON para migrar dados referentes a cursos de parceiros 
* Aguardando

### Deploy - AWS (Cloud IAAS)
* Aguardando

### Deploy - Puppet/Docker/Travis
* Puppet/Ansible (provisionamento de maquina scripts de preparação do servidor, provisionamento da maquina.
* Docker (Virtualização por containers)rodar a aploicação localmente com a exata configuração do ambiente de produção) 
* Travis (gerenciador de tarefas) util para realizar a Automatização dos testes)
* Aguardando


[Voltar ao topo](#top)


<div id='done'/>


## Atividades Concluidas - Done

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

### Migração para Python e Django versoes atuais
* DONE - by Andre Carvalho

### Script de carga de dados nas tabelas usando OCR
* DONE - by Andre Carvalho
* Necessidade para migrar para Heroku - postgree

### Incrementando Views de Curso
* No curso foi feito na threadView (permite o mesmo usuario na mesma sessão incrementar varias vezes)
* Agora foi feito para CourseView baseado na sessão do usuário, incrementa baseado apenas em uma nova sessão
* DONE - by Andre Carvalho

### Requisito para inclusão de material
* A inclusão de material via admin só pode conter um tipo de anexo ou um texto incorporado.
* Anteriormente o modulo admin aceitava um anexo e um texto incorporado no mesmo material
e ao acessar este material, o sistema ignorava o anexo mostrando apenas o texto incorporado.
* DONE - by Andre Carvalho

### Fix Insert the course  by WebApp
* DONE - by Andre Carvalho

### Tradução using Google para portugues e espanol
* DONE - by Andre Carvalho

### Correção e Configuração dos parametros de envio de email usando decouple
* DONE - by Andre Carvalho
* Situações em que ocorre envio de email:
1. Reinicializar senha de usuário (DONE)
    => Usa no corpo do email um template/html pre-formatado
    => Usa como sender do email os dados de usuário fornecidos na página html
    => Comando: send_mail_template(subject, template_name, context,[user.email]) / Módulo: Account
2. Usuário solicita contato com o responsável pelo portal (NEW)
    => Usa no corpo do email e como sender do email os dados de usuário fornecidos na página html
    => Comando: send_mail_template(subject, template_name, context, [settings.CONTACT_EMAIL]
3. Usuário tem dúvida sobre o conteudo do curso. (DONE)
    => Usa no corpo do email e como sender do email os dados de usuário fornecidos na página html
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
* Uma categoria definirá a caracteristica de diversos cursos.
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
* Foi substituida biblioteca de CSS de terceiros por gerar ERRO500 por regra de segurança do browser.  

### Inclusão de Internacionalização
* DONE - by Andre Carvalho
* Escolha o idioma do projeto - Ingles, Espanhol e Portugues do Brasil

### Framework CSS
* Curso Udemy professor Gileno Alves Santa Cruz Filho - Situação Concluído
* Foi usado o "PURECSS" com a opção de layout "Landing Page"

### Inclusão de icones no HTML
* Curso Udemy professor Gileno Alves Santa Cruz Filho - Situação Concluído
* Foi adicionado no projeto o CSS de fonte de icones (font-awesome 3.1.0)

#### Utilizar dominios pre definidos para campos de tabelas (model)
* Curso Udemy professor Gileno Alves Santa Cruz Filho - Situação Concluído
* Verificar o model Enrollment,

### Alterações no modulo administrativo do Django
* Curso Udemy professor Gileno Alves Santa Cruz Filho - Situação Concluído
* Foi criada uma classe USER ACCOUNTS herdada da classe USER do Django.
* Assim o django deiará de usar seu user auth padrão, e irá usar a classe USER Accounts para:
    <ul>
    <li>fazer acesso ao modulo admin
    <li>criar o super user
    </ul>
* Desta maneira poderemos fazer com que o campo email da tabela de usuário serja unico, o que nesta versão do django permite redundancia e também poderemos incluir mais campos de controle de usuário.

### Configuração para envio de email
* Curso Udemy professor Gileno Alves Santa Cruz Filho - Situação Concluído

### Templates Tag
* Curso Udemy professor Gileno Alves Santa Cruz Filho - Situação Concluído
* Foi utilizado na app curses template tag para reutilização de uma classe em mais de um html.

### Uso de signals
* Curso Udemy professor Gileno Alves Santa Cruz Filho - Situação Concluído
* O Django oferece um serviço de signals para quando determinados eventos ocorerem possam ser emitidos avisos, mensagens...
* Ver na app courses => courses.model.py => pos_save / pos_delete
* Ver na app Forum => Thread.model.py => pos_save / pos_delete

### Uso de decorator personalizado
* Curso Udemy professor Gileno Alves Santa Cruz Filho - Situação Concluído
* Criamos um decorator para verificar se o usuario tem permissão para acessar determinados modulos/recursos da app
* Ver decorator.py => def enrollment_required()

### Migração para o servidor de produção usando local_settings.py
* Curso Udemy professor Gileno Alves Santa Cruz Filho - Situação Concluído
* Este metodo é bem simples para sobreescrever o ambiente local sobre o de produção
* Note que o arquivo local_settings esta no gitignore, logo não será migrado para o servidor o que fará com que o try abaio falhe e portanto não ocorrerá o sobreinscrição no ambiente de produção.

### ListView paginado com menu lateral
* Curso Udemy professor Gileno Alves Santa Cruz Filho - Situação Concluído
* Para a tela de forum

### Inclusão das variaveis do request no template
* Curso Udemy professor Gileno Alves Santa Cruz Filho - Situação Concluído
* Algumas recargas de tela alguns dados podem não são atualizados, como por eemplo um novo indice de ordenação de paginação para um determinado objeto, dai é interessante incluir as variaveis do request no conteto nas recargas para atualiza-las.
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

##  Lista de funcionalidades do projeto  


| Features | Release |
| --- | --- |
| Registro de usuário | xxx |

* Outros cadastros necessários para o projeto disponiveis via módulo Admin 


[Voltar ao topo](#top)


<div id='atention'/>

## Boas Práticas/Cuidado
Além de boas práticas e cuidados apontados em outros projetos, lembrar que: 

1. Quando utilizamos o S3 para armazenar os arquivos estáticos devemos lembrar de incluir a atualização dos mesmos ao processo automatico de atualização continua. 


[Voltar ao topo](#top)


<div id='see'/>

## Conheça o projeto


Meet this application on [Heroku] (https://ocps3task.herokuapp.com/).
Perfis de login:
 
| User | Password |
| --- | --- |
| admin | admin |
| user01 | user |
| teacher01 | teacher |


[Voltar ao topo](#top)
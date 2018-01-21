# desafio_jetbov
Sistema para gestão de fazendas e cabeças de gado

## Deploy

1. Requisitos Necessarios Instalados
> Python 3+ | NodeJs

2. Passos:
```
1. git clone https://github.com/jonasfsilva/desafio_jetbov.git (Clonando Aplicação)

2. virtualenv -p python3 venv  (Criar virtual env)

3. source venv/bin/activate (Ativar virtualenv)

4. cd <pasta do projeto> 

5. pip install -r requirements (Instalando dependencias do python)

6. python manage.py migrate (aplicando migrates)

7. python manage.py set_permissions (Setando permissoes e criando grupo de gestores de fazenda)

8. python manage.py collectstatic (Coletar staticos)

9. cd app_front_end (entrar na pasta onde esta o front_end da aplicacao)

10. npm install bower.json (instalar dependencias do front_end)

11. python manage.py createsuperuser (crie um super usuario para cadastrar inicialmente os gestores e fazendas)

12. python manage.py run_tornado_server (Roda a aplicacao)

13. python manage.py test (Executa tests unitarios)

14. localhost:8801 (accessar aplicacao no browser)
```

3. Detalhes da API:

```
- /api/ (Url para acessar a api e suas urls)
- /api/docs (Url para acessar a documentacao da api, feita com o swagger e ver todas as filtragens possiveis)
- /api/pensagens/?gado__fazenda__cnpj=0000000 (É possivel filtrar relacionamentos na api)
- /api/pensagens/?expand=gado (Exibe os dados do gado que esta relacionado com a pesagem)
```

4. Detalhes do Admin:
```
    - É possivel criar gestores e vincula-los a uma fazenda
    - Quando este gestor fizer login ele podera listar apenas suas fazendas, e pensagens relacionadas a ela

```

5. Melhorias possiveis:
```
    - Criacao de mais testes unitarios para toda api
    - Melhorias nas qustoes de permissoes de accessos e regras de negocio
    - Layout mas otimizado
    - Criacao de comando unica para executar todo deploy
    - Filtragens listagens e permissoes admin

```

6. Tecnologias Utilizadas:
```
    - Django filter : Para fazer filtragens avançadas como na ORM
    
    - Django rest expander : Para mostrar dados de relacionamentos apenas quando
    desejado passando o paramentro expand="<nome do relacionamento>"

    - Django rest swagger : Para documentar todos os metodos e filtragens da API

    - AngularJS | AngularResource para consumir API

    - NodeJS "npm" para instalar bibliotecas Javascript

    - Git Flow para gerenciamento de codigo com git (develop e features e releases)
    
```

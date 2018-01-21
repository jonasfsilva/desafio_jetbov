# desafio_jetbov
Sistema para gestão de fazendas e cabeças de gado

## Deploy

1. Requisitos Necessarios Instalados
> Python 3+ | NodeJs

2. Passos:
```
git clone https://github.com/jonasfsilva/desafio_jetbov.git jetbov (Clonando Aplicação)

virtualenv -p python3 venv  (Criar virtual env)

source venv/bin/activate (Ativar virtualenv)

cd <pasta do projeto> 

pip install -r requirements (Instalando dependencias do python)

python manage.py migrate (aplicando migrates)

python manage.py set_permissions (Setando permissoes e criando grupo de gestores de fazenda)

cd app_front_end (entrar na pasta onde esta o front_end da aplicacao)

npm install bower.json (instalar dependencias do front_end)

python manage.py createsueruser (crie um super usuario para cadastrar inicialmente os gestores e fazendas)

python manage.py run_tornado_server (Roda a aplicacao)

localhost:8801 (accessar aplicacao no browser)
```

3. Detalhes da API:

```
- /api/ (Url para acessar a api e suas urls)
- /api/docs (Url para acessar a documentacao da api, feita com o swagger e ver todas as filtragens possiveis)
- /api/pensagens/?gado__fazenda__cnpj=0000000 (É possivel filtrar relacionamentos na api)
```

4. Detalhes do Admin:
```
- É possivel criar gestores e vincula-los a uma fazenda
- Quando este gestor fizer login ele podera listar apenas suas, fazendas, e pensagens relacionadas a ela

```

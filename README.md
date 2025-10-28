# Django REST API

Uma API REST simples construída com Django e Django REST Framework para gerenciamento de tarefas.

## 🚀 Características

- API RESTful para operações CRUD
- Autenticação e autorização
- Documentação automática da API
- Serialização de dados JSON
- Estrutura modular e escalável

## 📋 Pré-requisitos

- Python 3.8+ 
- pip (gerenciador de pacotes Python)
- Git

## 🛠️ Instalação e Configuração

### Windows

1. **Clone o repositório:**
```cmd
git clone https://github.com/pyladiesthe/django-rest-api.git
cd django-rest-api
```

2. **Crie um ambiente virtual:**
```cmd
python -m venv venv
venv\Scripts\activate
```

3. **Instale as dependências:**
```cmd
pip install -r requirements.txt
```

4. **Execute as migrações do banco de dados:**
```cmd
python manage.py makemigrations
python manage.py migrate
```

5. **Crie um superusuário (opcional):**
```cmd
python manage.py createsuperuser
```

6. **Execute o servidor de desenvolvimento:**
```cmd
python manage.py runserver
```

### Linux/macOS

1. **Clone o repositório:**
```bash
git clone https://github.com/pyladiesthe/django-rest-api.git
cd django-rest-api
```

2. **Crie um ambiente virtual:**
```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

4. **Execute as migrações do banco de dados:**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Crie um superusuário (opcional):**
```bash
python manage.py createsuperuser
```

6. **Execute o servidor de desenvolvimento:**
```bash
python manage.py runserver
```

## 🔧 Comandos Úteis

### Gerenciamento do Ambiente Virtual

**Windows:**
```cmd
# Ativar ambiente virtual
venv\Scripts\activate

# Desativar ambiente virtual
deactivate
```

**Linux/macOS:**
```bash
# Ativar ambiente virtual
source venv/bin/activate

# Desativar ambiente virtual
deactivate
```

### Comandos Django

```bash
# Criar migrações
python manage.py makemigrations

# Aplicar migrações
python manage.py migrate

# Executar testes
python manage.py test

# Coletar arquivos estáticos (produção)
python manage.py collectstatic

# Abrir shell Django
python manage.py shell

# Executar servidor
python manage.py runserver
```

## 📁 Estrutura do Projeto

```
django-rest-api/
├── api/                    # App principal da API
│   ├── migrations/         # Migrações do banco de dados
│   ├── __init__.py
│   ├── admin.py           # Configuração do admin
│   ├── apps.py            # Configuração do app
│   ├── models.py          # Modelos de dados
│   ├── serializers.py     # Serializers da API
│   ├── tests.py           # Testes
│   ├── urls.py            # URLs do app
│   └── views.py           # Views da API
├── lista_tarefas/         # Configurações do projeto
│   ├── __init__.py
│   ├── asgi.py            # Configuração ASGI
│   ├── settings.py        # Configurações principais
│   ├── urls.py            # URLs principais
│   └── wsgi.py            # Configuração WSGI
├── .gitignore             # Arquivos ignorados pelo Git
├── db.sqlite3             # Banco de dados SQLite
├── manage.py              # Script de gerenciamento Django
├── requirements.txt       # Dependências do projeto
└── README.md              # Documentação do projeto
```

## 🌐 Endpoints da API

A API estará disponível em `http://localhost:8000/` após iniciar o servidor.

### Endpoints Principais

- `GET /` - Lista todas as tarefas
- `POST /criar/` - Cria uma nova tarefa
- `PUT /atualiza/{id}/` - Atualiza uma tarefa específica
- `DELETE /deleta/{id}/` - Remove uma tarefa específica
- `GET /concluidas/` - Lista apenas as tarefas concluídas

### Painel Administrativo

Acesse o painel admin em: `http://localhost:8000/admin/`

## 📝 Exemplos de Uso

### Usando PowerShell (Windows)

```powershell
# Listar todas as tarefas
Invoke-RestMethod -Uri "http://localhost:8000/" -Method GET

# Criar uma nova tarefa
$body = @{
    titulo = "Nova Tarefa"
    descricao = "Descrição da tarefa"
    concluida = $false
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:8000/criar/" -Method POST -Body $body -ContentType "application/json"

# Listar tarefas concluídas
Invoke-RestMethod -Uri "http://localhost:8000/concluidas/" -Method GET
```

### Usando curl (Linux/macOS)

```bash
# Listar todas as tarefas
curl -X GET http://localhost:8000/

# Criar uma nova tarefa
curl -X POST http://localhost:8000/criar/ \
  -H "Content-Type: application/json" \
  -d '{"titulo": "Nova Tarefa", "descricao": "Descrição da tarefa", "concluida": false}'

# Atualizar uma tarefa
curl -X PUT http://localhost:8000/atualiza/1/ \
  -H "Content-Type: application/json" \
  -d '{"titulo": "Tarefa Atualizada", "descricao": "Nova descrição", "concluida": true}'

# Deletar uma tarefa
curl -X DELETE http://localhost:8000/deleta/1/

# Listar tarefas concluídas
curl -X GET http://localhost:8000/concluidas/
```

## 🧪 Executando Testes

**Windows:**
```cmd
# Executar todos os testes
python manage.py test

# Executar testes com verbosidade
python manage.py test --verbosity=2

# Executar testes de um app específico
python manage.py test api
```

**Linux/macOS:**
```bash
# Executar todos os testes
python manage.py test

# Executar testes com verbosidade
python manage.py test --verbosity=2

# Executar testes de um app específico
python manage.py test api
```

## 📦 Dependências

As principais dependências estão listadas no arquivo `requirements.txt`:

- Django
- Django REST Framework
- Outras dependências específicas do projeto

## 🤝 Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👩‍💻 Autor

Desenvolvido com ❤️ por [PyLadies The]

---

## 🔍 Solução de Problemas

### Problemas Comuns

**Erro de porta em uso:**
```cmd
# Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

```bash
# Linux/macOS
sudo lsof -t -i tcp:8000 | xargs kill -9
```

**Problemas com migrações:**
```bash
# Resetar migrações (cuidado em produção!)
python manage.py migrate --run-syncdb
```

**Problemas com ambiente virtual:**
```cmd
# Windows - Recriar ambiente virtual
rmdir /s venv
```

```bash
# Linux/macOS - Recriar ambiente virtual
rm -rf venv
```

```bash
# Depois seguir os passos de instalação novamente
```

## 📚 Recursos Úteis

- [Documentação Django](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Python Official Documentation](https://docs.python.org/)
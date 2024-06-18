# FastAPI Atletas

Uma aplicação FastAPI para gerenciar atletas com suporte a paginação, manipulação de exceções e respostas personalizadas.

## Instruções para Configuração e Execução

### Pré-requisitos

- Docker
- Docker Compose

### Configuração

Clone o repositório:

```bash
git clone <URL_DO_SEU_REPOSITORIO>
cd fastapi-atletas
Construir e Executar
Construa e execute a aplicação usando Docker Compose:

bash
Copiar código
docker-compose build
docker-compose up
Acesse a aplicação em http://localhost:8000.

Endpoints
GET /atletas/
Lista todos os atletas com paginação.

Parâmetros de Consulta:

nome: Filtra atletas pelo nome.
cpf: Filtra atletas pelo CPF.
Exemplo de Requisição:

bash
Copiar código
curl -X 'GET' \
  'http://localhost:8000/atletas/?nome=João&cpf=12345678900' \
  -H 'accept: application/json'
POST /atletas/
Cria um novo atleta.

Parâmetros:

nome (str): Nome do atleta.
cpf (str): CPF do atleta.
centro_treinamento (str): Centro de treinamento do atleta.
categoria (str): Categoria do atleta.
Exemplo de Requisição:

bash
Copiar código
curl -X 'POST' \
  'http://localhost:8000/atletas/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "nome": "João",
  "cpf": "12345678900",
  "centro_treinamento": "Centro 1",
  "categoria": "Categoria A"
}'
Tratamento de Erros
IntegrityError: Se tentar criar um atleta com um CPF já existente, a API retornará um erro com a mensagem: "Já existe um atleta cadastrado com o cpf: x" e status code 303.
Paginação
Os resultados dos atletas são paginados utilizando a biblioteca fastapi-pagination. Você pode especificar os parâmetros limit e offset na consulta para controlar a paginação.

Exemplo de Requisição:

bash
Copiar código
curl -X 'GET' \
  'http://localhost:8000/atletas/?limit=10&offset=0' \
  -H 'accept: application/json'
Licença
Este projeto está licenciado sob os termos da licença MIT.

perl
Copiar código

Certifique-se de substituir `<URL_DO_SEU_REPOSITORIO>` pela URL do seu repositório no GitHub.

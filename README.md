# FastAPI Atletas

Uma aplicação FastAPI para gerenciar atletas com suporte a paginação, manipulação de exceções e respostas personalizadas.

## Índice

- [Pré-requisitos](#pré-requisitos)
- [Configuração](#configuração)
- [Construir e Executar](#construir-e-executar)
- [Endpoints](#endpoints)
  - [GET /atletas/](#get-atletas)
  - [POST /atletas/](#post-atletas)
- [Tratamento de Erros](#tratamento-de-erros)
- [Paginação](#paginação)
- [Licença](#licença)

## Pré-requisitos

- Docker
- Docker Compose

## Configuração

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

nome (opcional): Filtra atletas pelo nome.
cpf (opcional): Filtra atletas pelo CPF.
limit (opcional): Limite de resultados por página.
offset (opcional): Ponto de início dos resultados.
Exemplo de Requisição:

bash
Copiar código
curl -X 'GET' \
  'http://localhost:8000/atletas/?nome=João&cpf=12345678900&limit=10&offset=0' \
  -H 'accept: application/json'
POST /atletas/
Cria um novo atleta.

Parâmetros do Corpo da Requisição:

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
IntegrityError: Se tentar criar um atleta com um CPF já existente, a API retornará um erro com a mensagem:
json
Copiar código
{
  "detail": "Já existe um atleta cadastrado com o cpf: x"
}
e status code 303.
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

markdown
Copiar código

### Pontos Principais Melhorados:
1. **Índice**: Adiciona um índice para facilitar a navegação.
2. **Detalhamento**: Expande as seções de configuração e execução.
3. **Endpoints**: Detalha claramente os parâmetros e fornece exemplos de requisições.
4. **Tratamento de Erros**: Explica o tratamento de exceções com exemplos de respostas.
5. **Paginação**: Explica como utilizar a paginação com exemplos.

Certifique-se de substituir `<URL_DO_SEU_REPOSITORIO>` pela URL do seu repositório no GitHub.

# vendas-e-com

Este projeto é um exemplo simples de como usar **Docker Compose** para configurar e executar uma aplicação Python com **Streamlit**.

## Pré-requisitos

Antes de começar, certifique-se de ter instalado em sua máquina:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Como executar o projeto

### 1. Clone este repositório
```bash
git clone https://github.com/seu-usuario/vendas-e-com.git
cd vendas-e-com/docker
```

### 2. Construa e inicie os contêineres
Dentro da pasta docker, você encontrará os arquivos necessários para o ambiente Docker.

Os arquivos mais importantes são:

Dockerfile: Define a imagem Docker para o projeto.
docker-compose.yaml: Configura os serviços do Docker.

Para construir a imagem e iniciar os contêineres, execute o comando abaixo:

```bash
docker-compose up --build
```

Com os contêineres em execução, acesse a aplicação Streamlit no navegador utilizando o endereço:

http://localhost:8501

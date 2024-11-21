# Use uma imagem base com Python
FROM python:3.9-slim

# Definir diretório de trabalho dentro do contêiner
WORKDIR /app

# Copiar as dependências para dentro do contêiner
COPY app/requirements.txt .

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código do projeto
COPY app/ /app/

# Expor a porta do Streamlit
EXPOSE 8501

# Comando para rodar a aplicação Streamlit
CMD ["streamlit", "run", "app.py"]

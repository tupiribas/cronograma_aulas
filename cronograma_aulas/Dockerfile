# Use a imagem base do Python
FROM python:3.12-slim-bullseye

# Instale dependências do sistema
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Defina o diretório de trabalho
WORKDIR /code

# Copie o arquivo de requisitos e instale as dependências
COPY requirements.txt /tmp/
RUN pip install --upgrade pip && pip install -r /tmp/requirements.txt

# Copie o código do projeto
COPY . /code/

# Exponha a porta 8080
EXPOSE 8080

# Comando para rodar a aplicação
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "cronograma_aulas.wsgi:application"]

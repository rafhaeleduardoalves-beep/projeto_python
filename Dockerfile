# Usa uma imagem oficial e leve do Python
FROM python:3.11-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o arquivo de dependências e instala as bibliotecas
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o código da aplicação para o container
COPY . .

# Expõe a porta usada pelo Flask
EXPOSE 5000

# Comando para executar a aplicação
CMD ["python", "app.py"]
# Use a imagem oficial do Python como imagem base
FROM python:3.8-slim

# Defina o diretório de trabalho para o aplicativo
WORKDIR /app

# Copie os arquivos necessários (o seu script Python) para o diretório de trabalho
COPY requirements.txt .
COPY main.py .

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Exponha a porta em que a aplicação FastAPI estará rodando
EXPOSE 8080

# Comando para executar o aplicativo quando o contêiner for iniciado
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]

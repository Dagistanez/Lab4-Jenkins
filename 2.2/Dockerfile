FROM python:3.9-alpine

WORKDIR /app

COPY . .

# Встановлюємо залежності
RUN pip install --no-cache-dir fastapi uvicorn requests pytest httpx
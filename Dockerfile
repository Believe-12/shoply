# Используем официальный образ Python
FROM python:3.12-slim

# Рабочая папка внутри контейнера
WORKDIR /app

# Копируем список зависимостей и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код приложения
COPY app.py .

# Указываем порт веб-приложения
EXPOSE 5000

# Команда запуска приложения
CMD ["python", "app.py"]

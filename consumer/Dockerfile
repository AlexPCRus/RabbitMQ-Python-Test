FROM python:3.9-slim as base
LABEL maintainer="AlexPC (alexmed2000@mail.ru)"

# Сборка зависимостей
ARG BUILD_DEPS="curl"
RUN apt-get update && apt-get install -y $BUILD_DEPS

# Инициализация проекта
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Декларация портов
#EXPOSE 5672:5672

# Установка библиотек
WORKDIR /app
COPY requirements.txt requirements.txt
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt

# Копирование consumer
COPY main.py main.py

# Запуск consumer
CMD ["bash", "-c", "sleep 60 && python3 main.py"]

# Телеграм бот для распознавания речевых сообщений 
С помощью библиотеки speech_recognition бот распознает голосовые сообщения и отвечает текстом :)

## Как установить

#### Настройка переменных окружения:

* Для хранения переменных окружения создаем файл .env:
```
touch .env
```

* Получаем токен после регистрации [бота](https://habr.com/ru/post/262247/) 
```
echo "TGBOT_TOKEN"=<токен бота>" >> .env 
```

### C помощью docker:

1. Скачать образ python:
```bash
docker pull python:3.10
```
2. Упаковать контейнер:
```bash
docker build -t speech-recognition-bot . 
```
3. Запустить контейнер:
```bash
docker run -d -t speech-recognition-bot
```
4. Проверить что контейнер запустился:
```bash
docker ps
```

### Обычным путем:

* Необходимо установить интерпретатор python версии 3.10
* Cкопировать содержимое проекта к себе в рабочую директорию
* Активировать внутри рабочей директории виртуальное окружение:

```
python -m venv [название окружения]
```

* Установить зависимости(необходимые библиотеки):

```
pip install -r pip_requirements.txt
```

### Как пользоваться:

Запускаем файл:
```
python bot.py
```


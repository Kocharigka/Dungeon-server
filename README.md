# Dungeon-server

### Запуск сервера
#### Первый запуск
- Установить [докер](https://www.docker.com/get-started)
- Выполнить
```
docker-compose build
docker-compose up
docker exec dungeon-server_web_1 python manage.py makemigrations
docker exec dungeon-server_web_1 python manage.py migrate
```
#### Последующие запуски
Выполнить
```
docker-compose up
```
#### Выключить - Ctrl + C
##### Сервер стартует на 127.0.0.1:8000
##### Дейли раны по пути /api/v1/daily
##### Если страницу не грузит, то нужно перезапустить сервер по первому сценарию

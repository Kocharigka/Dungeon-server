# Dungeon-server

### Запуск сервера
#### Первый запуск
- Установить [докер](https://www.docker.com/get-started)
- Выполнить
```
docker-compose build
docker-compose up
docker exec server_web_1 python manage.py makemigrations
docker exec server_web_1 python manage.py migrate
```
#### Последующие запуски
Выполнить
```
docker-compose up
```

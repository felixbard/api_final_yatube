# Проект API для Yatube Final
Этот проект иллюстрирует работоспособность REST API с помощью фреймворка Django REST API. Можно получить возможность просматривать посты, комментировать их, получить доступ к группам и подпискам пользователей. 

### Как развернуть проект на локальной машине
Клонировать репозиторий и перейти в него в командной строке:
```
cd api_final_yatube
```
Cоздать и активировать виртуальное окружение:
```
python3 -m venv env
```
```
source env/scripts/activate
```
Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
Выполнить миграции
```
python3 manage.py migrate
```
Запустить проект
```
python3 manage.py runserver
```

### Примеры запросов к API
Получение публикации
```
/api/v1/posts/{id}/
```
Ответ на запрос (код 200)
```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```
Добавление комментария
```
/api/v1/posts/{post_id}/comments/
```
Ответ на запрос (код 201)
```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}
```
Получение информации о сообществе
```
/api/v1/groups/{id}/
```
Ответ на запрос (код 200)
```
{
  "id": 0,
  "title": "string",
  "slug": "^-$",
  "description": "string"
}
```
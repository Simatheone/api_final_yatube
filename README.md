## :hash: API для социальной сети Yatube

## Оглавление
- [API для социальной сети Yatube](#hash-api-для-социальной-сети-yatube)
  - [Используемые технологии](#используемые-технологии)
  - [Структура проекта](#структура-проекта)
  - [Описание проекта](#описание-проекта)
  - [Примеры запросов на API](#примеры-запросов-на-api)
  - [Запуск проекта](#запуск-проекта)

---

### Используемые технологии

:snake: Python 3.8, :desktop_computer: Django 2.2.16, :arrows_clockwise: Django Rest Framework 3.12.4, :card_file_box: SQlite3, :key: Simple JWT, :soap: Django Filters 

---

## Структура проекта
```
yatube_api
 ├── tests/
 ├── yatube_api/
     ├── api/
         ...
         └── templates/
             └── redoc.html
     ├── posts/
         └── ...
     ├── static/
         └── redoc.yaml
     ├── yatube_api/
         └── ...
     └── manage.py
 ├── .gitignore
 ├── README.md
 ├── pytest.ini
 ├── requirements.txt
 └── setup.cfg
```

---

### Описание проекта

Данный проект является API для ранее разработанного проекта [yatube-social-network](https://github.com/simatheone/yatube-social-network).

В проекти используются две роли:
- анонимный пользователь;
- зарегестрированный пользователь.

Полный функционал API доступен только аутентифицированным пользователям. В проекте используется аутентификацию по токену.

<details><summary>Возможности пользователей:</summary>
<p>

| Возможности | Authorized user| Anonymous user |
| :--- | :---: | :---: |
| получить токен                                  | :white_check_mark: | :white_check_mark: |
| просматривать все посты                         | :white_check_mark: | :white_check_mark: |
| просматривать 1 пост                            | :white_check_mark: | :white_check_mark: |
| просматривать группы                            | :white_check_mark: | :white_check_mark: |
| просматривать комментарии                       | :white_check_mark: | :white_check_mark: |
| создавать посты                                 | :white_check_mark: | :x: |
| редактировать и удалять свои посты              | :white_check_mark: | :x: |
| комментировать посты других пользователей       | :white_check_mark: | :x: |
| редактировать и удалять собственные комментарии | :white_check_mark: | :x: |
| подписываться/отписываться на/от авторов        | :white_check_mark: | :x: |

При попытке изменить чужие данные должен возвращается код ответа **403 Forbidden**.

[:top: Вернуться к оглавлению](#оглавление)

</p>
</details>

---

### Примеры запросов на API
<details><summary>Подробнее:</summary>
<p>

В ответ на запросы ```POST```, ```PUT``` и ```PATCH``` API возвращает объект, который был добавлен или изменён.

Пример ```POST``` запроса на получение токена ```.../api/v1/jwt/create/```:

```json
{
  "username": "string",
  "password": "string"
}
```
Пример ответа:
```json
{
  "refresh": "string",
  "access": "string"
}
```

Пример ```GET``` запроса на получение всех постов ```.../api/v1/posts/```:

```json
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```

С другими примерами можно ознакомиться в документации к [API](#запуск-проекта).

[:top: Вернуться к оглавлению](#оглавление)

---

</p>
</details>

### Запуск проекта
Чтобы локально развернуть проект необходимо:

1. Клонировать репозиторий:
```bash
git clone https://github.com/simatheone/yatube-api.git
```

2. Создать виртуальное окружение:
```bash
python3 -m venv venv
```

3. Активировать виртуальное окружение:
```bash
bash/zsh:
source venv/bin/activate

Windows:
venv\Scripts\activate.bat
```

4. Обновить pip и установить зависимости из ```requirements.txt```:
```bash
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```

5. Выполнить миграции и запустить проект:
```bash
python3 manage.py migrate
python3 manage.py runserver
```
6. Ввести в браузере ```http://127.0.0.1:8000/redoc``` и ознакомитсья с более подробной документацией к API.

[:top: Вернуться к оглавлению](#оглавление)

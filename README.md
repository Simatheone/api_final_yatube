### API для социальной сети Yatube:

Чтобы развернуть проект на своей персональной машине необходимо:<br>
Клонировать репозиторий:

```
git clone https://github.com/Simatheone/api_final_yatube.git
```

Перейти в него в командной строке:

```shell
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```shell
source venv/bin/activate
```

Обновить pip с помощью команды:

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
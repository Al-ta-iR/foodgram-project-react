### Описание проекта:

Проект Foodgram позволяет публиковать рецепты, подписываться на 
публикации других пользователей, добавлять понравившиеся рецепты в «Избранное», 
а перед походом в магазин скачивать сводный список продуктов, 
необходимых для приготовления одного или нескольких выбранных блюд.

### Используемые технологии:
Python 3.8.6  
Django 2.2.16  
Django REST Framework 3.12.4  
Djoser 2.1.0  

### Как запустить backend проекта локально:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:Al-ta-iR/foodgram-project-react.git
```

```
cd foodgram-project-react
```

Перейти в папку backend и подготовить файл переменных окружения .env:

```
cd backend
```

скопировать шаблон из файла .env.template:
```
cp .env.template .env
```

заполнить его следующими данными:
```
SECRET_KEY='Django_SECRET_KEY' # секретный ключ Django (укажите свой)
DEBUG=True # default=False
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv .venv
```

```
source .venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Заполнить данными таблицу ингредиентов:

```
python3 manage.py load_csv_data
или
python3 manage.py load_json_data
```

Создать суперпользователя:

```
python3 manage.py createsuperuser
```

Запустить проект:

```
python3 manage.py runserver
```

Теперь по адресу <http://127.0.0.1:8000/admin/> доступна админка проекта,  
а по адресу <http://127.0.0.1:8000/api/> доступны эндпоинты API.


___________________________________
**Author:** Artyom Oleynik

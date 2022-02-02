[![foodgram workflow](https://github.com/Al-ta-iR/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg)](https://github.com/Al-ta-iR/foodgram-project-react/actions/workflows/foodgram_workflow.yml)

### Описание проекта:

Проект Foodgram позволяет публиковать рецепты, подписываться на 
публикации других пользователей, добавлять понравившиеся рецепты в «Избранное», 
а перед походом в магазин скачивать сводный список продуктов, 
необходимых для приготовления одного или нескольких выбранных блюд.

Проект запущен по адресу <http://84.201.162.57/>.

Документация по API: <http://84.201.162.57/api/docs/>.

### Используемые технологии:
Python 3.8.6  
Django 2.2.16  
Django REST Framework 3.12.4  
Djoser 2.1.0  
PostgreSQL 12  
Docker 20.10.7  
Gunicorn 20.0.4  
Nginx 1.19.3

### Как запустить проект локально в docker-контейнерах:

Клонировать репозиторий и перейти в него в командной строке:

```bash
git clone git@github.com:Al-ta-iR/foodgram-project-react.git
```

```bash
cd foodgram-project-react
```

Перейти в папку backend и подготовить файл переменных окружения .env:

```bash
cd backend
```

скопировать шаблон из файла .env.template:
```bash
cp .env.template .env
```

заполнить его следующими данными:
```
SECRET_KEY='Django_SECRET_KEY'  # секретный ключ Django (укажите свой)
DEBUG=True  # default=False
ALLOWED_HOSTS=127.0.0.1, localhost, backend  # перечислить используемые хосты через запятую,
              default='localhost, backend'
DB_ENGINE=django.db.backends.postgresql_psycopg2  # движок БД
POSTGRES_DB=postgres  # имя БД
POSTGRES_USER=postgres  # логин для подключения к БД
POSTGRES_PASSWORD=postgres  # пароль для подключения к БД (установите свой)
DB_HOST=db  # название сервиса (контейнера)
DB_PORT=5432  # порт для подключения к БД
```

Перейти в папку развёртывания инфраструктуры:

```bash
cd ../infra
```

Запустить приложение в docker-контейнерах:

```bash
docker-compose up -d
```

Выполнить миграции и сбор статики:

```bash
docker-compose exec web python3 manage.py migrate
```
    
```bash
docker-compose exec web python3 manage.py collectstatic --no-input
```

Теперь проект доступен по адресу <http://127.0.0.1/>,  
документация по API проекта - по адресу <http://127.0.0.1/api/docs/>.

Заполнить данными таблицу ингредиентов можно командами:

```
docker-compose exec web python3 manage.py load_csv_data
или
docker-compose exec web python3 manage.py load_json_data
```

### Создать суперпользователя

```bash
docker-compose exec web python3 manage.py createsuperuser
```

Теперь по адресу <http://127.0.0.1/admin/> доступна админка проекта.

### Остановить работу всех контейнеров

```bash
docker-compose down
```
___________________________________
**Author:** Artyom Oleynik

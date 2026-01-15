# Django Web Application

A full-featured Django web application with admin panel, ORM, and authentication.

## Features

- Django ORM for database operations
- Admin panel
- User authentication
- Template rendering
- REST API with Django REST Framework

## Project Structure

```
02-django-web-app/
├── myproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── users/
│   ├── __init__.py
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── templates/
│   ├── base.html
│   └── home.html
├── static/
│   ├── css/
│   └── js/
├── manage.py
├── requirements.txt
└── README.md
```

## Installation

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
```

## Running

```bash
python manage.py runserver
```

Access at: http://localhost:8000
Admin panel: http://localhost:8000/admin

## Commands

```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run tests
python manage.py test
```

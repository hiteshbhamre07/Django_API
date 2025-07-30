# Student API - Django REST Framework

This is a simple Django REST API project to perform CRUD operations on a `Student` model using Django REST Framework.

## 🚀 Features

- List all students (`GET`)
- Create a new student (`POST`)
- Uses Django REST Framework (DRF) for fast API development
- Easy to extend with other CRUD operations (Update/Delete)

## 🛠 Technologies Used
Python 3 ,
Django ,
Django REST Framework ,
Sqlite (database) ,


## 📦 Project Structure
📦 student_api_project/               # Main project folder
├── api/                              # Django app for handling Student APIs
│   ├── migrations/                   # Auto-generated DB migration files
│   ├── __init__.py                   # Python package marker
│   ├── admin.py                      # Register models in Django admin
│   ├── apps.py                       # App configuration
│   ├── models.py                     # Database model (Student)
│   ├── serializers.py                # DRF serializer for Student model
│   ├── views.py                      # API views (GET, POST, PUT, DELETE)
│   ├── urls.py                       # App-level URL routes
│
├── student_api_project/             # Django project settings/config
│   ├── __init__.py                   # Python package marker
│   ├── settings.py                   # Global project settings
│   ├── urls.py                       # Root URL configuration
│   └── wsgi.py                       # WSGI entry point for deployment
│
├── manage.py                         # Django command-line utility
└── requirements.txt                  # Project dependencies (optional but recommended)



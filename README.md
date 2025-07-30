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

<pre> 📦 student_api_project/ # Main project folder ├── api/ # Django app for Student APIs │ ├── migrations/ # DB migration files │ ├── __init__.py # Package initializer │ ├── admin.py # Admin interface │ ├── apps.py # App config │ ├── models.py # Student model │ ├── serializers.py # DRF serializer │ ├── views.py # API views (CRUD) │ └── urls.py # App-level URLs │ ├── student_api_project/ # Main project config │ ├── __init__.py # Package initializer │ ├── settings.py # Project settings │ ├── urls.py # Root URLs │ └── wsgi.py # WSGI entry point │ ├── manage.py # Django CLI utility └── requirements.txt # Python dependencies </pre>




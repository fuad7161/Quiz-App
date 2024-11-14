# Quiz-App
# Project setup instruction
- Install python
```
pip install python 
```
- creating virtual environment
```
python -m venv env
```
- activate the virtual environment
```
.\env\Scripts\activate.bat
```
- Install Django and Dependencies
```
pip install django djangorestframework
```
- then start project named Quizebit
```
django-admin startproject quizbit
```
- start an app
```
python manage.py startapp quiz
```
- Setup database and migrations, create and apply migraion
```
python manage.py makemigrations
python manage.py migrate
```
- to run the project
```
python manage.py runserver
```



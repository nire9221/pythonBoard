# pythonBoard

Python IT board project : Python, Django, PostgreSQL

1) setup
- python3 (download VScode or python.org)

- PostgreSQL and pgAdmin (https://www.postgresql.org/)

- Django : after installing python & postgreSQL, open terminal and type below: <br>

  python3 -m venv venv => create virtual machine <br>
  source venv/bin/activate => running virtual machine<br>
  pip install django => install django<br>
  django-admin startproject itBoardProject => create directory for initial set up file<br>
  cd itBoardProject => move to itBoardProject directory<br>
  python3 manage.py startapp itBoardApp<br>

2) register app : setting.py <br>

  INSTALLED_APPS = [<br>
  'django.contrib.admin', <br>
  'django.contrib.auth',<br>
  'django.contrib.contenttypes',<br>
  'django.contrib.sessions',<br>
  'django.contrib.messages',<br>
  'django.contrib.staticfiles',<br>
  'itBoardApp',<br>
  ]<br>

3) set up database :setting.py <br>

  DATABASES = {<br>
    'default': {<br>
    'ENGINE': 'django.db.backends.postgresql_psycopg2',<br>
    'NAME': 'itboard',<br>
    'USER' : 'itboarduser', <br>
    'PASSWORD': 'P@ssw0rd1',    // type your postgres user name & password <br>
    'HOST' :'localhost',<br>
    'PORT' :'',<br>
    }<br>
  }<br>

4) create database in postgreSQL<br>
  type in query tool: CREATE DATABASE itBoard; <br>
  or open pgadmin page -> right click create - database -> type database name -> save <br>

5) migrate database <br>
  itBoardProject> python3 manage.py migrate

6) update project URL<br>
  from django.contrib import admin <br>
  from django.urls import path, include <br>

  urlpatterns = [<br>
  path('admin/', admin.site.urls),<br>
  path('itBoardApp/', include('itBoardApp.urls'))<br>
  ]
  
7) creating view : views.py
  from django.shortcuts import render <br>
  <br>
  def index (request):<br>
    return render(request, 'itBoardApp/index.html') <br>
    
    
8) create another urls.py in itBoardApp folder <br>
 
9) update path : itBoardApp/urls.py
  from django.urls import path
  from . import views

  urlpatterns=[
      path('', views.index, name='index'),
  ]

10) create Base.html : itBoardApp/templates/base.html
`
<!DOCTYPE html>
<html>
    <head>
        <title>IT Board</title>
        <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
        <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
        <link href='//fonts.googleapis.com/css?family=Lobster&subset=latin,latin-ext' rel='stylesheet' type='text/css'>
    </head>
    <body>
        <div class='jumbotron' style="background-color: Navy; color: white;">
            <h1>Tech Reviews</h1>
        </div>
        <nav class="navbar navbar-default">
                <div class="container-fluid">
                <div class="navbar-header">
                <a class="navbar-brand" href="{% url 'index' %}">IT Board</a>
                </div>
                <ul class="nav navbar-nav">
                </ul>
                </div>
                </nav>
        <p>&nbsp;</p>
        <div class="container">
        {% block content %}
        {% endblock content %}
        </div>
    </body>
</html>
`
11) create index.html file : itBoardApp/templates/itBoardApp/index.html
`
{% extends 'base.html' %}
{% block content %}

<h2>IT Board</h2>
<p>Welcome to the site that
    reviews everything tech
</p>
<p>Under construction</p>

{%  endblock %}
`

12) create models : models.py

from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    eventTitle = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    description = models.CharField(max_length=255)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.eventTitle

    class Meta:
        db_table = 'event'
        verbose_name_plural = 'events'

13) migrate database : type --> python3 manage.py makemigrations
14) Register models : admin.py
  
  from django.contrib import admin
  from .models import Event

  admin.site.register(Event)
  
15)create superuser

python3 manage.py createsuperuser
Username (leave blank to use 'erin'): 
Email address: type your email
Password: 
Password (again): 

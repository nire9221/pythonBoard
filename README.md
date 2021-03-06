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
    title = models.CharField(max_length=255)
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


16) import the model : views.py

from .models import Event

17) create the view 

def getEvent(request):
    event_list = Event.objects.all()
    return render(request, 'itBoardApp/event.html', {'event_list': event_list})
    
18) update URL: urls.py 

urlpatterns = [
    path('', views.index, name='index'),
    path('getEvent/', views.getEvent, name='event'),
]

19) create event.html

`
{% extends 'base.html' %}
{% block content %}
<h1>Event</h1>
<table class='table'>
 <tr>
     <th>Title</th>
     <th>Description</th>

 </tr>
 {% for e in event_list %}
   <tr>
       <td>{{ e.title }}</td>
       <td>{{ e.description }}</td>
   </tr>
 {% endfor %}
</table>
{% endblock %}
`

20) update link : base.html
`
<ul class="nav navbar-nav">
  <li><a href="{% url 'event' %}">Event</a></li>
</ul>
`

21) create detail view : views.py

`
from django.shortcuts import render, get_object_or_404
from .models import Event


def index(request):
    return render(request, 'itBoardApp/index.html')


def getEvent(request):
    event_list = Event.objects.all()
    return render(request, 'itBoardApp/event.html', {'event_list': event_list})


def getEventDetail(request, id):
    eventdetail = get_object_or_404(Event, pk=id)

    return render(request, 'itBoardApp/eventDetail.html', {'eventDetail': eventDetail})

`

22) update url : urls.py
`
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getEvent/', views.getEvent, name='event'),
    path('getEventDetail/<int:id>', views.getEventDetail, name='eventDetail'),
]
`

23) update link : event.html
`
{% extends 'base.html' %}
{% block content %}
<h1>Event</h1>
<table class='table'>
 <tr>
     <th>Title</th>
     <th>Description</th>

 </tr>
 {% for e in event_list %}
    <tr>
        <td><a href="{% url 'eventDetail' id=p.id %}">{{ e.title }}</a></td>
        <td> {{e.description }}</td>
    </tr>
 {% endfor %}
</table>
{% endblock %}
`

24)create detail template : eventDetail.html
`
{% extends 'base.html' %}
{% block content %}
<h2>{{ eventdetail.title }}</h2>
<p>Description: {{ eventdetail.description }} </p>
<p>Added by: {{ eventdetail.userId }}</p>
<p>Event Date: {{ eventdetail.date }}</p>
<p>Event time: {{ eventdetail.time }}</p>
<p>URL: {{ eventdetail.url }}</p>
<p>Event location: {{ eventdetail.location }}</p>

{% endblock %}
`

25) create forms.py and add the path 


from django import forms
from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        
        
26) update eventform : views.py 

from .models import Event, EventForm

def newEvent(request):
    form = EventForm
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.save()
            form = EventForm()
    else:
        form = EventForm()
    return render(request, 'clubApp/newevent.html', {'form': form})


27) update path: urls.py

path('newEvent/', views.newEvent, name='newevent'),


28)create newEvent.html
`
{% extends 'base.html' %}
{% block content %}
<h2>Add Event</h2>
<form method='POST' class="post-form">
<table class='table'>
    
        {% csrf_token %}
        {{ form.as_table }}
    

</table>
<button type="submit" class="save btn btn-default">
    Save
</button>
</form>
{% endblock %}
`

29) update link : base.html
`
<ul class="nav navbar-nav">
  <li><a href="{% url 'event' %}">Event</a></li>
  <li><a href="{% url 'newevent' %}">Add Event</a></li>
</ul>
`

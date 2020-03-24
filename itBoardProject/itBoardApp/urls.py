from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('getarticle/', views.getarticle, name='article'),
    path('getarticledetail/<int:id>', views.getarticledetail, name='articledetail'),
    path('newArticle/', views.newArticle, name='newarticle'),
    path('getjobs/', views.getjobs, name='jobs'),
    path('getjobsdetails/<int:id>', views.getjobsdetails, name='jobsdetails'),
    path('newjob/', views.newJob, name='newjob'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
    path('Event/', views.getEvent, name='event'),
    path('eventDetail/<int:id>', views.eventDetail, name='eventDetail'),
    path('AddEvent/', views.newEvent, name='newevent'),
]
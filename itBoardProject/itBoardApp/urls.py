from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('getjobs/', views.getjobs, name='jobs'),
    path('getjobsdetails/<int:id>', views.getjobsdetails, name='jobsdetails'),
    path('newjob/', views.newJob, name='newjob'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]
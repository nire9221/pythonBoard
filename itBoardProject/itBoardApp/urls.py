from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Event/', views.getEvent, name='event'),
    path('eventDetail/<int:id>', views.eventDetail, name='eventDetail'),
    path('AddEvent/', views.newEvent, name='newevent'),
]

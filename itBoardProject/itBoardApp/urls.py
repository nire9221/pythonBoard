from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('getarticle/', views.getarticle, name='article'),
    path('getarticledetail/<int:id>', views.getarticledetail, name='articledetail'),
    path('newArticle/', views.newArticle, name='newarticle'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]
from django.contrib import admin
from .models import Genre, Article, Job, Event

# Register your models here.
admin.site.register(Genre)
admin.site.register(Article)
admin.site.register(Job)
admin.site.register(Event)
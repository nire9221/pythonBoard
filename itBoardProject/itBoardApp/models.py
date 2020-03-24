from django.db import models
from django.contrib.auth.models import User

#---------------------------
# Genre Class
#---------------------------
class Genre(models.Model):
    genrename = models.CharField(max_length=255)
    
    def __str__(self):
        return self.genrename

    class Meta:
        db_table='genre'
        verbose_name_plural='genres'

#---------------------------
# Article Class
#---------------------------
class Article(models.Model):
    articletitle = models.CharField(max_length=255)
    articledescription = models.CharField(max_length=255, null=True, blank=True)
    articleurl = models.CharField(max_length=255, null=True, blank=True)
    articlegenre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    articleuser = models.ForeignKey(User, on_delete=models.CASCADE)
    articledate = models.DateField(null=True)

    def __str__(self):
        return self.articletitle

    class Meta:
        db_table='article'
        verbose_name_plural='articles'

 
#---------------------------
# Job Class
#---------------------------
# Create your models here.
class Job(models.Model):
    JobTitle=models.CharField(max_length=255)
    Employer=models.CharField(max_length=255)
    JobURL=models.URLField(null=True, blank=True)
    User=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    JobLevel=models.CharField(max_length=255)
    Location=models.CharField(max_length=255)
    Availability =models.DateField()
    Description=models.TextField()
    
    def __str__(self):
        return self.JobTitle
    
    class Meta:
        db_table='Job'
        verbose_name_plural='Jobs'
        
#---------------------------
# Event Class
#---------------------------        
class Event(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField(max_length=255)
    url = models.URLField(null=True, blank=True)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'event'
        verbose_name_plural = 'events'

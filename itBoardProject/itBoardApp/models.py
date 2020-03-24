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
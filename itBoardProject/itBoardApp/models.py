from django.db import models
from django.contrib.auth.models import User

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
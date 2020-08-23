from django.db import models

# Create your models here.

class daily_Tasks(models.Model):
    name = models.CharField(max_length=50)

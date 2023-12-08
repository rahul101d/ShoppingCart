from django.db import models


# Create your models here.
class message(models.Model):
    first=models.CharField(max_length=50)
    mail=models.EmailField()
    text=models.CharField(max_length=50)
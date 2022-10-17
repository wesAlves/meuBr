from django.db import models

# Create your models here.
class Posts(models.Model):
    pages = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
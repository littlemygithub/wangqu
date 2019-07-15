from django.db import models

# Create your models here.
class Source(models.Model):
    link = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

class People(models.Model):
    name = models.CharField(max_length=20)
    picture = models.CharField(max_length=100)
    grade = models.CharField(max_length=20)
    blog = models.CharField(max_length=100)
    position = models.CharField(max_length=20)
    introduce = models.CharField(max_length=600)


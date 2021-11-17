from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    mono = models.IntegerField()
    city = models.CharField(max_length=40)
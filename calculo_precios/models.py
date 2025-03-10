from django.db import models

# Create your models here.
class Carne(models.Model):
    nombre = models.CharField(max_length=100)
    peso = models.FloatField(max_length=20)
    precio = models.FloatField(max_length=20)
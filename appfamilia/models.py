from django.db import models

# Create your models here.
class Padre(models.Model):
    nombre= models.CharField(max_length=15)
    apellido=models.CharField(max_length=20)
    celular=models.IntegerField()
    profesion=models.CharField(max_length=20)

class Madre(models.Model):
    nombre= models.CharField(max_length=15)
    apellidocasada=models.CharField(max_length=20)
    apellidosoltera=models.CharField(max_length=20)
    profesion=models.CharField(max_length=20)

class Hijo(models.Model):
    nombre= models.CharField(max_length=15)
    dni=models.IntegerField()

class Hija(models.Model):
    nombre= models.CharField(max_length=15)
    dni=models.IntegerField()
    estudiando=models.CharField(max_length=50)
    
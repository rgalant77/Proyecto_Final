from django.db import models

# Create your models here.

class Snowboard(models.Model):
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=20)
    tamaño = models.IntegerField()
    color = models.CharField(max_length=20)
    #def __str__(self):
        #return f"{self.id} | marca: {self.marca} | modelo: {self.modelo} | tamaño: {self.tamaño} | color: {self.color} "

class Ski(models.Model):
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=20)
    tamaño = models.IntegerField()
    color = models.CharField(max_length=20)
    #def __str__(self):
        #return f"{self.id} | marca: {self.marca} | modelo: {self.modelo} | tamaño: {self.tamaño} | color: {self.color} "
   
class Antiparras(models.Model):
    marca = models.CharField(max_length=30)
    talle = models.IntegerField()
    modelo = models.CharField(max_length=40)
    color = models.CharField(max_length=20)
    #def __str__(self):
        #return f"{self.id} | marca: {self.marca} | talle: {self.talle} | modelo: {self.modelo} | color: {self.color} " 
    

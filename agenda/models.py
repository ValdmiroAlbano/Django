from django.db import models

# Create your models here.

class Categoria(models.Model):
    name = models.CharField(max_length = 255, unique = True)

class Eventos(models.Model):
    name = models.CharField(max_length = 255)
    categoria = models.ForeignKey(Categoria, on_delete = models.SET_NULL, null = True)
    local = models.CharField(max_length = 255)
    link = models.CharField(max_length = 255)

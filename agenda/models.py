from django.db import models

# Create your models here.

class Categoria(models.Model):
    name = models.CharField(max_length = 255, unique = True)

    def __str__(self):
        return f"{self.name} <{self.id}>"

class Eventos(models.Model):

    def __str__(self):
        return  f"\n{self.name}\n{self.categoria.name}\n{self.local}"

    name = models.CharField(max_length = 255)
    categoria = models.ForeignKey(Categoria, on_delete = models.SET_NULL, null = True)
    local = models.CharField(max_length = 255)
    link = models.CharField(max_length = 255)
    data = models.DateField(null=True)
    participantes = models.IntegerField(default=0)

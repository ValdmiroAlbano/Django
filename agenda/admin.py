from django.contrib import admin

from agenda.models import Categoria, Eventos

# Register your models here.
admin.site.register(Eventos)
admin.site.register(Categoria)
from django.urls import path

from agenda.views import listar_eventos, exibir_evento

urlpatterns = [
    path("", listar_eventos, name = "listar_eventos_raiz"),
    path("eventos", listar_eventos, name = "listar_eventos"),
    path("evento/<int:id>/", exibir_evento, name = "exibir_evento")
]
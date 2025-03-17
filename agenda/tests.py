from datetime import date

from django.test import TestCase, Client
from agenda.models import Categoria, Eventos


# Create your tests here.
class TestPaginaInicial(TestCase):
    def test_lista_eventos(self):
        client = Client()
        response = client.get("/")
        #self.assertTemplateUsed(response, "agenda/exibir_eventos.html")
        self.assertContains(response, "<th>Nome</th>")

class TestListagemEventos(TestCase):
    def test_evento_com_data(self):
        categoria = Categoria()
        categoria.name = "Backend"
        categoria.save()

        evento = Eventos()
        evento.name = "Aula python"
        evento.categoria = categoria
        evento.local = "Luanda"
        evento.data = date.today()
        evento.save()

        response = client = Client()
        self.assertContains(response, "Aula python")
        self.assertEqual(list(response.context["eventos"]), [evento])

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from agenda.models import Eventos

def listar_eventos(request):
    evento = Eventos.objects.all()
    return render(
        request=request,
        context={"eventos": evento},
        template_name="agenda/listar_eventos.html"
    )

def exibir_evento(request, id):
    evento = get_object_or_404(Eventos, id=id)
    return render(
        request=request,
        context={"evento": evento},
        template_name="agenda/exibir_evento.html"
    )
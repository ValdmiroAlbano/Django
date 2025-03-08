from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def exibir_eventos(request):
    evento = {
        "nome" : "Nossa App1",
        "categoria": "Apenas 1",
        "local": "Luanda"
    }

    return HttpResponse (
        f"""
        <h1>Evento: {evento["nome"]}</h1>
        <p>Categoria: {evento["categoria"]}</p>
        <p>Local: {evento["local"]}</p>
        """
    )
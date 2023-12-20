from django.shortcuts import render
from apps.noticias.models import Noticia

def Home(request):
    # filtrar las ultimas 3 noticias
    ultimas_noticias = Noticia.objects.order_by('-fecha_publicacion')[:3]

    contexto = {
        'ultimas_noticias': ultimas_noticias
    }
    return render(request, 'home.html', contexto)

def Nosotros(request):
    return render(request, 'nosotros.html')
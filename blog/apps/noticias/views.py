from django.shortcuts import render
from .models import Noticia, Categoria

def ListarNoticias(request):
    contexto = {}
    id_categoria = request.GET.get("id", None)
    antiguedad = request.GET.get("antiguedad", None)
    orden = request.GET.get("orden", None)

    n = Noticia.objects.all()

    if id_categoria:
        n = n.filter(categoria_noticia=id_categoria)

    if antiguedad == "asc":
        n = n.order_by('fecha_publicacion')
    elif antiguedad == "desc":
        n = n.order_by('-fecha_publicacion')

    if orden == "asc":
        n = n.order_by('titulo')
    elif orden == "desc":
        n = n.order_by('-titulo')

    contexto = {
        'noticias': n,
        'categorias': Categoria.objects.all(),
    }

    return render(request, 'noticias/listar.html', contexto)



def DetalleNoticia(request, pk):
    contexto = {}

    n = Noticia.objects.get(pk = pk) # SELECT * FROM NOTICIAS WHERE id = 1
    contexto['noticias'] = n
    
    return render (request, 'noticias/detalle.html', contexto)
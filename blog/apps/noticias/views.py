from django.shortcuts import render
from .models import Noticia, Categoria

# Create your views here.
def ListarNoticias(request):
    contexto = {}
    id_categoria = request.GET.get("id", None)

    if id_categoria:
        n = Noticia.objects.filter(categoria_noticia = id_categoria)
    else:
        n = Noticia.objects.all() # SELECT * FROM NOTICIAS
    
    # filtrar por antiguedad asc
    antiguedad_asc = request.GET.get("antiguedad_asc")
    if antiguedad_asc:
        n = Noticia.objects.all().order_by('fecha_publicacion') #ordena por fecha

    # filtrar por antiguedad desc
    antiguedad_desc = request.GET.get("antiguedad_desc")
    if antiguedad_desc:
        n = Noticia.objects.all().order_by('-fecha_publicacion') #ordena por fecha

    # filtrar por orden alfabetico asc
    orden_asc = request.GET.get("orden_asc")
    if orden_asc:
        n = Noticia.objects.all().order_by('titulo') #ordena por titulo

    # filtrar por orden alfabetico desc
    orden_desc = request.GET.get("orden_desc")
    if orden_desc:
        n = Noticia.objects.all().order_by('-titulo') #ordena por titulo

    
    cat = Categoria.objects.all().order_by('nombre') #ordena por nombre
    contexto['noticias'] = n
    contexto['categorias'] = cat
    
    return render (request, 'noticias/listar.html', contexto)


def DetalleNoticia(request, pk):
    contexto = {}

    n = Noticia.objects.get(pk = pk) # SELECT * FROM NOTICIAS WHERE id = 1
    contexto['noticias'] = n
    
    return render (request, 'noticias/detalle.html', contexto)
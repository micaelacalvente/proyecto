from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Noticia, Categoria
from .forms import NoticiaForm
from django.contrib.auth.decorators import login_required

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

    #BORRAR NOTICIA
    if request.method == 'POST' and 'delete_noticia' in request.POST:
        n.delete()
        return redirect('noticias:listar')
    
    return render (request, 'noticias/detalle.html', contexto)

@login_required
def AddNoticia(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST or None, request.FILES) ##Request files es para las imagenes

        if form.is_valid():
            noticia = form.save(commit=False)
            noticia.autor = request.user
            form.save()
            return redirect('home')
    else:
        form = NoticiaForm()
    
    return render (request, 'noticias/addNoticia.html', {'form':form})
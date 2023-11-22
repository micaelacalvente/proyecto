from django.shortcuts import render

# Create your views here.
def ListarNoticias(request):
    return render (request, 'noticias/listar.html')
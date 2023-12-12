from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'noticias'

urlpatterns = [
    path('', views.ListarNoticias, name='listar'),
    path('detalle/<int:pk>', views.DetalleNoticia, name='detalle'),
    path('addNoticia', views.AddNoticia, name='addnoticia'),
    path('noticias/<int:pk>/edit/', views.EditarNoticia, name='edit_noticia'),
    path('comentario/add/<int:noticia_id>', views.AddComentario, name= 'add_comentario'),
    path('comentario/delete/<int:comentario_id>', views.BorrarComentario, name= 'delete_comentario'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
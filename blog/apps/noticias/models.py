from django.db import models
from apps.usuarios.models import Usuario

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    

class Noticia(models.Model):
    titulo = models.CharField(max_length=50) # = VARCHAR | max_length longitud max
    resumen = models.CharField(max_length=200, null=True)
    contenido = models.TextField()
    #imagen requiere la libreria pillow
    imagenes = models.ImageField(upload_to='noticias')
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    categoria_noticia = models.ForeignKey(Categoria, on_delete= models.SET_NULL, null=True) # models.CASCADE
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=Usuario.objects.get(is_superuser=True).pk)

    def __str__(self):
        return self.titulo
    
class Comentario(models.Model):
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE, related_name='comentarios')
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario = models.CharField(max_length=50)

    def __str__(self):
        return self.contenido
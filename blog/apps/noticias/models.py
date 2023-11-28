from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    

class Noticia(models.Model):
    titulo = models.CharField(max_length=50) # = VARCHAR | max_length longitud max
    contenido = models.TextField()
    #imagen requiere la libreria pillow
    imagenes = models.ImageField(upload_to='noticias')
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    categoria_noticia = models.ForeignKey(Categoria, on_delete= models.SET_NULL, null=True)

    def __str__(self):
        return self.titulo
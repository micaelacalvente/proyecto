from django import forms
from .models import Noticia

class NoticiaForm(forms.ModelForm):

    class Meta:
        model = Noticia
        fields = [
            'titulo',
            'resumen',
            'contenido',
            'imagenes',
            'categoria_noticia',
        ]
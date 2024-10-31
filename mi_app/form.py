from django import forms
from .models import Lista

class Lista_Playlist(forms.ModelForm):
    class Meta:
        model = Lista
        fields = ['nombre_lista', 'descripcion_lista']



        
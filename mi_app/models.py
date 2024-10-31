from django.db import models
from django.core.exceptions import ValidationError
from PIL import Image as PILImage
import os

# Función para validar el tamaño del archivo de audio
def validar_audio(file):
    max_size = 5 * 1024 * 1024  # 5 MB
    if file.size > max_size:
        raise ValidationError("El tamaño del archivo de audio no puede ser mayor a 5 MB.")

# Modelo para las Canciones
class Cancion(models.Model):
    id_cancion = models.AutoField(primary_key=True)
    nombre_cancion = models.CharField(max_length=100)
    nombre_autor = models.CharField(max_length=100)
    audio = models.FileField(upload_to='static/archivos_proyecto/audios/', blank=True, validators=[validar_audio])
    imagen = models.ImageField(upload_to='static/archivos_proyecto/imagenes/', blank=True)

    def save(self, *args, **kwargs):
        # Redimensionar imagen si está presente
        if self.imagen:
            img = PILImage.open(self.imagen)
            img.thumbnail((800, 800))  # Redimensionar a un tamaño máximo de 800x800
            img.save(self.imagen.path)  # Guardar la imagen redimensionada

        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre_cancion  # Representación legible de Cancion

# Modelo para el Catálogo
class Catalogo(models.Model):
    id_catalogo = models.AutoField(primary_key=True)
    cancion = models.ForeignKey(Cancion, on_delete=models.CASCADE, related_name='catalogos')

    def __str__(self):
        return f"Catalogo de {self.cancion.nombre_cancion}"  # Mejor descripción

# Modelo para las Listas
class Lista(models.Model):
    id_lista = models.AutoField(primary_key=True)
    nombre_lista = models.CharField(max_length=100)
    descripcion_lista = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_lista  # Representación legible de Lista

# Modelo para la PreLista
class PreLista(models.Model):
    id_prelista = models.AutoField(primary_key=True)
    catalogo = models.ForeignKey(Catalogo, on_delete=models.CASCADE, related_name='prelistas')
    lista = models.ForeignKey(Lista, on_delete=models.CASCADE, related_name='prelistas')

    def __str__(self):
        return f"{self.catalogo.cancion.nombre_cancion} en {self.lista.nombre_lista}"  # Claridad

# Modelo para colas
class Cola(models.Model):
    id_cola = models.AutoField(primary_key=True)
    catalogo = models.ForeignKey(Catalogo, on_delete=models.CASCADE, related_name='colas')
    lista = models.ForeignKey(Lista, on_delete=models.CASCADE, related_name='colas')

    def __str__(self):
        return f"Canción en cola de la lista {self.lista.nombre_lista}: {self.catalogo.cancion.nombre_cancion}"  # Claridad

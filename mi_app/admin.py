from django.contrib import admin

from .models import Cancion

from .models import Catalogo

admin.site.register(Cancion)
admin.site.register(Catalogo)
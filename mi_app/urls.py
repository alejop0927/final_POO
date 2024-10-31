from django.urls import path
from . import views

urlpatterns = [
    path('crear_lista/', views.crear_lista_playlist, name='crear_lista_playlist'),
    path('ver_catalogo/', views.ver_catalogo, name='ver_catalogo'),
    path('lista_de_playlist/', views.lista_de_playlist, name='lista_de_playlist'),
    path('agregar_cancion/<int:id_lista>/', views.set_agregar_cancion_lista, name='set_agregar_cancion_lista'),
    path('agregar_cancion/', views.agregar_cancion_lista, name='agregar_cancion_lista'),
    path('ver_canciones/<int:lista_id>/', views.ver_canciones_lista, name='ver_canciones_lista'),  # URL ajustada
    path('eliminar_cancion/<int:prelista_id>/', views.eliminar_cancion_lista, name='eliminar_cancion_lista'),
    path('eliminar_lista/<int:lista_id>/', views.set_eliminar_lista, name='set_eliminar_lista'),
    path('eliminar_lista/', views.eliminar_lista, name='eliminar_lista'),
    
]

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Catalogo, Lista, PreLista
from .form import Lista_Playlist
from .exceptions import CancionNoEncontradaError, ListaNoEncontradaError, CancionNoAgregadaError

def ver_catalogo(request):
    """Vista para mostrar el catálogo de canciones."""
    catalogo = Catalogo.objects.select_related('cancion').all()
    print(f"Número de catálogos: {catalogo.count()}")  # Mensaje de depuración
    context = {
        'catalogo': catalogo
    }
    return render(request, 'mi_app/ver_catalogo.html', context)

def crear_lista_playlist(request):
    """Vista para crear una nueva lista de reproducción."""
    if request.method == 'POST':
        form = Lista_Playlist(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Lista de reproducción creada con éxito.')
            return redirect('lista_de_playlist')
        else:
            messages.error(request, 'Error al crear la lista de reproducción. Por favor, revisa los datos.')

    form = Lista_Playlist()
    return render(request, 'mi_app/crear_lista.html', {'form': form})

def lista_de_playlist(request):
    """Vista para mostrar todas las listas de reproducción."""
    listas = Lista.objects.all()
    return render(request, 'mi_app/ver_listas.html', {'listas': listas})

def set_agregar_cancion_lista(request, id_lista):
    """Almacena el ID de la lista en la sesión para agregar canciones."""
    request.session['id_lista'] = id_lista
    return redirect('agregar_cancion_lista')

def agregar_cancion_lista(request):
    """Vista para agregar canciones a una lista de reproducción específica."""
    id_lista = request.session.get('id_lista')

    try:
        lista = get_object_or_404(Lista, id_lista=id_lista)
    except Lista.DoesNotExist:
        raise ListaNoEncontradaError(f'Lista con ID {id_lista} no encontrada.')

    if request.method == 'POST':
        cancion_id = request.POST.get('cancion_id')
        
        try:
            cancion = get_object_or_404(Catalogo, id_catalogo=cancion_id)
        except Catalogo.DoesNotExist:
            raise CancionNoEncontradaError(f'Canción con ID {cancion_id} no encontrada.')

        try:
            PreLista.objects.create(catalogo=cancion, lista=lista)
            messages.success(request, f'Canción "{cancion.cancion.nombre_cancion}" agregada a la lista "{lista.nombre_lista}".')
        except Exception as e:
            raise CancionNoAgregadaError(f'No se pudo agregar la canción: {str(e)}')

        return redirect('lista_de_playlist')

    catalogo = Catalogo.objects.all()
    return render(request, 'mi_app/agregar_cancion.html', {'lista': lista, 'catalogo': catalogo})

def ver_canciones_lista(request, lista_id):
    """Vista para mostrar las canciones de una lista de reproducción específica."""
    try:
        lista = get_object_or_404(Lista, id_lista=lista_id)
    except Lista.DoesNotExist:
        raise ListaNoEncontradaError(f'Lista con ID {lista_id} no encontrada.')

    canciones = PreLista.objects.filter(lista=lista)
    return render(request, 'mi_app/ver_canciones_lista.html', {'lista': lista, 'canciones': canciones})

def eliminar_cancion_lista(request, prelista_id):
    """Elimina una canción de una lista de reproducción."""
    try:
        prelista = get_object_or_404(PreLista, id_prelista=prelista_id)
    except PreLista.DoesNotExist:
        messages.error(request, 'Canción no encontrada para eliminar.')
        return redirect('lista_de_playlist')

    lista_id = prelista.lista.id_lista
    prelista.delete()
    messages.success(request, 'Canción eliminada de la lista con éxito.')
    return redirect('ver_canciones_lista', lista_id=lista_id)

def set_eliminar_lista(request, lista_id):
    """Almacena el ID de la lista a eliminar en la sesión."""
    request.session['lista_id'] = lista_id
    return redirect('eliminar_lista')

def eliminar_lista(request):
    """Elimina una lista de reproducción."""
    lista_id = request.session.get('lista_id')

    try:
        lista = get_object_or_404(Lista, id_lista=lista_id)
        lista.delete()
        messages.success(request, 'Lista de reproducción eliminada con éxito.')
    except Lista.DoesNotExist:
        messages.error(request, 'Lista no encontrada para eliminar.')

    return redirect('lista_de_playlist')

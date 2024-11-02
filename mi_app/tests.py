from django.test import TestCase
from django.urls import reverse
from .models import Cancion, Catalogo, Lista, PreLista

class PlaylistViewsTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Crear una canción para usar en las pruebas
        cls.cancion = Cancion.objects.create(
            nombre_cancion="I'm Good (Blue)",
            nombre_autor="David Guetta & Bebe Rexha",
            audio="MEDIA/aUDIO_CANCIONES/David Guetta & Bebe Rexha - I'm Good (Blue) [Official Music Video].MP3",
            imagen="MEDIA/IMAGENES_CANCIONES/David Guetta & Bebe Rexha - I'm Good (Blue) [Official Music Video].JPG"
        )
        cls.catalogo = Catalogo.objects.create(cancion=cls.cancion)
        cls.lista = Lista.objects.create(nombre_lista="Mi Lista", descripcion_lista="Lista de prueba")

    def test_ver_catalogo(self):
        """Prueba que la vista ver_catalogo retorna la respuesta correcta."""
        response = self.client.get(reverse('ver_catalogo'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mi_app/ver_catalogo.html')
        self.assertContains(response, self.cancion.nombre_cancion)

    def test_crear_lista_playlist(self):
        """Prueba la creación de una nueva lista de reproducción."""
        response = self.client.post(reverse('crear_lista_playlist'), {
            'nombre_lista': 'Lista Nueva',
            'descripcion_lista': 'Descripción de lista nueva'
        })
        self.assertEqual(response.status_code, 302)  # Redirige después de crear
        self.assertTrue(Lista.objects.filter(nombre_lista='Lista Nueva').exists())

    def test_agregar_cancion_lista(self):
        """Prueba agregar una canción a una lista."""
        self.client.session['id_lista'] = self.lista.id_lista
        response = self.client.post(reverse('agregar_cancion_lista'), {
            'cancion_id': self.catalogo.id_catalogo
        })
        self.assertEqual(response.status_code, 302)  # Redirige después de agregar
        self.assertTrue(PreLista.objects.filter(catalogo=self.catalogo, lista=self.lista).exists())

    def test_ver_canciones_lista(self):
        """Prueba ver las canciones en una lista de reproducción."""
        PreLista.objects.create(catalogo=self.catalogo, lista=self.lista)
        response = self.client.get(reverse('ver_canciones_lista', args=[self.lista.id_lista]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.cancion.nombre_cancion)

    def test_eliminar_cancion_lista(self):
        """Prueba eliminar una canción de la lista de reproducción."""
        prelista = PreLista.objects.create(catalogo=self.catalogo, lista=self.lista)
        response = self.client.post(reverse('eliminar_cancion_lista', args=[prelista.id_prelista]))
        self.assertEqual(response.status_code, 302)  # Redirige después de eliminar
        self.assertFalse(PreLista.objects.filter(id_prelista=prelista.id_prelista).exists())

    def test_agregar_cancion_inexistente_lista(self):
        """Prueba que no se pueda agregar una canción inexistente."""
        self.client.session['id_lista'] = self.lista.id_lista
        response = self.client.post(reverse('agregar_cancion_lista'), {
            'cancion_id': 99999  # ID que no existe
        })
        self.assertEqual(response.status_code, 404)  # O el código que corresponda a tu lógica

    def test_eliminar_cancion_inexistente_lista(self):
        """Prueba que no se pueda eliminar una canción inexistente."""
        response = self.client.post(reverse('eliminar_cancion_lista', args=[99999]))  # ID que no existe
        self.assertEqual(response.status_code, 404)  # O el código que corresponda a tu lógica

Proyecto de aula
Entrega 1


Software Reproductor de Música


Alejandro Peña Restrepo




Algoritmos y programación orientada a objetos
Gabriel Jaime Thomas Uribe


Universidad de Medellín


03/09/2024

















Descripción del problema
Se va a desarrollar un software en el cual se nos permita administrar múltiples canciones y de esta poder hacer playlists además de crear álbumes y escuchar música, por otra parte, podemos buscar canciones y agregarlas a las playlists.
Además, el enfoque esta para todo tipo de personas que quieran escuchar buena música con tan solo unos clics y la forma en como está constituido el software es de una manera ágil y versátil con el fin de que a los usuarios que la usen se les sea fácil y accesible a los múltiples contenidos. 

Análisis del problema
Para los requisitos funcionales se tendrá en cuenta la descripción del problema, abarcando múltiples aspectos para que el aplicativo quede completa y compacta al momento que un usuario la use. Además, se realizará la implementación de cada requerimiento funcional del reproductor de música los cuales se explicaran detalladamente a continuación.
Requisitos funcionales
Nombre	R1 Crear lista de Reproducción 
Resumen	El sistema debe permitir a los usuarios crear listas de reproducción
Entradas	•	Descripción
•	Nombre de la lista
Resultado	•	La lista de reproducción es creada con éxito en el sistema

Pasos	Métodos	Responsabilidades
Crear lista de Reproducción	__str__(id,nombre, descripción)	Lista
Almacenar lista de reproducción	crear_lista_playlist
	Lista

Nombre	R2  Visualizar lista de reproducción  
Resumen	El sistema debe permitir al usuario visualizar las listas que tenga creadas 
Entradas	•	Id lista reproduccion
Resultado	•	El sistema debe permitir visualizar con éxito las listas que se tengan disponibles o previamente creadas

Pasos	Métodos	Responsabilidades
Verificar que este creada la lista	lista_de_playlist(request)
	Lista
Visualizar lista de reproducción	return render(request, 'mi_app/ver_listas.html', {'listas': listas})
	Lista

Nombre	R3 Agregar canción a una lista de reproducción
Resumen	El sistema permite al usuario el ingreso de canciones a la playlist que se este haciendo
Entradas	•	Id canción 
Resultado	•	La canción queda agregada con éxito a la lista

Pasos	Métodos	Responsabilidades
Verificar si la lista esta creada	 agregar_cancion_lista(request)
	Prelista 
Agregar canción lista	 agregar_cancion_lista(request)
	Prelista 

Nombre	R4 Eliminar canción de la lista
Resumen	El sistema debe permitir eliminar una canción de la lista de reproducción
Entradas	•	Id canción
Resultado	•	El sistema elimina con éxito la canción de la lista

Pasos	Métodos	Responsabilidades
Ver la lista creada	Ver_lista()	Prelista
Verificar que la canción este  en la 	eliminar_cancion_lista(request, prelista_id)
	Prelista 
Eliminar canción de la lista	prelista.delete()
	Prelista




Nombre	R5 visualizar canciones de una lista de reproducción 
Resumen	El sistema debe permitir visualizar las canciones que conforman la lista de reproducción creada 
Entradas	•	Id Lista
Resultado	•	las canciones son visibles en las listas de reproducción

Pasos	Métodos	Responsabilidades
Mostrar la lista	lista_de_playlist(request)	Lista 
Mostrar componentes almacenados en lista	ver_canciones_lista(request, lista_id)
	Prelista


Nombre	R6 Eliminar una lista de reproduccion
Resumen	El sistema debe permitir visualizar las listas y poder eliminar cualquiera de que desee eliminar
Entradas	•	Id Lista
Resultado	•	Lista eliminada

Pasos	Métodos	Responsabilidades
Mostrar la lista	lista_de_playlist(request)	Lista 
Mostrar componentes almacenados en lista	eliminar_lista(request)
	Lista





Nombre	R7 Reproducir siguiente o anterior canción 
Resumen	El sistema debe permitir reproducir la siguiente o anterior canción en la lista de reproducción, gestionando el orden y reproducción mediante JavaScript en el navegador.
Entradas	•	Id de la canción (a través del dataset en el HTML)
•	Nombre de la canción (a través del contenido del li en el HTML)
•	Artista de la canción (implícito en el nombre de la canción o no especificado explícitamente en el código proporcionado)
•	Lista de canciones (representada como elementos li en el ul con el id lista-canciones)
Resultado	•	El sistema reproduce la siguiente canción o la anterior canción en la lista de reproducción.

Pasos	Métodos	Responsabilidades
Recopilar todas las canciones	Playlist.collectSongs()	Playlist
Cargar y reproducir la canción actual	Player.loadAndPlaySong(index)	Player
Reproducir la canción anterior	Player.playPrevious()	Player
Reproducir la canción siguiente	Player.playNext()	Player
Mostrar mensajes de alerta si no hay más canciones	Player.alertNoMoreSongs(message)	Player 



Nombre	R8 Control de volumen de la música 
Resumen	El sistema debe permitir al usuario subir y bajar el volumen del reproductor mediante botones. El cambio de volumen debe reflejarse en tiempo real.
Entradas	•	Subir volumen
•	Bajar volumen
Resultado	•	El sistema ajusta el volumen del reproductor de audio según el botón presionado (subir o bajar volumen).

Pasos	Métodos	Responsabilidades
Subir volumen	Player.increaseVolume()	Player
Bajar volumen	Player.decreaseVolume()	Player


Nombre	R9 Descarga de canciones 
Resumen	El sistema debe permitir al usuario descargar la canción que se está reproduciendo actualmente.
Entradas	•	URL de la canción actual (a través del dataset en el HTML).
Resultado	•	El sistema descarga la canción actual al dispositivo del usuario.

Pasos	Métodos	Responsabilidades
Descargar la canción actual	Player.dowloadCurrentSong()	Player


Nombre	R10 Ajuste de Velocidad de Reproducción
Resumen	El sistema debe permitir al usuario ajustar la velocidad de reproducción de la canción que se está reproduciendo actualmente.
Entradas	•	Factor de velocidad (e.g., 1.0 para normal, 1.5 para 1.5x más rápido, etc.)
Resultado	•	La velocidad de reproducción de la canción cambia según el factor de velocidad seleccionado.

Pasos	Métodos	Responsabilidades
Ajustar la velocidad de reproducción	Player.setPlaybackRate(rate)	Player


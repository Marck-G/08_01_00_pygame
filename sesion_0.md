# Sesión 0: Fundamentos de Pygame

**Objetivo:** Introducir Pygame y preparar el entorno de desarrollo para la creación de un juego 2D.

## Contenidos

* Instalación de Pygame
* Creación de la ventana principal del juego
* Loop principal y control de FPS
* Renderizado de un color de fondo

## Detalles

1. **Instalación de Pygame:**

   * Usar `pip install pygame` para instalar la librería.

2. **Crear ventana básica:**

   * Inicializar Pygame con `pygame.init()`.
   * Configurar tamaño de ventana con `pygame.display.set_mode((WIDTH, HEIGHT))`.
   * Poner título con `pygame.display.set_caption("Título del juego")`.

3. **Loop principal:**

   * Procesar eventos con `pygame.event.get()`.
   * Detectar cierre de ventana.
   * Controlar la velocidad de actualización de frames con `pygame.time.Clock()`.

4. **Renderizado:**

   * Pintar fondo de color.
   * Actualizar la pantalla con `pygame.display.flip()`.

**Resultado esperado:**

* Una ventana de juego que se puede abrir, mostrar un color de fondo y cerrarse correctamente.

[Siguiente](sesion_1.md)
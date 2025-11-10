# Sesión 1: Personajes y Movimiento

**Objetivo:** Introducir la creación del personaje jugador y su control básico dentro del juego.

## Contenidos

* Creación del personaje jugador
* Movimiento horizontal (izquierda y derecha)
* Salto y control de gravedad
* Eventos de teclado para controlar al jugador

## Detalles

1. **Creación del personaje:**

   * Definir tamaño, posición inicial y color.
   * Preparar variables de física: velocidad vertical y gravedad.

2. **Movimiento horizontal:**

   * Detectar teclas `izquierda` y `derecha` (`A/D` o flechas).
   * Actualizar la posición X del jugador según la velocidad.

3. **Salto y gravedad:**

   * Detectar tecla de salto (`W`, `UP` o `SPACE`).
   * Aplicar fuerza negativa para el salto.
   * Aplicar gravedad cada frame para simular caída.
   * Limitar el salto solo cuando el jugador está sobre una plataforma o suelo.

4. **Eventos de teclado:**

   * Usar `pygame.event.get()` para eventos de cierre.
   * Usar `pygame.key.get_pressed()` para movimiento continuo.

**Resultado esperado:**

* Un jugador que puede moverse a izquierda y derecha.
* Capaz de saltar solo cuando está sobre un sólido.
* Responde correctamente a los eventos de teclado.

[Siguiente](sesion_2.md)
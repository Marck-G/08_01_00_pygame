# Sesión 5: Escenas y Menú

**Objetivo:** Implementar un sistema de escenas que permita cambiar entre menú, juego y Game Over de forma organizada.

## Contenidos

* Concepto de escena en juegos
* Manejo de múltiples escenas (Menu, Game, GameOver)
* Cambio de escenas y gestión de transición

## Detalles

1. **Sistema de escenas:**

   * Crear una clase base `Scene` con métodos `update()` y `draw()`.
   * Cada escena (menú, juego, Game Over) hereda de `Scene`.

2. **Cambio de escenas:**

   * El `Game` controla la escena activa y permite cambiar mediante `change_scene()`.
   * Permite iniciar, pausar y finalizar escenas de manera controlada.

3. **Ventajas:**

   * Permite separar la lógica de cada parte del juego.
   * Facilita añadir nuevas pantallas (tutorial, créditos) sin modificar el código base.
   * Mejora la legibilidad y mantenimiento del proyecto.

**Resultado esperado:**

* El juego tiene un menú principal funcional.
* Se puede pasar a la escena de juego y a la escena de Game Over según la lógica.
* Cada escena se ejecuta de manera independiente con su propio `update` y `draw`.

[Siguiente](../06_Puntos/README.md)
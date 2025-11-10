# Sesión 8: Mejoras Gráficas y Animaciones

**Objetivo:** Integrar sprites y animaciones para el jugador, enemigos y objetos, mejorando la apariencia del juego.

## Contenidos

* Uso de sprites para personajes, enemigos y objetos
* Animaciones básicas (caminar, saltar, recibir daño)
* Integración de sprites con el sistema de cámara
* Preparación de assets gráficos (spritesheets y PNGs con transparencia)

## Detalles

1. **Sprites del jugador y enemigos:**

   * Cargar imágenes desde la carpeta `assets/`.
   * Separar frames de animación y asociarlos a estados (caminar, saltar, dañado).

2. **Animaciones:**

   * Actualizar frames cada cierto número de ticks o según velocidad de movimiento.
   * Cambiar animación según el estado del jugador o enemigo.

3. **Integración con la cámara:**

   * Restar la posición de la cámara al dibujar los sprites.
   * Mantener consistencia en el movimiento relativo a la pantalla.

4. **Assets gráficos:**

   * Mantener tamaños consistentes para sprites.
   * Usar fondo transparente en PNG para facilitar renderizado sobre cualquier fondo.

**Resultado esperado:**

* El juego muestra animaciones fluidas de los personajes y enemigos.
* Las plataformas y objetos se renderizan con sprites visualmente consistentes.
* El juego tiene un aspecto más profesional y agradable visualmente.


[Siguiente](../09_particulas/README.md)
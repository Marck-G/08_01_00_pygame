# Sesión 6: Puntos, Vidas y Game Over

**Objetivo:** Implementar un sistema de puntos, vidas y la gestión de la pantalla de Game Over.

## Contenidos

* Creación de coleccionables (monedas)
* Sistema de puntuación
* Sistema de vidas y detección de muerte
* Pantalla de Game Over
* Manejo de dependencias entre escenas y archivos

## Detalles

1. **Coleccionables:**

   * Cada moneda tiene una posición y un estado de recogida.
   * Incrementa el puntaje del jugador al ser recogida.

2. **Puntuación:**

   * Contador de puntos visible en pantalla.
   * Se actualiza dinámicamente al recoger monedas u otros objetos.

3. **Vidas y Game Over:**

   * El jugador tiene un número limitado de vidas.
   * Colisión con enemigos u obstáculos reduce vidas.
   * Al llegar a cero vidas, se cambia a la escena de Game Over.

4. **Gestión de dependencias:**

   * Evitar importaciones circulares entre `GameScene` y `GameOverScene`.
   * Usar importaciones locales dentro de funciones para romper dependencias circulares.

**Resultado esperado:**

* El jugador puede recoger monedas y ver su puntuación.
* El jugador tiene un número limitado de vidas y recibe feedback visual.
* Al quedarse sin vidas, se muestra la pantalla de Game Over correctamente.

[Siguiente](../07_Enemigos/README.md)
# Sesión 3: Cámara y Seguimiento del Jugador

**Objetivo:** Implementar un sistema de cámara que siga al jugador dentro del nivel.

## Contenidos

* Concepto de cámara en juegos 2D
* Desplazamiento del escenario basado en la posición del jugador
* Ajuste de coordenadas de renderizado con desplazamiento de cámara

## Detalles

1. **Sistema de cámara:**

   * Mantener un valor `camera_x` que determina el desplazamiento horizontal.
   * Actualizar `camera_x` según la posición del jugador para centrarlo en la pantalla.

2. **Renderizado con cámara:**

   * Restar `camera_x` a la posición X de cada objeto al dibujarlo.
   * Esto incluye plataformas, enemigos, monedas y jugador.

3. **Límites de cámara:**

   * Evitar que la cámara se mueva más allá de los bordes del nivel.
   * Mantener al jugador visible en todo momento.

**Resultado esperado:**

* El jugador siempre se mantiene visible en la pantalla.
* Los elementos del nivel se desplazan correctamente al moverse el jugador.
* La sensación de movimiento dentro del nivel es fluida y consistente.

[Siguiente](04_OOP/README.md)
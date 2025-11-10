# Sesión 9: Efectos Visuales, Partículas y Sonidos

**Objetivo:** Agregar efectos visuales y sonoros al juego para mejorar la retroalimentación y la experiencia del jugador.

## Contenidos

* Sistema de partículas para monedas, saltos y daños
* Efectos visuales al interactuar con objetos
* Integración de efectos de sonido y música de fondo
* Fuentes de audios gratuitos y legales

## Detalles

1. **Sistema de partículas:**

   * Cada partícula tiene posición, velocidad, color y tiempo de vida.
   * Se genera al recoger monedas, saltar o recibir daño.
   * Se actualiza y dibuja cada frame, eliminando partículas expiradas.

2. **Efectos visuales:**

   * Monedas muestran partículas doradas al recogerse.
   * Saltos generan partículas de polvo.
   * Daños generan partículas rojas alrededor del jugador.

3. **Sonidos y música:**

   * Efectos de sonido para saltos, recoger monedas, daño y otros eventos.
   * Música de fondo en loop continuo.
   * Integración con `pygame.mixer`:

     * `pygame.mixer.Sound()` para SFX.
     * `pygame.mixer.music` para música de fondo.

4. **Fuentes de audio:**

   * [Freesound.org](Freesound.org)
   * Kenney Assets
   * OpenGameArt
   * Zapsplat

5. **Buenas prácticas:**

   * Cargar todos los sonidos al inicio y usar `set_volume` para equilibrarlos.
   * Evitar solapamiento de sonidos cortos usando `pygame.mixer.get_busy()`.
   * Mantener consistencia con la cámara al dibujar partículas.

**Resultado esperado:**

* Monedas, saltos y daños generan efectos visuales.
* Los eventos del juego reproducen sonidos adecuados.
* Música de fondo reproduce en loop y efectos sonoros mejoran la experiencia de juego.

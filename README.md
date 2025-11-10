# Curso Introductorio de Desarrollo de Videojuegos 2D con Python y Pygame

Este curso está diseñado para programadores con experiencia que desean iniciarse en el desarrollo de videojuegos 2D utilizando **Python** y **Pygame**. A lo largo del curso, se construye un juego de plataformas paso a paso, organizando el código en módulos y carpetas según la funcionalidad.

## Estructura de archivos

El proyecto está dividido en sesiones/temas, cada uno con sus propios archivos:

```
├── 00_basic.py                  # Sesión 0: Fundamentos de Pygame y ventana básica
├── 01_Personajes.py             # Sesión 1: Creación de personajes y eventos de movimiento
├── 02_Plataformas.py            # Sesión 2: Creación de plataformas y colisiones
├── 03_Camara.py                 # Sesión 3: Sistema de cámara y seguimiento del jugador
├── 04_OOP/                      # Sesión 4: Refactorización a OOP (clases Player, Platform, Game)
│   ├── game.py
│   ├── main.py
│   ├── platform.py
│   ├── player.py
│   └── settings.py
├── 05_escenas/                  # Sesión 5: Implementación de escenas y menú
│   ├── game_scene.py
│   ├── menu_scene.py
│   ├── scene.py
│   └── settings.py
├── 06_Puntos/                   # Sesión 6: Sistema de puntos, vidas y Game Over
│   ├── coin.py
│   ├── game_over.py
│   ├── game_scene.py
│   └── player.py
├── 07_Enemigos/                 # Sesión 7: Enemigos y obstáculos
│   ├── enemy.py
│   ├── obstacle.py
│   ├── game_scene.py
│   └── player.py
├── 08_Mejoras_graficas/         # Sesión 8: Sprites y animaciones básicas
│   ├── assets/                  # Carpeta de imágenes
│   ├── coin.py
│   ├── enemy.py
│   ├── player.py
│   └── game_scene.py
└── 09_particulas/                # Sesión 9: Efectos visuales, partículas y sonidos
    ├── assets/                  # Sprites y sonidos (wav, mp3)
    ├── particle.py
    ├── player.py
    └── game_scene.py
```

## Sesiones del curso

### Sesión 0: Fundamentos de Pygame

* Creación de la ventana del juego.
* Loop principal y control de FPS.
* Renderizado de color de fondo.

### Sesión 1: Personajes

* Creación del personaje jugador.
* Movimiento horizontal y salto.
* Eventos de teclado.

### Sesión 2: Plataformas

* Creación de plataformas estáticas.
* Colisión del jugador con plataformas.
* Limitación del salto solo cuando el jugador está sobre un sólido.

### Sesión 3: Cámara

* Sistema de cámara que sigue al jugador.
* Ajuste de coordenadas para renderizado con desplazamiento.

### Sesión 4: Refactorización OOP

* Transformación de las entidades en clases (`Player`, `Platform`, `Game`).
* Mejora en la organización del código.

### Sesión 5: Escenas y menú

* Sistema de escenas para menú, juego y Game Over.
* Cambio de escenas mediante un SceneManager.

### Sesión 6: Puntos, vidas y Game Over

* Implementación de coleccionables (monedas).
* Sistema de vidas y reinicio del jugador.
* Pantalla de Game Over con puntuación.
* Solución de dependencias circulares mediante importaciones locales.

### Sesión 7: Enemigos y obstáculos

* Creación de enemigos móviles y obstáculos fijos.
* Colisiones que restan vidas al jugador.
* Integración con el sistema de Game Over.

### Sesión 8: Mejoras gráficas y animaciones

* Uso de sprites para jugador, enemigos y objetos.
* Animaciones de caminar, saltar y daño.
* Integración de sprites con el sistema de cámara.

### Sesión 9: Efectos visuales, partículas y sonidos

* Sistema de partículas para monedas, saltos y daños.
* Integración de efectos de sonido y música de fondo.
* Uso de `pygame.mixer` para SFX y música.
* Fuentes recomendadas para sonidos: Freesound, Kenney Assets, OpenGameArt, Zapsplat.

---

Este curso modular permite a los estudiantes seguir **archivo por archivo**, entendiendo la progresión de un juego de plataformas desde cero hasta un prototipo completo con animaciones, enemigos, puntos, efectos visuales y sonido.

[Siguiente](sesion_0.md)
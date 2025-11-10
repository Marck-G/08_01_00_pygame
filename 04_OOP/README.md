# Sesión 4: Refactorización a OOP

**Objetivo:** Transformar el proyecto a un enfoque de **Programación Orientada a Objetos**, mejorando la organización y modularidad del código.

## Contenidos

* Creación de clases para entidades principales
* Organización del código en módulos
* Mejora de la mantenibilidad y escalabilidad del juego

## Detalles

1. **Clases principales:**

   * `Player`: maneja movimiento, físicas, animaciones y colisiones.
   * `Platform`: representa plataformas estáticas o móviles.
   * `Game`: controlador principal del juego, manejo de escenas y eventos.

2. **Modularización:**

   * Separar cada clase en archivos individuales dentro de la carpeta `04_OOP/`.
   * Configuración y constantes en `settings.py`.

3. **Beneficios de OOP:**

   * Código más limpio y organizado.
   * Facilita añadir nuevas entidades (enemigos, objetos, efectos) sin modificar el código base.
   * Permite reutilización y escalabilidad del proyecto.

**Resultado esperado:**

* Todas las entidades del juego son clases con responsabilidades claras.
* Los módulos están organizados por funcionalidad.
* El juego sigue funcionando igual, pero el código es más mantenible y preparado para agregar nuevas características.

[Siguiente](../05_escenas/README.md)
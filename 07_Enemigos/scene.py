from abc import ABC, abstractmethod


# Clase base para todas las escenas del juego
class Scene:
    """Clase base para todas las escenas del juego."""

    def __init__(self, game):
        self.game = game

    @abstractmethod
    def handle_events(self, events):
        """Maneja los eventos de la escena."""
        pass

    @abstractmethod
    def update(self):
        """Actualiza la lógica de la escena."""
        pass

    @abstractmethod
    def draw(self):
        """Dibuja la escena en la pantalla."""
        pass

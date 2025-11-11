import numpy as np

def crear_cubo(tamano=1.0):
    """Devuelve vértices y caras de un cubo centrado en el origen"""

    s = tamano / 2

    # Vértices del cubo (x, y, z, 1)
    vertices = np.array([
        [-s, -s, -s, 1],
        [ s, -s, -s, 1],
        [ s,  s, -s, 1],
        [-s,  s, -s, 1],
        [-s, -s,  s, 1],
        [ s, -s,  s, 1],
        [ s,  s,  s, 1],
        [-s,  s,  s, 1],
    ], dtype=float)

    # Caras definidas por índices de vértices
    caras = np.array([
        [0, 1, 2, 3],  # Frontal
        [4, 5, 6, 7],  # Trasera
        [0, 1, 5, 4],  # Inferior
        [2, 3, 7, 6],  # Superior
        [1, 2, 6, 5],  # Derecha
        [0, 3, 7, 4],  # Izquierda
    ], dtype=int)

    return vertices, caras

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

from math3d import matrices
from objects.cube import crear_cubo

def init_window(width=1300, height=900):
    pygame.init()
    pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Demo 3D - Cubo")

    glEnable(GL_DEPTH_TEST)
    gluPerspective(45, (width / height), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

def dibujar_cubo(vertices, caras):
    """Dibuja un cubo con líneas de color blanco"""
    glBegin(GL_LINES)
    glColor3f(1, 1, 1)

    # Dibujar los bordes de las caras
    for cara in caras:
        for i in range(4):
            v1 = vertices[cara[i]][:3]
            v2 = vertices[cara[(i + 1) % 4]][:3]
            glVertex3fv(v1)
            glVertex3fv(v2)
    glEnd()

def main():
    init_window()
    vertices, caras = crear_cubo(2.0)

    angulo = 0.0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Crear matrices de rotación
        Rx = matrices.rotacion_x(np.radians(angulo - 0.04))
        Ry = matrices.rotacion_y(np.radians(angulo - 0.1))
        RZ = matrices.rotacion_z(np.radians(angulo))

        # Aplicar las rotaciones a los vértices originales
        transformacion = Ry @ Rx @ RZ # el @ es el operador de producto matricial en numpy 
        vertices_transformados = (transformacion @ vertices.T).T

        dibujar_cubo(vertices_transformados, caras)

        angulo += 0.2  # Rotación continua

        pygame.display.flip()
        pygame.time.wait(10)

    pygame.quit()

if __name__ == "__main__":
    main()

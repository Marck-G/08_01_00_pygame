import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

from math3d import matrices
from objects.cube import crear_cubo


def init_window(width=1200, height=800):
    pygame.init()
    pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Demo 3D - Transformaciones y Cámara")

    glEnable(GL_DEPTH_TEST)
    glClearColor(0.0, 0.0, 0.0, 1.0)  # fondo negro
    gluPerspective(45, (width / height), 0.1, 50.0)
    # ❌ eliminamos glTranslatef(), ahora todo se controla por matrices numpy


def dibujar_cubo(vertices, caras):
    """Dibuja un cubo con líneas blancas"""
    glBegin(GL_LINES)
    glColor3f(1, 1, 1)
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

    # Estado inicial del cubo y cámara
    angulo = 0.0
    posicion_cubo = np.array([0.0, 0.0, 0.0])
    escala_cubo = np.array([1.0, 1.0, 1.0])
    cam_pos = np.array([0.0, 0.0, 5.0])  # cámara alejada del cubo (positiva en Z)

    clock = pygame.time.Clock()
    running = True
    while running:
        dt = clock.tick(60) / 1000  # Delta time (s)

        # --- EVENTOS ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            running = False
        if keys[K_w]:
            cam_pos[2] -= 2 * dt  # acercar
        if keys[K_s]:
            cam_pos[2] += 2 * dt  # alejar
        if keys[K_a]:
            cam_pos[0] -= 2 * dt
        if keys[K_d]:
            cam_pos[0] += 2 * dt
        if keys[K_q]:
            cam_pos[1] -= 2 * dt
        if keys[K_e]:
            cam_pos[1] += 2 * dt

        # --- MATRICES ---
        # Modelo
        Rx = matrices.rotacion_x(np.radians(angulo * dt))
        Ry = matrices.rotacion_y(np.radians(angulo))
        S = matrices.escala(*escala_cubo)
        T = matrices.traslacion(*posicion_cubo)
        M = T @ Ry @ Rx @ S

        # Vista (la cámara)
        V = matrices.traslacion(-cam_pos[0], -cam_pos[1], -cam_pos[2])

        # Transformar vértices
        vertices_transformados = (V @ M @ vertices.T).T

        # --- RENDER ---
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        dibujar_cubo(vertices_transformados, caras)
        pygame.display.flip()

        angulo += 50 * dt

    pygame.quit()


if __name__ == "__main__":
    main()

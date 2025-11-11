import pygame
from pygame.locals import *
from OpenGL.GL import *
import numpy as np

from math3d import matrices
from objects.cube import crear_cubo


def init_window(width=800, height=600):
    pygame.init()
    pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Demo 3D - Cámara libre y proyección manual")
    glEnable(GL_DEPTH_TEST)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    pygame.mouse.set_visible(False)
    pygame.event.set_grab(True)  # bloquear ratón en la ventana


def dibujar_cubo(vertices, caras):
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
    WIDTH, HEIGHT = 800, 600
    init_window(WIDTH, HEIGHT)
    vertices, caras = crear_cubo(2.0)

    # --- MATRIZ DE PROYECCIÓN MANUAL ---
    P = matrices.proyeccion_perspectiva(45, WIDTH / HEIGHT, 0.1, 100.0)

    # --- ESTADO DEL CUBO ---
    angulo = 0.0
    posicion_cubo = np.array([0.0, 0.0, 0.0])
    escala_cubo = np.array([1.0, 1.0, 1.0])

    # --- CÁMARA ---
    cam_pos = np.array([0.0, 0.0, 5.0])
    yaw, pitch = 0.0, 0.0
    sensibilidad = 0.2
    velocidad = 3.0

    clock = pygame.time.Clock()
    running = True
    while running:
        dt = clock.tick(60) / 1000.0
        dx, dy = pygame.mouse.get_rel()  # movimiento del ratón
        yaw += dx * sensibilidad
        pitch -= dy * sensibilidad
        pitch = np.clip(pitch, -89.0, 89.0)

        # --- DIRECCIÓN DE LA CÁMARA ---
        front = np.array([
            np.cos(np.radians(yaw)) * np.cos(np.radians(pitch)),
            np.sin(np.radians(pitch)),
            np.sin(np.radians(yaw)) * np.cos(np.radians(pitch))
        ])
        front = front / np.linalg.norm(front)
        right = np.cross(front, np.array([0.0, 1.0, 0.0]))
        right = right / np.linalg.norm(right)
        up = np.cross(right, front)

        # --- INPUT TECLADO ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            running = False
        if keys[K_w]:
            cam_pos += front * velocidad * dt
        if keys[K_s]:
            cam_pos -= front * velocidad * dt
        if keys[K_a]:
            cam_pos -= right * velocidad * dt
        if keys[K_d]:
            cam_pos += right * velocidad * dt
        if keys[K_q]:
            cam_pos -= up * velocidad * dt
        if keys[K_e]:
            cam_pos += up * velocidad * dt

        # --- MATRICES ---
        Rx = matrices.rotacion_x(np.radians(angulo))
        Ry = matrices.rotacion_y(np.radians(angulo))
        S = matrices.escala(*escala_cubo)
        T = matrices.traslacion(*posicion_cubo)
        M = T @ Ry @ Rx @ S

        target = cam_pos + front
        V = matrices.vista_look_at(cam_pos, target, np.array([0.0, 1.0, 0.0]))

        # Transformación completa
        vertices_transformados = (P @ V @ M @ vertices.T).T

        # Normalizar a coordenadas homogéneas (dividir por w)
        for i in range(len(vertices_transformados)):
            if vertices_transformados[i][3] != 0:
                vertices_transformados[i] /= vertices_transformados[i][3]

        # --- RENDER ---
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        dibujar_cubo(vertices_transformados, caras)
        pygame.display.flip()

        angulo += 40 * dt

    pygame.quit()


if __name__ == "__main__":
    main()

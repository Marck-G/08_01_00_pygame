import numpy as np

def vista_look_at(eye, target, up):
    """Crea una matriz de vista tipo lookAt"""
    f = target - eye
    f = f / np.linalg.norm(f)

    u = up / np.linalg.norm(up)
    s = np.cross(f, u)
    s = s / np.linalg.norm(s)
    u = np.cross(s, f)

    M = np.eye(4)
    M[0, :3] = s
    M[1, :3] = u
    M[2, :3] = -f
    M[:3, 3] = -M[:3, :3] @ eye
    return M


def proyeccion_perspectiva(fov, aspect, near, far):
    """Matriz de proyección perspectiva manual"""
    f = 1.0 / np.tan(np.radians(fov) / 2)
    P = np.zeros((4, 4))
    P[0, 0] = f / aspect
    P[1, 1] = f
    P[2, 2] = (far + near) / (near - far)
    P[2, 3] = (2 * far * near) / (near - far)
    P[3, 2] = -1
    return P


def identidad():
    """Matriz identidad 4x4"""
    return np.eye(4)

def traslacion(tx, ty, tz):
    """Matriz de traslación"""
    T = np.eye(4)
    T[0, 3] = tx
    T[1, 3] = ty
    T[2, 3] = tz
    return T

def escala(sx, sy, sz):
    """Matriz de escala"""
    S = np.eye(4)
    S[0, 0] = sx
    S[1, 1] = sy
    S[2, 2] = sz
    return S

def rotacion_x(theta):
    """Rotación alrededor del eje X"""
    c, s = np.cos(theta), np.sin(theta)
    R = np.eye(4)
    R[1, 1], R[1, 2] = c, -s
    R[2, 1], R[2, 2] = s, c
    return R

def rotacion_y(theta):
    """Rotación alrededor del eje Y"""
    c, s = np.cos(theta), np.sin(theta)
    R = np.eye(4)
    R[0, 0], R[0, 2] = c, s
    R[2, 0], R[2, 2] = -s, c
    return R

def rotacion_z(theta):
    """Rotación alrededor del eje Z"""
    c, s = np.cos(theta), np.sin(theta)
    R = np.eye(4)
    R[0, 0], R[0, 1] = c, -s
    R[1, 0], R[1, 1] = s, c
    return R

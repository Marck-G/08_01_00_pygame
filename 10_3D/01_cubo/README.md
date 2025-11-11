# 🚀 Sesión 1 — Introducción al Espacio 3D y Representación Matemática

> **Objetivo:** Comprender el paso del espacio 2D al 3D, definir la representación matemática de los puntos y objetos,  
> e introducir el concepto de coordenadas homogéneas y matrices de transformación.

---

## 🌐 1. Del plano 2D al espacio 3D

En el entorno 2D, todo punto puede representarse como:

$$
\mathbf{p}_{2D} = 
\begin{bmatrix}
x \\
y
\end{bmatrix}
$$

Donde \( x \) e \( y \) son las coordenadas en el eje horizontal y vertical respectivamente.

Al pasar al **espacio tridimensional**, añadimos un nuevo eje, el **eje Z**, que nos permite medir profundidad.

$$
\mathbf{p}_{3D} = 
\begin{bmatrix}
x \\
y \\
z
\end{bmatrix}
$$

Este vector ahora representa una posición en el espacio tridimensional.

---

## 🧮 2. Ejes de referencia en 3D

El sistema de coordenadas cartesiano tridimensional está formado por tres ejes perpendiculares entre sí:

- **Eje X:** horizontal (izquierda ↔ derecha)
- **Eje Y:** vertical (arriba ↔ abajo)
- **Eje Z:** profundidad (cerca ↔ lejos)

Un punto \( (x, y, z) \) se interpreta como una distancia a lo largo de cada uno de estos ejes.

En muchos motores gráficos (y en nuestro proyecto), adoptamos la siguiente convención:
- Eje X → hacia la derecha  
- Eje Y → hacia arriba  
- Eje Z → hacia el fondo de la pantalla (positivo hacia el observador)

---

## 🧠 3. Representación de puntos y objetos

Los objetos tridimensionales se construyen a partir de **vértices**, que son puntos en el espacio.  
Por ejemplo, un cubo puede definirse mediante los ocho vértices de sus esquinas:

$$
V =
\begin{bmatrix}
x_1 & y_1 & z_1 \\
x_2 & y_2 & z_2 \\
x_3 & y_3 & z_3 \\
\vdots & \vdots & \vdots \\
x_8 & y_8 & z_8
\end{bmatrix}
$$

Cada fila representa un vértice, y el conjunto de vértices define la **geometría del objeto**.

---

## 📐 4. Coordenadas homogéneas

Para aplicar transformaciones (rotación, traslación, escala) con una sola operación matricial,  
usamos **coordenadas homogéneas**, agregando una cuarta componente \( w \):

$$
\mathbf{p}_{h} =
\begin{bmatrix}
x \\
y \\
z \\
1
\end{bmatrix}
$$

Gracias a este cuarto elemento, podemos representar **traslaciones** y **proyecciones** mediante multiplicaciones matriciales.

---

## 🧩 5. Matriz identidad

La matriz identidad 4×4 actúa como punto de partida para cualquier transformación:

$$
I =
\begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

Aplicarla sobre cualquier punto no lo modifica:

$$
I \cdot \mathbf{p}_{h} = \mathbf{p}_{h}
$$

Esto representa el **estado inicial sin transformaciones**.

---

## ⚙️ 6. Transformaciones básicas (visión general)

Cada operación geométrica puede representarse como una **matriz 4x4**.  
Más adelante las construiremos con NumPy, pero a nivel teórico se definen así:

- **Traslación** — mover un objeto:
  $$
  T =
  \begin{bmatrix}
  1 & 0 & 0 & t_x \\
  0 & 1 & 0 & t_y \\
  0 & 0 & 1 & t_z \\
  0 & 0 & 0 & 1
  \end{bmatrix}
  $$

- **Escalado** — cambiar su tamaño:
  $$
  S =
  \begin{bmatrix}
  s_x & 0 & 0 & 0 \\
  0 & s_y & 0 & 0 \\
  0 & 0 & s_z & 0 \\
  0 & 0 & 0 & 1
  \end{bmatrix}
  $$

- **Rotaciones** — cambiar su orientación:
  - En X:
    $$
    R_x(\theta) =
    \begin{bmatrix}
    1 & 0 & 0 & 0 \\
    0 & \cos\theta & -\sin\theta & 0 \\
    0 & \sin\theta & \cos\theta & 0 \\
    0 & 0 & 0 & 1
    \end{bmatrix}
    $$
  - En Y:
    $$
    R_y(\theta) =
    \begin{bmatrix}
    \cos\theta & 0 & \sin\theta & 0 \\
    0 & 1 & 0 & 0 \\
    -\sin\theta & 0 & \cos\theta & 0 \\
    0 & 0 & 0 & 1
    \end{bmatrix}
    $$
  - En Z:
    $$
    R_z(\theta) =
    \begin{bmatrix}
    \cos\theta & -\sin\theta & 0 & 0 \\
    \sin\theta & \cos\theta & 0 & 0 \\
    0 & 0 & 1 & 0 \\
    0 & 0 & 0 & 1
    \end{bmatrix}
    $$

Estas matrices se usarán en sesiones posteriores para transformar los vértices de nuestros objetos 3D.

---

## 🧠 7. Composición de transformaciones

Una transformación completa suele combinar varias operaciones:

$$
M = T \cdot R \cdot S
$$

El resultado se aplica a cada vértice:

$$
\mathbf{p'} = M \cdot \mathbf{p}_{h}
$$

> ⚠️ El orden importa: las multiplicaciones de matrices **no son conmutativas**.

Por ejemplo:

$$
R \cdot T \neq T \cdot R
$$

Esto significa que **rotar y luego trasladar** no es igual a **trasladar y luego rotar**.

---

## 🧭 8. Espacios de coordenadas

Para entender correctamente los movimientos en 3D, hay que distinguir los **espacios de referencia**:

| Espacio | Qué representa |
|----------|----------------|
| **Local (modelo)** | El sistema propio del objeto (sus coordenadas internas). |
| **Mundo (world)** | La posición global dentro de la escena. |
| **Vista (view)** | Lo que "ve" la cámara. |
| **Proyección (clip)** | Coordenadas preparadas para proyectar en 2D. |

Las transformaciones entre espacios se aplican multiplicando las matrices adecuadas:

$$
V_{mundo} = M_{modelo} \cdot V_{local}
$$

$$
V_{vista} = M_{vista} \cdot V_{mundo}
$$

$$
V_{clip} = P_{proyeccion} \cdot V_{vista}
$$

---

## 🧮 9. Uso de NumPy

Para realizar todas estas operaciones en Python, usaremos **NumPy**,  
que permite representar puntos y matrices de forma eficiente:

```python
import numpy as np

# Vector homogéneo
p = np.array([x, y, z, 1])

# Matriz de traslación
T = np.array([
    [1, 0, 0, tx],
    [0, 1, 0, ty],
    [0, 0, 1, tz],
    [0, 0, 0, 1]
])

# Aplicar transformación
p_transformed = T @ p
```
Con esta base, podemos representar cualquier transformación espacial de forma algebraica y precisa.

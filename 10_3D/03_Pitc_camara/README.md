# 🧭 Sesión 3 — Cámara libre y Proyección 3D con NumPy y OpenGL

> **Objetivo:** Comprender y aplicar los fundamentos matemáticos de la cámara en 3D (rotación, traslación y proyección),  
> utilizando **NumPy** para construir las **matrices de transformación** que controlan la posición del observador y los objetos en el mundo 3D.

---

## 🧱 1. Introducción

En las primeras sesiones trabajamos con transformaciones 2D y luego con un cubo 3D rotando.  
Ahora damos un paso más: **simularemos una cámara real**, capaz de moverse y mirar en cualquier dirección dentro del espacio tridimensional.

Para ello, usaremos:
- **NumPy** → para operar con matrices y vectores.
- **PyOpenGL + Pygame** → para visualizar los objetos y recibir la entrada del usuario (ratón y teclado).

El enfoque es educativo: **no usamos las funciones automáticas de OpenGL** como `gluPerspective()` o `glRotatef()`.  
En su lugar, **calculamos manualmente todas las matrices** para entender cómo funciona la proyección 3D desde la matemática.

---

## 🧮 2. Fundamentos Matemáticos

### 2.1. Espacio 3D y coordenadas homogéneas

Un punto en 3D se representa como un vector columna:
$$
P = 
\begin{bmatrix}
x \\
y \\
z \\
1
\end{bmatrix}
$$
Usamos **4 componentes (x, y, z, 1)** para poder aplicar transformaciones lineales (rotaciones, escalas, traslaciones) mediante **multiplicación matricial**.

---

### 2.2. Matrices básicas de transformación

| Transformación | Descripción | Ejemplo |
|----------------|--------------|----------|
| **Traslación** | Desplaza un objeto en el espacio. | `matrices.traslacion(dx, dy, dz)` |
| **Rotación** | Gira el objeto sobre un eje (x, y o z). | `matrices.rotacion_y(θ)` |
| **Escalado** | Cambia el tamaño del objeto. | `matrices.escala(sx, sy, sz)` |

Cada una de estas operaciones se puede combinar multiplicando sus matrices:

$$
M_{modelo} = T \times R_y \times R_x \times S
$$

Esta matriz final representa la **transformación del objeto** desde su espacio local al mundo.

---

### 2.3. Matriz de vista (View Matrix)

La **matriz de vista** transforma el mundo según la posición y orientación de la cámara, simulando el hecho de que “nos movemos” dentro del entorno.

Se construye a partir de tres vectores ortogonales:
- **f (forward)** → dirección hacia donde mira la cámara.  
- **s (side/right)** → eje horizontal.  
- **u (up)** → eje vertical.

La función `vista_look_at(eye, target, up)` calcula esta matriz usando productos vectoriales:

$$
V =
\begin{bmatrix}
s_x & s_y & s_z & -s \cdot eye \\
u_x & u_y & u_z & -u \cdot eye \\
-f_x & -f_y & -f_z & f \cdot eye \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

Donde:
- `eye`: posición de la cámara.
- `target`: punto hacia el que mira.
- `up`: vector que indica la "vertical" del mundo (normalmente `[0, 1, 0]`).

---

### 2.4. Matriz de proyección perspectiva

La proyección convierte coordenadas 3D en 2D, simulando la **profundidad y el campo de visión** del ojo humano.

La fórmula para la matriz de proyección perspectiva es:
$$
 P =
\begin{bmatrix}
\frac{f}{aspect} & 0 & 0 & 0 \\
0 & f & 0 & 0 \\
0 & 0 & \frac{far + near}{near - far} & \frac{2 \cdot far \cdot near}{near - far} \\
0 & 0 & -1 & 0
\end{bmatrix}

$$
donde  
$$
f = \frac{1}{\tan(fov/2)}
$$

y:
- **fov** → campo de visión vertical (en grados).  
- **aspect** → relación de aspecto (ancho / alto de la pantalla).  
- **near, far** → distancias al plano cercano y lejano del recorte de visión (clipping planes).

---

### 2.5. Transformación final

Cada vértice pasa por una secuencia de transformaciones:

$$
P_{clip} = P_{proyección} \times V_{vista} \times M_{modelo} \times P_{mundo}
$$

Luego, para convertir a coordenadas de pantalla, se divide por la componente **w** (normalización):

$$
P_{final} = \frac{P_{clip}}{w}
$$


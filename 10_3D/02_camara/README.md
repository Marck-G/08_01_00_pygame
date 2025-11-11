# 🧱 Sesión 2 — Fundamentos de Transformaciones 3D con NumPy y Álgebra Lineal

> **Objetivo:** Comprender cómo se representan objetos y transformaciones en 3D mediante matrices y vectores,  
> utilizando las operaciones básicas de álgebra lineal que sirven como cimiento de cualquier motor gráfico 3D.

---

## 🌍 1. Introducción

En esta sesión pasamos de trabajar en 2D (traslaciones y rotaciones planas)  
a construir un entorno **3D matemático** utilizando **NumPy** como herramienta de cálculo matricial.

El propósito fue entender cómo los objetos tridimensionales —como un cubo o una esfera— se representan y transforman  
mediante **multiplicaciones de matrices**, en lugar de operaciones geométricas directas.

Esta es la base de todos los motores 3D modernos (Unity, Unreal, Godot, etc.),  
y entenderla permite comprender el pipeline interno de gráficos.

---

## 🧮 2. Representación de un objeto 3D

En computación gráfica, un objeto tridimensional se describe como un conjunto de puntos o vértices:

$$
V = 
\begin{bmatrix}
x_1 & y_1 & z_1 \\
x_2 & y_2 & z_2 \\
x_3 & y_3 & z_3 \\
\vdots & \vdots & \vdots \\
x_n & y_n & z_n
\end{bmatrix}
$$

Para aplicar transformaciones (rotación, traslación, escala) de forma uniforme,  
cada vértice se representa en **coordenadas homogéneas**, añadiendo un cuarto componente \( w = 1 \):

$$
V_h = 
\begin{bmatrix}
x_1 & y_1 & z_1 & 1 \\
x_2 & y_2 & z_2 & 1 \\
\vdots & \vdots & \vdots & \vdots \\
x_n & y_n & z_n & 1
\end{bmatrix}
$$

Esto permite representar todas las transformaciones como **multiplicaciones matriciales** 4x4.

---

## 📐 3. Álgebra lineal aplicada a transformaciones

### 3.1. Vectores

Un **vector** representa dirección y magnitud en el espacio.  
En 3D, un vector puede representar:
- Una posición: \( (x, y, z) \)
- Una dirección: \( (dx, dy, dz) \)
- Una normal (perpendicular a una superficie)

Propiedades fundamentales:

$$
\begin{aligned}
\text{Suma de vectores:} &\quad \vec{a} + \vec{b} \\
\text{Producto por escalar:} &\quad k \cdot \vec{v} \\
\text{Producto punto:} &\quad \vec{a} \cdot \vec{b} = |a||b|\cos(\theta) \\
\text{Producto cruzado:} &\quad \vec{a} \times \vec{b}
\end{aligned}
$$

---

### 3.2. Matrices de transformación

En 3D, las transformaciones se representan como **matrices 4x4** que operan sobre los vectores homogéneos.

#### a) Matriz de Traslación

Desplaza un objeto en el espacio tridimensional.

$$
T = 
\begin{bmatrix}
1 & 0 & 0 & t_x \\
0 & 1 & 0 & t_y \\
0 & 0 & 1 & t_z \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

Multiplicar un vértice por esta matriz añade \( (t_x, t_y, t_z) \) a su posición.

---

#### b) Matriz de Escalado

Cambia el tamaño del objeto.

$$
S =
\begin{bmatrix}
s_x & 0 & 0 & 0 \\
0 & s_y & 0 & 0 \\
0 & 0 & s_z & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

- Si \( s_x = s_y = s_z \), el escalado es uniforme.  
- Si difieren, se obtiene un escalado anisotrópico.

---

#### c) Matriz de Rotación

Define una rotación en torno a un eje.

**Rotación en X:**

$$
R_x(\theta) =
\begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & \cos\theta & -\sin\theta & 0 \\
0 & \sin\theta & \cos\theta & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

**Rotación en Y:**

$$
R_y(\theta) =
\begin{bmatrix}
\cos\theta & 0 & \sin\theta & 0 \\
0 & 1 & 0 & 0 \\
-\sin\theta & 0 & \cos\theta & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

**Rotación en Z:**

$$
R_z(\theta) =
\begin{bmatrix}
\cos\theta & -\sin\theta & 0 & 0 \\
\sin\theta & \cos\theta & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

---

### 3.3. Composición de transformaciones

Las transformaciones se pueden **combinar multiplicando matrices**:

$$
M_{total} = T \cdot R \cdot S
$$

> **Orden importa:**  
> la multiplicación matricial **no es conmutativa**, por tanto:
> 
> $$
> R \cdot T \neq T \cdot R
> $$

Normalmente, el orden usado en gráficos 3D es:

1. Escalado (S)  
2. Rotación (R)  
3. Traslación (T)

Así, cada vértice del modelo se transforma con:

$$
V' = T \cdot R \cdot S \cdot V
$$

---

## 🧭 4. Espacios de coordenadas

En un pipeline 3D existen varios **espacios de coordenadas**, cada uno con su propósito:

| Espacio | Descripción |
|----------|--------------|
| **Local (modelo)** | Coordenadas originales del objeto respecto a su propio centro. |
| **Mundo (world)** | Objeto posicionado en la escena global. |
| **Vista (view)** | Sistema de referencia de la cámara. |
| **Proyección (clip)** | Coordenadas preparadas para proyectar en 2D. |

Cada etapa se obtiene multiplicando matrices:

$$
\begin{aligned}
V_{world} &= M_{model} \cdot V_{local} \\
V_{view}  &= M_{view} \cdot V_{world} \\
V_{clip}  &= P_{projection} \cdot V_{view}
\end{aligned}
$$

El resultado final \( V_{clip} \) es lo que se proyecta en pantalla.

---

## 🧠 5. Coordenadas homogéneas y división por w

Tras la multiplicación por la matriz de proyección, cada vértice tiene un componente \( w \).  
Para normalizar el resultado (convertir de espacio 3D a pantalla), se realiza:

$$
\begin{aligned}
x' &= \frac{x}{w} \\
y' &= \frac{y}{w} \\
z' &= \frac{z}{w}
\end{aligned}
$$

Este proceso se llama **perspectiva homogénea**,  
y es lo que genera la **sensación de profundidad**:  
objetos lejanos se dibujan más pequeños.

---

## 🧩 6. Pipeline conceptual (sin código)

1. **Definimos un objeto** como una lista de vértices 3D.  
2. **Construimos las matrices** de escala, rotación y traslación.  
3. **Multiplicamos todas** para obtener una matriz de modelo:  
   \( M_{model} = T \cdot R \cdot S \)  
4. **Aplicamos esta matriz** a todos los vértices del objeto.  
5. Obtenemos las posiciones transformadas en el mundo 3D.

En esta sesión aún no introducimos la cámara ni la proyección;  
eso se aborda en la **Sesión 3**, cuando incorporamos las matrices de vista y proyección.

---

## 📚 7. Conceptos aprendidos

| Concepto | Descripción |
|-----------|-------------|
| **Matriz 4x4** | Permite aplicar todas las transformaciones (incluyendo traslaciones) mediante álgebra lineal. |
| **Coordenadas homogéneas** | Extienden el espacio 3D a 4D para representar traslaciones y perspectivas. |
| **Producto matricial** | Base de todas las transformaciones geométricas. |
| **No conmutatividad** | El orden de las transformaciones afecta el resultado final. |
| **Espacios de coordenadas** | Cada objeto pasa del espacio local al de mundo, vista y proyección. |

---

## 🎯 8. Conclusión

Esta sesión sentó las bases del **motor matemático** de nuestro entorno 3D:

- Los objetos se definen como matrices de vértices.  
- Las transformaciones se aplican mediante multiplicación matricial.  
- Se comprendió la estructura de las matrices 4x4 que controlan movimiento, orientación y escala.  

Con estos conocimientos, en la siguiente sesión construimos la **cámara libre y la proyección perspectiva**,  
para dar vida al mundo 3D y permitir movernos dentro de él.

---

## 🧾 Créditos

Desarrollado dentro del proyecto **"Game Dev Learning Path"**  
Autoría conjunta con ChatGPT (GPT-5).  
Objetivo: aprendizaje progresivo de matemáticas, álgebra lineal y gráficos 3D en Python.

# 🎮 Sesión 0 — Fundamentos Teóricos para Juegos 3D

> **Objetivo:** Sentar las bases matemáticas y conceptuales necesarias para desarrollar juegos en 3D,  
> comprendiendo vectores, matrices, sistemas de coordenadas, transformaciones y proyección.

---

## 🌐 1. Introducción al desarrollo 3D

En los juegos 3D, cada objeto, cámara y luz se representa mediante **coordenadas matemáticas**.  
El motor de un juego realiza transformaciones constantes de estos objetos para renderizarlos en pantalla.

La comprensión de **espacios de coordenadas, matrices y vectores** es crucial para:

- Mover objetos y cámaras.  
- Rotar y escalar elementos.  
- Aplicar proyecciones para representar la profundidad.  
- Implementar físicas y colisiones.  

---

## 🧮 2. Sistemas de coordenadas

### 2.1. Coordenadas 2D

En 2D, cada punto se representa como:

$$
\mathbf{p}_{2D} =
\begin{bmatrix}
x \\
y
\end{bmatrix}
$$

- $x$ → horizontal  
- $y$ → vertical  

Transformaciones como traslación y rotación se realizan mediante matrices 2×2 (rotación) o 3×3 (coordenadas homogéneas).

---

### 2.2. Coordenadas 3D

En 3D, añadimos el eje **Z** para la profundidad:

$$
\mathbf{p}_{3D} =
\begin{bmatrix}
x \\
y \\
z
\end{bmatrix}
$$

- $x$ → izquierda / derecha  
- $y$ → arriba / abajo  
- $z$ → profundidad (cerca ↔ lejos)

Los objetos 3D se definen como **conjuntos de vértices**:

$$
V =
\begin{bmatrix}
x_1 & y_1 & z_1 \\
x_2 & y_2 & z_2 \\
\vdots & \vdots & \vdots \\
x_n & y_n & z_n
\end{bmatrix}
$$

---

### 2.3 Coordenadas homogéneas (ampliación teórica)

En geometría y gráficos 3D, las **coordenadas homogéneas** permiten representar puntos y vectores en un espacio extendido que facilita las transformaciones lineales y afines.  
Se define un vector 3D $ (x, y, z) $ extendido con un componente extra $ w $:

$$
\mathbf{p}_h =
\begin{bmatrix}
x \\
y \\
z \\
w
\end{bmatrix}
$$

En la práctica, normalmente $ w = 1 $ para los **puntos** y $ w = 0 $ para los **vectores de dirección**.

---

#### 1️⃣ ¿Por qué usar coordenadas homogéneas?

1. **Unificar transformaciones:**  
   - Traslaciones, escalados y rotaciones pueden representarse como multiplicaciones por **matrices 4x4**.  
   - En coordenadas cartesianas normales, la traslación **no puede representarse como multiplicación de matriz 3x3**, por lo que se requeriría suma adicional.

2. **Proyecciones:**  
   - Para representar perspectiva (objetos lejanos se ven más pequeños), se usan transformaciones homogéneas que involucran $ w $ y luego se realiza una **división por $ w $**.

3. **Distinción entre puntos y direcciones:**  
   - Puntos → $ w = 1 $ (tienen posición)  
   - Vectores → $ w = 0 $ (solo dirección)  
   - Esto permite operaciones consistentes, por ejemplo: trasladar vectores de dirección no los cambia, trasladar puntos sí.

---

#### 2️⃣ Representación de transformaciones con coordenadas homogéneas

**Traslación**

En coordenadas homogéneas:

$$
T =
\begin{bmatrix}
1 & 0 & 0 & t_x \\
0 & 1 & 0 & t_y \\
0 & 0 & 1 & t_z \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

Aplicando a un punto:

$$
\mathbf{p}' = T \cdot \mathbf{p}_h =
\begin{bmatrix}
x + t_x \\
y + t_y \\
z + t_z \\
1
\end{bmatrix}
$$

Si $\mathbf{v}_h$ es un vector $( w=0 )$, la traslación no lo afecta:

$$
\mathbf{v}' = T \cdot \mathbf{v}_h =
\begin{bmatrix}
v_x \\
v_y \\
v_z \\
0
\end{bmatrix}
$$

---

**Rotación y escalado**

Se pueden representar igualmente como matrices 4x4 homogéneas, aplicables tanto a puntos como vectores:

- **Rotación en X:**

$$
R_x(\theta) =
\begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & \cos\theta & -\sin\theta & 0 \\
0 & \sin\theta & \cos\theta & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

- **Escalado:**

$$
S =
\begin{bmatrix}
s_x & 0 & 0 & 0 \\
0 & s_y & 0 & 0 \\
0 & 0 & s_z & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

---

#### 3️⃣ Ventajas de las coordenadas homogéneas

- Permiten **combinar múltiples transformaciones** en una sola multiplicación matricial:

$$
M = T \cdot R \cdot S
$$

- Facilitan el manejo de **proyecciones perspectiva** mediante división por $ w $.  
- Diferencian **puntos de vectores de dirección**, esencial para física y cámaras.  
- Son la base de todos los motores gráficos 3D modernos.


---

## 📐 3. Transformaciones geométricas básicas

### 3.1 Traslación en 3D

La **traslación** es la operación geométrica que permite **mover un objeto de una posición a otra** dentro del espacio tridimensional, sin modificar su orientación ni su tamaño.  
En términos matemáticos, consiste en sumar un vector de desplazamiento a cada punto del objeto.

#### 1️⃣ Representación matemática

Si un punto del espacio tiene coordenadas:

$$
\mathbf{p} =
\begin{bmatrix}
x \\
y \\
z
\end{bmatrix}
$$

y queremos trasladarlo por un vector de desplazamiento:

$$
\mathbf{t} =
\begin{bmatrix}
t_x \\
t_y \\
t_z
\end{bmatrix}
$$

el punto trasladado se obtiene sumando:

$$
\mathbf{p}' = \mathbf{p} + \mathbf{t} =
\begin{bmatrix}
x + t_x \\
y + t_y \\
z + t_z
\end{bmatrix}
$$

---

#### 2️⃣ Representación mediante coordenadas homogéneas

Para integrar la traslación en un **sistema matricial uniforme**, se utilizan coordenadas homogéneas.  
El vector punto se extiende a:

$$
\mathbf{p}_h =
\begin{bmatrix}
x \\
y \\
z \\
1
\end{bmatrix}
$$

y la matriz de traslación se define como:

$$
T =
\begin{bmatrix}
1 & 0 & 0 & t_x \\
0 & 1 & 0 & t_y \\
0 & 0 & 1 & t_z \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

La aplicación de la traslación se realiza mediante multiplicación matricial:

$$
\mathbf{p}'_h = T \cdot \mathbf{p}_h =
\begin{bmatrix}
x + t_x \\
y + t_y \\
z + t_z \\
1
\end{bmatrix}
$$

---

#### 3️⃣ Propiedades de la traslación

1. **Linealidad parcial:**  
   - La traslación es lineal respecto a los vectores de desplazamiento.  
   - Trasladar un objeto por $\mathbf{t}_1$ y luego por $\mathbf{t}_2$ es equivalente a trasladarlo por $\mathbf{t}_1 + \mathbf{t}_2$:

   $$
   T(\mathbf{t}_2) \cdot T(\mathbf{t}_1) = T(\mathbf{t}_1 + \mathbf{t}_2)
   $$

2. **No afecta vectores de dirección:**  
   - Si aplicamos traslación a un vector ($w = 0$), este no se desplaza:

   $$
   T \cdot
   \begin{bmatrix} v_x \\ v_y \\ v_z \\ 0 \end{bmatrix} =
   \begin{bmatrix} v_x \\ v_y \\ v_z \\ 0 \end{bmatrix}
   $$

3. **Independiente de la rotación o escala:**  
   - La traslación se puede combinar con rotaciones y escalados mediante multiplicación matricial:

   $$
   M = T \cdot R \cdot S
   $$

---

#### 4️⃣ Interpretación geométrica

- Cada punto del objeto se **desplaza de manera uniforme** en el espacio.  
- El objeto mantiene su **orientación y forma**, solo cambia su posición.  
- Es la base de cualquier movimiento de cámara, personajes u objetos en un juego 3D.

---

#### 5️⃣ Ejemplo conceptual

Si tenemos un cubo con un vértice en $(1, 2, 3)$ y queremos trasladarlo $ (5, -2, 1) $:

$$
\mathbf{p} = \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}, \quad
\mathbf{t} = \begin{bmatrix} 5 \\ -2 \\ 1 \end{bmatrix}
$$

$$
\mathbf{p}' = \mathbf{p} + \mathbf{t} =
\begin{bmatrix}
6 \\
0 \\
4
\end{bmatrix}
$$

En coordenadas homogéneas:

$$
\mathbf{p}_h =
\begin{bmatrix} 1 \\ 2 \\ 3 \\ 1 \end{bmatrix}, \quad
T =
\begin{bmatrix}
1 & 0 & 0 & 5 \\
0 & 1 & 0 & -2 \\
0 & 0 & 1 & 1 \\
0 & 0 & 0 & 1
\end{bmatrix}, \quad
\mathbf{p}'_h = T \cdot \mathbf{p}_h =
\begin{bmatrix} 6 \\ 0 \\ 4 \\ 1 \end{bmatrix}
$$

---

Esta sección **sienta las bases para comprender cualquier movimiento de objetos en 3D**, y será la primera transformación que combinaremos con rotaciones y escalados en las sesiones posteriores.


### 3.2 Escalado en 3D

El **escalado** es la transformación que permite **cambiar el tamaño de un objeto** en el espacio tridimensional.  
Puede ser **uniforme** (mismo factor en todos los ejes) o **no uniforme / anisotrópico** (diferente factor por eje).

---

#### 1️⃣ Representación matemática

Si un punto tiene coordenadas:

$$
\mathbf{p} =
\begin{bmatrix}
x \\
y \\
z
\end{bmatrix}
$$

y queremos escalarlo por factores $ s_x, s_y, s_z $ en cada eje:

$$
\mathbf{p}' =
\begin{bmatrix}
s_x \cdot x \\
s_y \cdot y \\
s_z \cdot z
\end{bmatrix}
$$

- **Escalado uniforme:** $ s_x = s_y = s_z $ → el objeto mantiene proporciones.  
- **Escalado anisotrópico:** factores diferentes → el objeto puede estirarse o comprimirse en algún eje.

---

#### 2️⃣ Representación mediante coordenadas homogéneas

En coordenadas homogéneas, la matriz de escalado 4×4 es:

$$
S =
\begin{bmatrix}
s_x & 0 & 0 & 0 \\
0 & s_y & 0 & 0 \\
0 & 0 & s_z & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

Aplicando a un punto homogéneo:

$$
\mathbf{p}'_h = S \cdot \mathbf{p}_h =
\begin{bmatrix}
s_x \cdot x \\
s_y \cdot y \\
s_z \cdot z \\
1
\end{bmatrix}
$$

Si el vector es de dirección ($ w = 0 $) también se escala de la misma manera, ya que la componente $ w $ no afecta la multiplicación:

$$
\mathbf{v}'_h = S \cdot \mathbf{v}_h =
\begin{bmatrix}
s_x \cdot v_x \\
s_y \cdot v_y \\
s_z \cdot v_z \\
0
\end{bmatrix}
$$

---

#### 3️⃣ Propiedades del escalado

1. **Combinable con otras transformaciones:**  
   Se puede multiplicar con matrices de rotación y traslación:

   $$
   M = T \cdot R \cdot S
   $$

2. **Efecto acumulativo:**  
   Escalar varias veces por factores diferentes es equivalente a multiplicar los factores:

   $$
   S_2 \cdot S_1 = 
   \begin{bmatrix}
   s_{x2} \cdot s_{x1} & 0 & 0 & 0 \\
   0 & s_{y2} \cdot s_{y1} & 0 & 0 \\
   0 & 0 & s_{z2} \cdot s_{z1} & 0 \\
   0 & 0 & 0 & 1
   \end{bmatrix}
   $$

3. **Origen como referencia:**  
   - El escalado se realiza respecto al **origen de coordenadas** (0,0,0) del espacio.  
   - Si se desea escalar alrededor de otro punto, primero hay que **trasladar el objeto al origen**, escalar y luego trasladarlo de vuelta.

---

#### 4️⃣ Interpretación geométrica

- Cada vértice del objeto se **multiplica por un factor de escala** en cada eje.  
- No cambia la orientación ni la posición relativa al origen (a menos que se combine con traslación).  
- Permite aumentar o reducir objetos, deformarlos, o generar animaciones de crecimiento.

---

#### 5️⃣ Ejemplo conceptual

Supongamos un cubo con un vértice en $(2, 3, 1)$ y queremos escalarlo uniformemente por un factor 2:

$$
\mathbf{p} = \begin{bmatrix} 2 \\ 3 \\ 1 \end{bmatrix}, \quad
s_x = s_y = s_z = 2
$$

$$
\mathbf{p}' =
\begin{bmatrix}
2 \cdot 2 \\
2 \cdot 3 \\
2 \cdot 1
\end{bmatrix} =
\begin{bmatrix}
4 \\
6 \\
2
\end{bmatrix}
$$

Si queremos un escalado anisotrópico: $ s_x = 2, s_y = 1, s_z = 0.5 $:

$$
\mathbf{p}' =
\begin{bmatrix}
2 \cdot 2 \\
1 \cdot 3 \\
0.5 \cdot 1
\end{bmatrix} =
\begin{bmatrix}
4 \\
3 \\
0.5
\end{bmatrix}
$$

---

El **escalado es esencial** en juegos para animaciones, cambios de tamaño dinámicos, deformaciones de personajes y objetos, y para normalizar modelos en la escena.


### 3.3 Rotación en 3D

La **rotación** es la transformación que permite **girar un objeto alrededor de un eje** en el espacio tridimensional, cambiando su orientación sin modificar su posición relativa al origen ni su tamaño.

---

#### 1️⃣ Representación matemática

En 3D, las rotaciones se definen respecto a los ejes principales: X, Y y Z.  
Si un punto tiene coordenadas:

$$
\mathbf{p} =
\begin{bmatrix}
x \\
y \\
z
\end{bmatrix}
$$

y queremos girarlo un ángulo $\theta$ alrededor de uno de los ejes, se aplica la correspondiente **matriz de rotación**.

---

#### 2️⃣ Matrices de rotación en coordenadas homogéneas

- **Rotación alrededor del eje X:**

$$
R_x(\theta) =
\begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & \cos\theta & -\sin\theta & 0 \\
0 & \sin\theta & \cos\theta & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

- **Rotación alrededor del eje Y:**

$$
R_y(\theta) =
\begin{bmatrix}
\cos\theta & 0 & \sin\theta & 0 \\
0 & 1 & 0 & 0 \\
-\sin\theta & 0 & \cos\theta & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

- **Rotación alrededor del eje Z:**

$$
R_z(\theta) =
\begin{bmatrix}
\cos\theta & -\sin\theta & 0 & 0 \\
\sin\theta & \cos\theta & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

Aplicando a un punto homogéneo $\mathbf{p}_h = [x, y, z, 1]^T$:

$$
\mathbf{p}'_h = R \cdot \mathbf{p}_h
$$

---

#### 3️⃣ Propiedades de la rotación

1. **Conserva la distancia y la forma:**  
   - La rotación es una transformación **isométrica**, no altera longitudes ni ángulos internos de los objetos.

2. **No afecta la traslación de vectores de dirección:**  
   - Igual que en traslación y escalado, los vectores de dirección ($w=0$) se rotan de la misma forma que los puntos, sin cambiar su posición relativa al origen.

3. **Composición de rotaciones:**  
   - Rotaciones sucesivas se multiplican mediante matrices:

   $$
   R = R_z(\theta_z) \cdot R_y(\theta_y) \cdot R_x(\theta_x)
   $$

   - **Importante:** el orden de las rotaciones **importa**, ya que las matrices no conmutan:

   $$
   R_x \cdot R_y \neq R_y \cdot R_x
   $$

4. **Rotación alrededor de un punto arbitrario:**  
   - Para rotar alrededor de un punto distinto del origen, se realiza:
     1. Traslación del objeto al origen
     2. Rotación
     3. Traslación de vuelta

---

#### 4️⃣ Interpretación geométrica

- Rotar un objeto en torno a un eje cambia su orientación dentro del espacio 3D.  
- Se utiliza para animaciones, giros de cámaras, objetos móviles, y para alinear modelos con el mundo o la vista de la cámara.

---

#### 5️⃣ Ejemplo conceptual

Supongamos un punto en $(1, 0, 0)$ y queremos rotarlo 90° ($\pi/2$) alrededor del eje Z:

$$
\mathbf{p} = \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}, \quad
R_z\left(\frac{\pi}{2}\right) =
\begin{bmatrix}
0 & -1 & 0 & 0 \\
1 & 0 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

Multiplicando:

$$
\mathbf{p}'_h = R_z \cdot
\begin{bmatrix} 1 \\ 0 \\ 0 \\ 1 \end{bmatrix} =
\begin{bmatrix} 0 \\ 1 \\ 0 \\ 1 \end{bmatrix}
$$

El punto ha girado 90° en sentido antihorario alrededor del eje Z.

---

La **rotación en 3D**, combinada con **traslación y escalado**, forma la base de **todas las transformaciones de objetos en un motor 3D**, y es esencial para la animación y la interacción en videojuegos.


### 3.4. Composición de transformaciones

Las transformaciones se aplican multiplicando matrices:

$$
M = T \cdot R \cdot S
$$

Y el vértice final es:

$$
\mathbf{p}' = M \cdot \mathbf{p}_h
$$

> ⚠️ El orden importa: las multiplicaciones de matrices **no son conmutativas**.

---

### 4. Espacios de coordenadas en 3D

En gráficos 3D es fundamental distinguir entre distintos **espacios de coordenadas**, ya que un objeto puede tener varias posiciones y orientaciones dependiendo de la referencia que usemos.  
Cada transformación depende del **sistema de referencia** en el que se aplique.

---

#### 1️⃣ Espacios principales

| Espacio | Descripción |
|----------|-------------|
| **Local (modelo)** | Sistema de coordenadas propio del objeto. Cada vértice se define relativo al origen del objeto. |
| **Mundo (world)** | Posición global dentro de la escena, aplicando transformaciones del objeto respecto al mundo. |
| **Vista (view)** | Sistema de coordenadas de la cámara, que define qué parte del mundo se observa. |
| **Proyección (clip)** | Coordenadas transformadas y preparadas para proyectarse en la pantalla 2D. |

---

#### 2️⃣ Transformaciones entre espacios

Cada espacio se obtiene aplicando la correspondiente **matriz de transformación**:

1. **Del modelo al mundo:**

$$
V_{mundo} = M_{modelo} \cdot V_{local}
$$

- Multiplica cada vértice por la matriz que contiene **traslación, rotación y escala** del objeto en el mundo.

2. **Del mundo a la vista (cámara):**

$$
V_{vista} = M_{vista} \cdot V_{mundo}
$$

- Aplica la posición y orientación de la cámara, transformando el mundo al punto de vista de la cámara.

3. **De la vista a clip (proyección):**

$$
V_{clip} = P_{proyeccion} \cdot V_{vista}
$$

- Convierte las coordenadas 3D en **coordenadas homogéneas proyectadas**, listas para la rasterización en 2D.

---

#### 3️⃣ Observaciones importantes

1. **Orden de multiplicación:**  
   - Las transformaciones deben aplicarse en el orden correcto: **modelo → mundo → vista → proyección**.  
   - Alterar el orden produce resultados incorrectos.

2. **Múltiples objetos:**  
   - Cada objeto tiene su propia **matriz de modelo**.  
   - El espacio mundo unifica todos los objetos en la escena.

3. **Coherencia de sistemas:**  
   - Todas las operaciones de rotación, traslación y escalado se aplican respecto a **la referencia correcta**.  
   - Ejemplo: rotar un objeto en espacio local gira el objeto alrededor de su propio origen; rotarlo en espacio mundo lo gira respecto al origen global.

---

#### 4️⃣ Ejemplo conceptual

Supongamos un cubo definido en su espacio **local** con vértice:

$$
V_{local} = \begin{bmatrix} 1 \\ 1 \\ 1 \\ 1 \end{bmatrix}
$$

- Su matriz de modelo traslada el cubo a la posición global $(5,0,0)$:

$$
M_{modelo} =
\begin{bmatrix}
1 & 0 & 0 & 5 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

- Vértice en espacio mundo:

$$
V_{mundo} = M_{modelo} \cdot V_{local} =
\begin{bmatrix} 6 \\ 1 \\ 1 \\ 1 \end{bmatrix}
$$

- Luego, aplicando la matriz de cámara (vista) y proyección, se obtiene el vértice listo para renderizar en pantalla 2D.

---

#### 5️⃣ Conclusión

Entender los **espacios de coordenadas** es esencial para:

- Aplicar correctamente transformaciones de objetos y cámaras.  
- Organizar la escena de manera consistente.  
- Implementar proyecciones y renderizado 3D correcto.  

> Los espacios de coordenadas permiten separar **posición interna del objeto**, **ubicación en el mundo** y **perspectiva de la cámara**, facilitando el control total sobre la escena 3D.
---

### 5. Proyección y profundidad

En gráficos 3D, para mostrar los objetos en **una pantalla 2D** necesitamos transformar las coordenadas tridimensionales en coordenadas de pantalla.  
Esto se logra mediante **proyecciones**, que también permiten simular la **profundidad** y la perspectiva.

---

#### 1️⃣ Tipos de proyección

1. **Proyección ortográfica:**  
   - Conserva paralelismo de líneas.  
   - Las dimensiones no se alteran con la distancia.  
   - Ideal para mapas, planos o interfaces 2D dentro del 3D.  

   Matriz de proyección ortográfica:

   $$
   P_{ortho} =
   \begin{bmatrix}
   \frac{2}{r-l} & 0 & 0 & -\frac{r+l}{r-l} \\
   0 & \frac{2}{t-b} & 0 & -\frac{t+b}{t-b} \\
   0 & 0 & -\frac{2}{f-n} & -\frac{f+n}{f-n} \\
   0 & 0 & 0 & 1
   \end{bmatrix}
   $$

   Donde $l, r, b, t, n, f$ son los límites izquierdo, derecho, inferior, superior, cercano y lejano del volumen de visión.

2. **Proyección perspectiva:**  
   - Simula cómo los objetos lejanos se ven más pequeños.  
   - Reproduce la profundidad y la sensación real de 3D.  

   Matriz de proyección perspectiva típica:

   $$
   P_{persp} =
   \begin{bmatrix}
   \frac{f}{aspect} & 0 & 0 & 0 \\
   0 & f & 0 & 0 \\
   0 & 0 & \frac{far + near}{near - far} & \frac{2 \cdot far \cdot near}{near - far} \\
   0 & 0 & -1 & 0
   \end{bmatrix}
   $$

   Donde:  
   - $f = \frac{1}{\tan(\frac{fov}{2})}$ es el factor de escala según el ángulo de visión ($fov$).  
   - $aspect$ es la relación de aspecto de la pantalla.  
   - $near$ y $far$ son los planos cercano y lejano de visión.

---

#### 2️⃣ División por $w$ y coordenadas de pantalla

Tras multiplicar un vértice homogéneo $\mathbf{p}_h$ por la matriz de proyección:

$$
\mathbf{p}_{clip} = P \cdot V_{vista}
$$

Se obtiene un vector homogéneo:

$$
\mathbf{p}_{clip} =
\begin{bmatrix}
x_c \\
y_c \\
z_c \\
w_c
\end{bmatrix}
$$

Para pasar a **coordenadas normalizadas de dispositivo (NDC)**:

$$
x_{ndc} = \frac{x_c}{w_c}, \quad
y_{ndc} = \frac{y_c}{w_c}, \quad
z_{ndc} = \frac{z_c}{w_c}
$$

- Este paso convierte los vértices en **valores entre -1 y 1**, listos para mapear a píxeles de pantalla.  
- La división por $w$ también implementa el **efecto de perspectiva**: objetos lejanos se ven más pequeños.

---

#### 3️⃣ Interpretación geométrica

- La **proyección transforma 3D a 2D**, manteniendo información de profundidad.  
- Permite al motor de renderizado determinar **qué objetos se ven y cómo se ven**.  
- Junto con los **espacios de coordenadas**, completa la cadena:

$$
V_{local} \xrightarrow{M_{modelo}} V_{mundo} \xrightarrow{M_{vista}} V_{vista} \xrightarrow{P_{proyeccion}} V_{clip} \xrightarrow{/w} V_{ndc}
$$

- Después de esta etapa, los valores NDC se transforman a **coordenadas de pantalla** para dibujar los píxeles.

---

#### 4️⃣ Ejemplo conceptual

Un vértice en espacio vista:

$$
V_{vista} = \begin{bmatrix} 2 \\ 1 \\ -5 \\ 1 \end{bmatrix}
$$

Aplicando proyección perspectiva con:

- $fov = 90^\circ$, $aspect = 1.0$, $near = 1$, $far = 10$  

Obtenemos:

$$
V_{clip} =
\begin{bmatrix}
2 \\
1 \\
z_c \\
5
\end{bmatrix} \quad (\text{valores aproximados})
$$

Dividiendo por $w = 5$ para normalizar:

$$
V_{ndc} =
\begin{bmatrix}
0.4 \\
0.2 \\
z_{ndc}
\end{bmatrix}
$$

- El punto queda listo para mapearse a la pantalla, mostrando la **reducción de tamaño por la distancia** y conservando la **profundidad**.

---

### 6. Uso de matrices para transformaciones en 3D

En gráficos 3D, todas las transformaciones básicas —**traslación, escalado y rotación**— se pueden representar mediante **matrices 4x4** aplicadas a vectores en **coordenadas homogéneas**. Esto permite combinar varias transformaciones de manera eficiente y coherente.

---

#### 1️⃣ Representación de vértices y objetos

Cada objeto 3D se puede representar como una **matriz de vértices**, donde cada fila corresponde a un vértice en coordenadas homogéneas:

$$
V =
\begin{bmatrix}
x_1 & y_1 & z_1 & 1 \\
x_2 & y_2 & z_2 & 1 \\
\vdots & \vdots & \vdots & \vdots \\
x_n & y_n & z_n & 1
\end{bmatrix}
$$

- La cuarta columna $w=1$ permite aplicar **traslaciones mediante multiplicación matricial**.

---

#### 2️⃣ Matrices de transformación

- **Traslación**:

$$
T =
\begin{bmatrix}
1 & 0 & 0 & t_x \\
0 & 1 & 0 & t_y \\
0 & 0 & 1 & t_z \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

- **Escalado**:

$$
S =
\begin{bmatrix}
s_x & 0 & 0 & 0 \\
0 & s_y & 0 & 0 \\
0 & 0 & s_z & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

- **Rotación alrededor de Z**:

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

#### 3️⃣ Aplicación de transformaciones

Para transformar un objeto, se multiplican las matrices de transformación en el orden deseado y luego se aplican a los vértices:

$$
V' = V \cdot (T \cdot R \cdot S)^T
$$

- El orden de multiplicación importa: **escalado → rotación → traslación**.  
- Se obtiene un **nuevo conjunto de vértices**, con posición, orientación y tamaño actualizados.

---

#### 4️⃣ Ejemplo conceptual

Supongamos un cubo con un vértice en $(1, 1, 1)$:

1. Escalar uniformemente por 2 → $(2, 2, 2)$  
2. Rotar 90° alrededor del eje Z → $(-2, 2, 2)$  
3. Trasladar a $(5, 0, 2)$ → $(3, 2, 4)$  

> Cada operación se puede representar mediante la correspondiente **matriz 4x4**, y aplicarlas secuencialmente permite calcular el resultado final de manera sistemática.

---

#### 5️⃣ Conclusión

El uso de **matrices para transformaciones** permite:

- Aplicar **cualquier combinación de traslación, rotación y escalado** de forma consistente.  
- Facilitar la manipulación de múltiples objetos en un **motor 3D**.  
- Experimentar con transformaciones conceptualmente antes de implementar renderizado o animaciones.

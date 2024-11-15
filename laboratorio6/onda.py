import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

def ecuacion_onda(f, g, alfa, beta, a, b, c, h, k):
    # Definir el numero de pasos espaciales (n) y temporales (m)
    n = int(a / h) + 1
    m = int(b / k) + 1
    
    # Parametro de estabilidad
    r = c * k / h
    if r > 1:
        raise ValueError("El esquema es inestable. Asegurate de que c*k/h <= 1.")

    # Inicializar la matriz u para almacenar los valores de la solucion
    u = np.zeros((n, m))

    # Condiciones iniciales en el tiempo t=0
    u[:, 0] = f(np.arange(0, n) * h)
    
    # Condiciones de velocidad inicial en t=0 (la primera derivada de u respecto al tiempo)
    u[:, 1] = u[:, 0] + k * g(np.arange(0, n) * h)
    
    # Condiciones en la frontera (para todas las filas en los extremos de x)
    for j in range(m):
        u[0, j] = alfa(j * k)   # Frontera izquierda
        u[-1, j] = beta(j * k)  # Frontera derecha

    # Calcular la solucion usando diferencias finitas para la ecuacion de onda
    for j in range(1, m - 1):
        for i in range(1, n - 1):
            u[i, j + 1] = 2 * u[i, j] - u[i, j - 1] + r**2 * (u[i + 1, j] - 2 * u[i, j] + u[i - 1, j])

    return u

# Caso 1: Condicion inicial senoidal y velocidad cero
def f_senoidal(x):
    # Desplazamiento inicial en funcion senoidal
    return np.sin(np.pi * x)

def g_senoidal(x):
    # Velocidad inicial cero para el caso senoidal
    return np.zeros_like(x)

# Caso 2: Condicion inicial escalonada y velocidad no cero
def f_escalonada(x):
    # Desplazamiento inicial en forma escalonada
    return np.where(x < 0.5, 1, 0)

def g_escalonada(x):
    # Velocidad inicial no cero para el caso escalonada
    return np.sin(np.pi * x)

# Condiciones en la frontera alfa(x) y beta(x)
def alfa(t):
    # Frontera izquierda
    return 0

def beta(t):
    # Frontera derecha
    return 0

# Parametros comunes
a = 1      # Longitud del dominio espacial
b = 1      # Tiempo total
c = 1      # Velocidad de propagacion de la onda
h = 0.05   # Tamano del paso en x
k = 0.005  # Tamano del paso en t

# Ejecutar la funcion y obtener la solucion para el caso 1 (senoidal)
u_senoidal = ecuacion_onda(f_senoidal, g_senoidal, alfa, beta, a, b, c, h, k)

# Ejecutar la funcion y obtener la solucion para el caso 2 (escalonada)
u_escalonada = ecuacion_onda(f_escalonada, g_escalonada, alfa, beta, a, b, c, h, k)

# Graficar el mapa de la onda en 3D para el caso senoidal
fig = plt.figure()

# Subgrafico para el caso senoidal
ax = fig.add_subplot(121, projection='3d')
x = np.linspace(0, a, u_senoidal.shape[0])
t = np.linspace(0, b, u_senoidal.shape[1])
X, T = np.meshgrid(t, x)

# Dibujar la superficie para el caso senoidal
ax.plot_surface(X, T, u_senoidal, cmap=cm.jet)
ax.set_xlabel('Tiempo')
ax.set_ylabel('Posicion')
ax.set_zlabel('Desplazamiento')
ax.set_title("Caso 1: Condicion Inicial Senoidal")

# Subgrafico para el caso escalonada
ax2 = fig.add_subplot(122, projection='3d')

# Dibujar la superficie para el caso escalonada
ax2.plot_surface(X, T, u_escalonada, cmap=cm.jet)
ax2.set_xlabel('Tiempo')
ax2.set_ylabel('Posicion')
ax2.set_zlabel('Desplazamiento')
ax2.set_title("Caso 2: Condicion Inicial Escalonada")

# Ajustar el layout de los graficos
plt.tight_layout()

# Mostrar los graficos
plt.show()

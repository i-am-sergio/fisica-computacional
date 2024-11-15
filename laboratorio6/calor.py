import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

def calor(f, alfa, beta, a, b, c, h, k):
    # Definir el numero de pasos espaciales (n) y temporales (m)
    n = int(a / h) + 1
    m = int(b / k) + 1
    
    # Parametro de estabilidad
    r = c * k / (h**2)
    if r > 0.5:
        raise ValueError("El esquema es inestable. Asegurate de que c*k/h^2 <= 0.5.")

    # Inicializar la matriz u para almacenar los valores de la solucion
    u = np.zeros((n, m))

    # Condiciones iniciales en el tiempo t=0
    u[:, 0] = f(np.arange(0, n) * h)
    
    # Condiciones en la frontera (para todas las filas en los extremos de x)
    for j in range(m):
        u[0, j] = alfa(j * k)   # Frontera izquierda
        u[-1, j] = beta(j * k)  # Frontera derecha

    # Calcular la solucion usando diferencias finitas
    for j in range(0, m - 1):
        for i in range(1, n - 1):
            u[i, j + 1] = u[i, j] + r * (u[i + 1, j] - 2 * u[i, j] + u[i - 1, j])
    
    return u


# Caso 1: Condicion inicial senoidal
def f_senoidal(x):
    # Funcion senoidal de temperatura inicial
    return np.sin(np.pi * x)

# Caso 2: Condicion inicial gaussiana
def f_gaussiana(x):
    # Parametros de la distribucion gaussiana
    sigma = 0.2  # Ancho de la campana
    mu = 0.75    # Media (centro del dominio)
    return np.exp(-(x - mu)**2 / (2 * sigma**2))

# Condiciones de frontera alfa(t) y beta(t)
def alfa(t):
    # Condicion de frontera izquierda (temperatura constante 0)
    return 0

def beta(t):
    # Condicion de frontera derecha (temperatura constante 0)
    return 0


# Parametros comunes
a = 1      # Longitud del dominio espacial
b = 1      # Tiempo total
c = 1      # Coeficiente de difusion
h = 0.1    # Tamano del paso en x
k = 0.005  # Tamano del paso en t

# Ejecutar la funcion y obtener la solucion para el caso 1 (senoidal)
u_senoidal = calor(f_senoidal, alfa, beta, a, b, c, h, k)

# Ejecutar la funcion y obtener la solucion para el caso 2 (gaussiana)
u_gaussiana = calor(f_gaussiana, alfa, beta, a, b, c, h, k)

# Graficar el mapa de calor en 3D para el caso senoidal
fig = plt.figure()
ax = fig.add_subplot(121, projection='3d')

x = np.linspace(0, a, u_senoidal.shape[0])
t = np.linspace(0, b, u_senoidal.shape[1])
X, T = np.meshgrid(t, x)

# Dibujar la superficie para el caso senoidal
ax.plot_surface(X, T, u_senoidal, cmap=cm.jet)
ax.set_xlabel('Tiempo')
ax.set_ylabel('Posicion')
ax.set_zlabel('Temperatura')
ax.set_title("Caso 1: Condicion Inicial Senoidal")

# Graficar el mapa de calor en 3D para el caso gaussiano
ax2 = fig.add_subplot(122, projection='3d')

# Dibujar la superficie para el caso gaussiano
ax2.plot_surface(X, T, u_gaussiana, cmap=cm.jet)
ax2.set_xlabel('Tiempo')
ax2.set_ylabel('Posicion')
ax2.set_zlabel('Temperatura')
ax2.set_title("Caso 2: Condicion Inicial Gaussiana")

# Ajustar el layout de los graficos
plt.tight_layout()

# Mostrar los graficos
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Parámetros del móvil
m = 1000  # masa en kg
v_i = 10  # velocidad inicial en m/s
v_f = 180  # velocidad final en m/s
t = 100   # tiempo en segundos

# Cálculo de la aceleración
a = (v_f - v_i) / t

# Cálculo de la fuerza aplicada
F = m * a

# Generar datos para graficar la velocidad en función del tiempo
time = np.linspace(0, t, 100)  # 100 puntos entre 0 y t
velocities = v_i + a * time  # ecuación de la velocidad

# Graficar el cambio de velocidad
plt.figure()
plt.plot(time, velocities, label='Velocidad (m/s)', color='tomato')
plt.xlabel('Tiempo (s)')
plt.ylabel('Velocidad (m/s)')
plt.title('Cambio de velocidad de un móvil')
plt.legend()
plt.grid(True)
plt.show()

# Imprimir resultados
print(f"Aceleración: {a:.2f} m/s^2")
print(f"Fuerza aplicada: {F:.2f} N")

# Graficar distancia - tiempo
# Usar el mismo arreglo de tiempo para calcular distancias
distances = v_i * time + 0.5 * a * time**2  # ecuación de la distancia

plt.figure()
plt.plot(time, distances, label='Distancia (m)', color='chartreuse')
plt.xlabel('Tiempo (s)')
plt.ylabel('Distancia (m)')
plt.title('Distancia recorrida por un móvil')
plt.legend()
plt.grid(True)
plt.show()

# Imprimir resultados de distancia
print(f"Distancia recorrida: {distances[-1]:.2f} m")

# Graficar aceleración - tiempo
acceleration_time = np.full_like(time, a)  # Crear un arreglo constante para la aceleración

plt.figure()
plt.plot(time, acceleration_time, label='Aceleración (m/s^2)', color='royalblue')
plt.xlabel('Tiempo (s)')
plt.ylabel('Aceleración (m/s²)')
plt.title('Aceleración de un móvil')
plt.legend()
plt.grid(True)
plt.show()

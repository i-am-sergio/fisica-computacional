import numpy as np
import matplotlib.pyplot as plt

# Parámetros iniciales
m = 0.01  # masa (kg)
v0 = 8.0  # velocidad inicial (m/s)
y0 = 0.0  # altura inicial (m)
g = 9.81  # aceleración debida a la gravedad (m/s^2)

# Condiciones iniciales
v = v0
y = y0
t0 = 0.0
dt = 0.001  # paso de tiempo (segundos)
t_end = 2.0  # tiempo final de simulación (segundos)

# Listas para almacenar resultados
times = []
heights = []
velocities = []
ek_values = []
ep_values = []
em_values = []

# Integración numérica (Método de Euler)
t = t0
while t <= t_end:
    # Guardar los resultados en cada paso
    times.append(t)
    heights.append(y)
    velocities.append(v)
    
    EK = 0.5 * m * v**2
    EP = m * g * y
    Em = EK + EP
    ek_values.append(EK)
    ep_values.append(EP)
    em_values.append(Em)
    
    # Actualización de las variables usando el método de Euler
    v = v - g * dt  # velocidad (v = v0 - g * t)
    y = y + v * dt  # posición (y = y0 + v * t)
    
    # Avanzar al siguiente tiempo
    t += dt

    # Detener el ciclo cuando la velocidad se vuelve negativa (cuando el objeto empieza a caer)
    if v < 0 and y > 0:
        break

# Altura máxima alcanzada
max_height = max(heights)

# Graficar los resultados
plt.figure(figsize=(10, 6))

# Energías
plt.subplot(3, 1, 1)
plt.plot(times, ek_values, label='Energía Cinética')
plt.plot(times, ep_values, label='Energía Potencial')
plt.plot(times, em_values, label='Energía Total')
plt.xlabel('Tiempo (s)')
plt.ylabel('Energía (J)')
plt.legend()

# Altura
plt.subplot(3, 1, 2)
plt.plot(times, heights, label='Altura')
plt.xlabel('Tiempo (s)')
plt.ylabel('Altura (m)')
plt.legend()

# Velocidad
plt.subplot(3, 1, 3)
plt.plot(times, velocities, label='Velocidad')
plt.xlabel('Tiempo (s)')
plt.ylabel('Velocidad (m/s)')
plt.legend()

plt.tight_layout()
plt.show()

# Mostrar la altura máxima
print(f"La altura máxima alcanzada es: {max_height:.2f} metros.")

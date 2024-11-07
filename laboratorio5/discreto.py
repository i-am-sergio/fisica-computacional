import numpy as np
import matplotlib.pyplot as plt

# Función para validar la entrada numérica
def input_positivo(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor > 0:
                return valor
            else:
                print("El valor debe ser mayor a 0.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

# Función para ingresar un número sin restricciones
def input_sin_restriccion(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            return valor
        except ValueError:
            print("Por favor, ingrese un número válido.")

# Función para calcular energías cinética, potencial y mecánica total
def calcular_energias(m, v_initial, g, t_max, num_points=10):
    time_points = np.linspace(0, t_max, num_points)  # puntos de tiempo para evaluar
    kinetic_energy = []
    potential_energy = []
    total_energy = []

    # Cálculo de energías en cada instante
    for t in time_points:
        # Altura y velocidad en cada instante
        h = v_initial * t - 0.5 * g * t**2
        v = v_initial - g * t

        # Energías
        EK = 0.5 * m * v**2  # Energía cinética
        EP = m * g * h       # Energía potencial
        Em = EK + EP         # Energía mecánica total

        # Guardar los valores en listas
        kinetic_energy.append(EK)
        potential_energy.append(EP)
        total_energy.append(Em)
    
    return time_points, kinetic_energy, potential_energy, total_energy

# Función para graficar energía vs. tiempo con puntos y valores de energía
def energia_vs_tiempo(time_points, kinetic_energy, potential_energy, total_energy):
    plt.figure(figsize=(12, 8))

    # Energía Cinética con puntos y valores
    plt.plot(time_points, kinetic_energy, label="Energía Cinética (EK)", color="slateblue", marker='o')
    for i, ek in enumerate(kinetic_energy):
        plt.text(time_points[i], ek, f"{ek:.2f} J", ha='right', color="slateblue", fontsize=8)

    # Energía Potencial con puntos y valores
    plt.plot(time_points, potential_energy, label="Energía Potencial (EP)", color="orange", marker='o')
    for i, ep in enumerate(potential_energy):
        plt.text(time_points[i], ep, f"{ep:.2f} J", ha='right', color="orange", fontsize=8)

    # Energía Mecánica Total con puntos y valores
    plt.plot(time_points, total_energy, label="Energía Mecánica Total (Em)", color="seagreen", linestyle="--", marker='o')
    for i, em in enumerate(total_energy):
        plt.text(time_points[i], em, f"{em:.2f} J", ha='right', color="seagreen", fontsize=8)

    # Etiquetas y leyenda
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Energía (J)")
    plt.title("Conservación de la Energía de una Pelota Lanzada Hacia Arriba")
    plt.legend()
    plt.grid()
    plt.show()



# # Datos del problema
# m = 0.01  # masa en kg
# v_initial = 8.0  # velocidad inicial en m/s
# g = 9.81  # gravedad en m/s^2
# t_max = v_initial / g  # tiempo hasta que la velocidad se hace cero (v = 0)

# Ingreso de datos validados
print("========== CONSERVACIÓN DE LA ENERGÍA ==========")
m = input_positivo("Masa del objeto (kg): ")
v_initial = input_sin_restriccion("Velocidad inicial (m/s): ")
g = input_positivo("Aceleración debida a la gravedad (m/s^2): ")

# Cálculo del tiempo hasta que la velocidad se hace cero
t_max = v_initial / g

# Imprimir datos iniciales
print(f"Datos Iniciales:")
print(f"Masa del objeto: {m} kg")
print(f"Velocidad inicial: {v_initial} m/s")
print(f"Aceleración debida a la gravedad: {g} m/s^2")
print(f"Tiempo hasta que la velocidad se hace cero: {t_max:.2f} s\n")

# Calcular energías
time_points, kinetic_energy, potential_energy, total_energy = calcular_energias(m, v_initial, g, t_max)

# Imprimir velocidad, altura y energías en cada instante
for i in range(len(time_points)):
    print(f"[{i}] => Tiempo: {time_points[i]:.2f} s | Altura: {v_initial * time_points[i] - 0.5 * g * time_points[i]**2:.2f} m | Velocidad: {v_initial - g * time_points[i]:.2f} m/s | EK: {kinetic_energy[i]:.2f} J | EP: {potential_energy[i]:.2f} J | Em: {total_energy[i]:.2f} J")

# Imprimit resultados finales de energías
print(f"\nResultados Finales:")
print(f"Energía Cinética Final (EK): {kinetic_energy[-1]:.2f} J")
print(f"Energía Potencial Final (EP): {potential_energy[-1]:.2f} J")
print(f"Energía Mecánica Final (Em): {total_energy[-1]:.2f} J")
print(f"Altura Final: {v_initial * time_points[-1] - 0.5 * g * time_points[-1]**2:.2f} m")

# Graficar energías
energia_vs_tiempo(time_points, kinetic_energy, potential_energy, total_energy)

# Problema 1:
"""
Una pelota de masa m = 0.01kg (10g) es lanzada hacia arriba con una velocidad inicial de v=8m/s. 
Mientras sube, alcanza una altura máxima hasta donde la energía cinética se convierte totalmente en energía potencial. 
No hay resistencia del aire.

a) ¿Cuál es la energía cinética inicial de la pelota al momento de ser lanzada?
b) ¿Cuál es la altura máxima que alcanza la pelota?
c) Calcula y grafica la energía cinética y la energía potencial gravitatoria 
de la pelota en función del tiempo hasta que llega a su altura máxima.
"""
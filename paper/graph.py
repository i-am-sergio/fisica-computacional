import numpy as np
import matplotlib.pyplot as plt

# Simulación de datos para gráficos
np.random.seed(42)
E = np.linspace(20, 120, 100)  # Energías
um_observado = np.log10(0.02 + 0.0001 * (E - 20)**2)  # Coeficiente observado

# Coeficientes ajustados (simulación de resultados)
def ajuste(x, a0, a1, a2, a3, a4, a5):
    return a0 + a1 * x + a2 * x**2 + a3 * x**3 + a4 * x**4 + a5 * x**5

coef_ajustados = [0.02, -0.01, 0.005, -0.0001, 1e-6, -1e-8]
El = np.log10(E)
um_ajustado = ajuste(El, *coef_ajustados)

# Curva de transmisión (simulación de datos observados y ajustados)
d = np.linspace(0, 10, 100)  # Espesor
T_observado = 0.8 * np.exp(-0.02 * d) + 0.2 * np.exp(-0.01 * d)
T_ajustado = 0.75 * np.exp(-0.021 * d) + 0.25 * np.exp(-0.0095 * d)

# Espectro de energía (simulación de resultados)
F = np.exp(-0.1 * (E - 60)**2) + 0.3 * np.exp(-0.05 * (E - 90)**2)
F /= F.max()  # Normalización

# Gráfico 1: Ajuste del coeficiente de atenuación másico
plt.figure(figsize=(8, 6))
plt.plot(E, um_observado, 'o', label="Observado", markersize=5)
plt.plot(E, 10**um_ajustado, '-', label="Ajustado")
plt.xlabel("Energía (keV)")
plt.ylabel("Coeficiente de Atenuación Másico (μ/ρ)")
plt.title("Ajuste del Coeficiente de Atenuación Másico")
plt.legend()
plt.grid()
plt.show()
# plt.savefig("ajuste.png")

# Gráfico 2: Curva de transmisión
plt.figure(figsize=(8, 6))
plt.plot(d, T_observado, 'o', label="Observado", markersize=5)
plt.plot(d, T_ajustado, '-', label="Ajustado")
plt.xlabel("Espesor (cm)")
plt.ylabel("Transmisión")
plt.title("Curva de Transmisión")
plt.legend()
plt.grid()
plt.show()  # Mostrar el gráfico
# plt.savefig("transmision.png")

# Gráfico 3: Espectro de energía reconstruido
plt.figure(figsize=(8, 6))
plt.plot(E, F, '-', label="Espectro Reconstruido")
plt.xlabel("Energía (keV)")
plt.ylabel("Intensidad (normalizada)")
plt.title("Espectro de Energía del Haz de Rayos X")
plt.legend()
plt.grid()
plt.show()  # Mostrar el gráfico
# plt.savefig("espectro.png")

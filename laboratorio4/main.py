import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Método de aproximación discreta
def work_discrete(F, a, b, n):
    dx = (b - a) / n  # Ancho de los intervalos
    work = 0.0
    x_values = np.linspace(a, b, n)

    for x in x_values:
        # Sumar el trabajo de cada segmento
        work += F(x) * dx

    return work, x_values

# Método continuo (integración)
def work_continuous(F, a, b):
    work, _ = quad(F, a, b)
    return work

# Funciones de fuerza
def F_cos(x):
    return np.cos(x)

def F_sin(x):
    return np.sin(x)

def F_exp(x):
    return np.exp(x)

def F_quad(x):
    return 0.5 * x**2 - 2 * x + 3

# Función para calcular trabajo y graficar
def calculate_and_plot(F, a, b, n, label):
    work_d, x_values = work_discrete(F, a, b, n)
    work_c = work_continuous(F, a, b)

    print(f"Trabajo (Método Discreto) para {label}: {work_d:.6f} J")
    print(f"Trabajo (Método Continuo) para {label}: {work_c:.6f} J")

    plt.figure(figsize=(14, 6))

    # Gráfico del método discreto
    plt.subplot(1, 2, 1)
    plt.bar(x_values, F(x_values), width=(b - a) / n, alpha=0.5, align='edge', color='blue')
    plt.title(f'Método Discreto: Aproximación del Trabajo ({label})')
    plt.xlabel('Posición (x)')
    plt.ylabel('Fuerza (F)')
    plt.axhline(0, color='black', lw=0.5, ls='--')
    plt.axvline(0, color='black', lw=0.5, ls='--')
    plt.grid()

    # Gráfico del método continuo
    x = np.linspace(a, b, 100)
    plt.subplot(1, 2, 2)
    plt.plot(x, F(x), label=f'Fuerza: F(x) = {label}', color='orange')
    plt.fill_between(x, F(x), alpha=0.3, color='orange')
    plt.title(f'Método Continuo: Integral del Trabajo ({label})')
    plt.xlabel('Posición (x)')
    plt.ylabel('Fuerza (F)')
    plt.axhline(0, color='black', lw=0.5, ls='--')
    plt.axvline(0, color='black', lw=0.5, ls='--')
    plt.legend()
    plt.grid()

    plt.tight_layout()
    plt.show()

# Parámetros
n = 50  # Número de intervalos

# Calcular y graficar para cada función
calculate_and_plot(F_cos, 0, np.pi / 2, n, 'cos(x)')
calculate_and_plot(F_sin, 0, np.pi, n, 'sin(x)')
calculate_and_plot(F_exp, 0, 1, n, 'e^x')
calculate_and_plot(F_quad, 0, 4, n, '0.5x^2 - 2x + 3')

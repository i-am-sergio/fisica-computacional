import random
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Función para realizar la integración por Monte Carlo
def monte_carlo_integration(func, a, b, num_points=10000, visualize=False):
    # Generar puntos aleatorios
    x_random = np.random.uniform(a, b, num_points)
    y_max = max(func(x) for x in np.linspace(a, b, 1000))
    y_random = np.random.uniform(0, y_max, num_points)

    # Identificar puntos bajo y sobre la curva
    under_curve = y_random <= func(x_random)
    over_curve = ~under_curve

    # Calcular el área bajo la curva
    area_rectangle = (b - a) * y_max
    integral = (under_curve.sum() / num_points) * area_rectangle

    if visualize:
        # Gráfico con seaborn
        sns.set_theme(style="whitegrid")
        plt.figure(figsize=(10, 6))

        # Curva de la función
        x = np.linspace(a, b, 1000)
        y = func(x)
        sns.lineplot(x=x, y=y, label='Función', color='blue', linewidth=2.5)

        # Puntos bajo la curva
        sns.scatterplot(x=x_random[under_curve], y=y_random[under_curve],
                        color='green', s=5, label='Puntos bajo la curva', alpha=0.6)

        # Puntos sobre la curva
        sns.scatterplot(x=x_random[over_curve], y=y_random[over_curve],
                        color='red', s=5, label='Puntos sobre la curva', alpha=0.6)

        # Configuración del gráfico
        plt.title('Integración Monte Carlo', fontsize=14)
        plt.xlabel('x', fontsize=12)
        plt.ylabel('f(x)', fontsize=12)
        plt.legend(fontsize=10)
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.show()

    return integral

# Ejercicio 1: I[g(X)] = ∫[0,1] exp(x^2) dx
def func1(x):
    return np.exp(x**2)

# Ejercicio 2: I[g(X)] = ∫[-1,1] exp(x^4) dx
def func2(x):
    return np.exp(x**4)

# Ejercicio 3: I[g(X)] = ∫[0,1] (1 - exp(x^2))^(1/2) dx
def func3(x):
    return np.sqrt(np.maximum(1 - np.exp(x**2), 0))  

# Ejercicio 4: I[g(X)] = ∫[0,∞] x(1 + x^2)^(-2) dx
def func4(x):
    return x * (1 + x**2)**(-2)

# Ejercicio 5: I[g(X)] = ∫[0,1] exp(x + x^2) dx
def func5(x):
    return np.exp(x + x**2)

# Ejercicio 6: I[g(X)] = ∫[0,∞] exp(-x) dx
def func6(x):
    return np.exp(-x)

# Ejercicio 7: I[g(X)] = ∫[0,∞] (1 - x^2)^(3/2) dx
def func7(x):
    return (1 - x**2)**(3/2)

# Parámetros de la integral
num_points = 10000  # Número de puntos aleatorios

def menu():
    print("1. I[g(X)] = ∫[0,1] exp(x^2) dx")
    print("2. I[g(X)] = ∫[-1,1] exp(x^4) dx")
    print("3. I[g(X)] = ∫[0,1] (1 - exp(x^2))^(1/2) dx")
    print("4. I[g(X)] = ∫[0,∞] x(1 + x^2)^(-2) dx")
    print("5. I[g(X)] = ∫[0,1] exp(x + x^2) dx")
    print("6. I[g(X)] = ∫[0,∞] exp(-x) dx")
    print("7. I[g(X)] = ∫[0,∞] (1 - x^2)^(3/2) dx")
    op = int(input("Ingrese el número del ejercicio que desea realizar => "))

    if op == 1:
        result1 = monte_carlo_integration(func1, 0, 1, num_points, visualize=True)
        print(f"Ejercicio 1: La aproximación de la integral es: {result1}")
    elif op == 2:
        result2 = monte_carlo_integration(func2, -1, 1, num_points, visualize=True)
        print(f"Ejercicio 2: La aproximación de la integral es: {result2}")
    elif op == 3:
        result3 = monte_carlo_integration(func3, 0, 1, num_points, visualize=True)
        print(f"Ejercicio 3: La aproximación de la integral es: {result3}")
    elif op == 4:
        result4 = monte_carlo_integration(func4, 0, 10, num_points, visualize=True)
        print(f"Ejercicio 4: La aproximación de la integral es: {result4}")
    elif op == 5:
        result5 = monte_carlo_integration(func5, 0, 1, num_points, visualize=True)
        print(f"Ejercicio 5: La aproximación de la integral es: {result5}")
    elif op == 6:
        result6 = monte_carlo_integration(func6, 0, 10, num_points, visualize=True)
        print(f"Ejercicio 6: La aproximación de la integral es: {result6}")
    elif op == 7:
        result7 = monte_carlo_integration(func7, 0, 1, num_points, visualize=True)
        print(f"Ejercicio 7: La aproximación de la integral es: {result7}")

while True:
    menu()


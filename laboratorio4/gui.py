import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
import tkinter as tk
from tkinter import ttk

# Funciones de fuerza
def F_cos(x):
    return np.cos(x)

def F_sin(x):
    return np.sin(x)

def F_exp(x):
    return np.exp(x)

def F_quad(x):
    return 0.5 * x**2 - 2 * x + 3

# Métodos de trabajo
def work_discrete(F, a, b, n):
    dx = (b - a) / n
    work = 0.0
    x_values = np.linspace(a, b, n)
    for x in x_values:
        work += F(x) * dx
    return work, x_values

def work_continuous(F, a, b):
    work, _ = quad(F, a, b)
    return work

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

# Función para obtener los valores y graficar
def plot_function():
    a = float(entry_a.get())
    b = float(entry_b.get())
    n = int(entry_n.get())
    selected_function = function_var.get()

    if selected_function == "cos(x)":
        F = F_cos
        label = "cos(x)"
    elif selected_function == "sin(x)":
        F = F_sin
        label = "sin(x)"
    elif selected_function == "e^x":
        F = F_exp
        label = "e^x"
    elif selected_function == "0.5x^2 - 2x + 3":
        F = F_quad
        label = "0.5x^2 - 2x + 3"

    calculate_and_plot(F, a, b, n, label)

# Crear la ventana principal
root = tk.Tk()
root.title("Cálculo de Trabajo")
root.geometry("400x400")
root.configure(bg='#91eb81')

# Estilo para widgets
style = ttk.Style()
style.configure("TLabel", font=("Arial", 12))
style.configure("TEntry", font=("Arial", 12), padding=5)
style.configure("TButton", font=("Arial", 12), padding=5)
style.configure("TCombobox", font=("Arial", 12), padding=5)

# Selector de función
function_var = tk.StringVar(value="cos(x)")
functions = ["cos(x)", "sin(x)", "e^x", "0.5x^2 - 2x + 3"]
function_label = ttk.Label(root, text="Seleccione la función:")
function_label.pack(pady=10)
function_dropdown = ttk.Combobox(root, textvariable=function_var, values=functions)
function_dropdown.pack(pady=10)

# Entradas para los límites y el número de intervalos
limits_frame = ttk.LabelFrame(root, text="Límites y Número de Intervalos", padding=(10, 10))
limits_frame.pack(padx=10, pady=10)

ttk.Label(limits_frame, text="Límite Inferior (a):").grid(row=0, column=0, sticky="w")
entry_a = ttk.Entry(limits_frame)
entry_a.grid(row=0, column=1)
entry_a.insert(0, "0")  # Valor por defecto
ttk.Label(limits_frame, text="Límite Superior (b):").grid(row=1, column=0, sticky="w")
entry_b = ttk.Entry(limits_frame)
entry_b.grid(row=1, column=1)
entry_b.insert(0, "4")  # Valor por defecto para la función cuadrática
ttk.Label(limits_frame, text="Número de Intervalos (n):").grid(row=2, column=0, sticky="w")
entry_n = ttk.Entry(limits_frame)
entry_n.grid(row=2, column=1)
entry_n.insert(0, "50")  # Valor por defecto

# Botón para calcular y graficar
calculate_button = ttk.Button(root, text="Calcular y Graficar", command=plot_function)
calculate_button.pack(pady=20)

# Iniciar el bucle principal
root.mainloop()
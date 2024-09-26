import tkinter as tk
from tkinter import messagebox

def calcular_desplazamiento_uniforme(v, delta_t):
    return v * delta_t  # desplazamiento en metros

def calcular_desplazamiento_acelerado(Vi, alpha, delta_t):
    return Vi * delta_t + 0.5 * alpha * delta_t**2  # desplazamiento en metros

def calcular_velocidad_final(Vi, alpha, delta_t):
    return Vi + alpha * delta_t  # velocidad final en m/s

def realizar_calculo():
    try:
        opcion = var_opcion.get()
        if opcion == 1:
            v = float(entry_v.get())
            delta_t = float(entry_delta_t.get())
            resultado = calcular_desplazamiento_uniforme(v, delta_t)
            messagebox.showinfo("Resultado", f"Desplazamiento: Δx = {resultado:.2f} metros")
        elif opcion == 2:
            Vi = float(entry_vi.get())
            alpha = float(entry_alpha.get())
            delta_t = float(entry_delta_t.get())
            resultado = calcular_desplazamiento_acelerado(Vi, alpha, delta_t)
            messagebox.showinfo("Resultado", f"Desplazamiento: Δx = {resultado:.2f} metros")
        elif opcion == 3:
            Vi = float(entry_vi.get())
            alpha = float(entry_alpha.get())
            delta_t = float(entry_delta_t.get())
            resultado = calcular_velocidad_final(Vi, alpha, delta_t)
            messagebox.showinfo("Resultado", f"Velocidad final: Vf = {resultado:.2f} m/s")
        else:
            messagebox.showwarning("Advertencia", "Seleccione una opción válida.")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")

# Configuración de la ventana
root = tk.Tk()
root.title("Calculadora de Cinemática")
root.geometry("400x400")
root.configure(bg="#f0f0f0")

# Título
titulo = tk.Label(root, text="Calculadora de Cinemática (SI)", font=("Arial", 16, "bold"), bg="#f0f0f0")
titulo.pack(pady=10)

# Opción de cálculo
var_opcion = tk.IntVar(value=1)
opcion_frame = tk.Frame(root, bg="#f0f0f0")
opcion_frame.pack(pady=10)

tk.Radiobutton(opcion_frame, text="1. Desplazamiento uniforme (Δx = v × Δt)", variable=var_opcion, value=1, bg="#f0f0f0").pack(anchor="w")
tk.Radiobutton(opcion_frame, text="2. Desplazamiento con aceleración (Δx = ViΔt + (αΔt²)/2)", variable=var_opcion, value=2, bg="#f0f0f0").pack(anchor="w")
tk.Radiobutton(opcion_frame, text="3. Velocidad final (Vf = Vi + αΔt)", variable=var_opcion, value=3, bg="#f0f0f0").pack(anchor="w")

# Entradas
entry_frame = tk.Frame(root, bg="#f0f0f0")
entry_frame.pack(pady=10)

tk.Label(entry_frame, text="Ingrese v (m/s):", bg="#f0f0f0").grid(row=0, column=0, sticky="w")
entry_v = tk.Entry(entry_frame)  # Campo para v
entry_v.grid(row=0, column=1)

tk.Label(entry_frame, text="Ingrese Vi (m/s):", bg="#f0f0f0").grid(row=1, column=0, sticky="w")
entry_vi = tk.Entry(entry_frame)
entry_vi.grid(row=1, column=1)

tk.Label(entry_frame, text="Ingrese α (m/s²):", bg="#f0f0f0").grid(row=2, column=0, sticky="w")
entry_alpha = tk.Entry(entry_frame)
entry_alpha.grid(row=2, column=1)

tk.Label(entry_frame, text="Ingrese Δt (s):", bg="#f0f0f0").grid(row=3, column=0, sticky="w")
entry_delta_t = tk.Entry(entry_frame)
entry_delta_t.grid(row=3, column=1)

# Botón de calcular
boton_calcular = tk.Button(root, text="Calcular", command=realizar_calculo, bg="#4CAF50", 
                           fg="white",
                           # border radius
                            bd=2)
boton_calcular.pack(pady=20)

# Ejecutar la aplicación
root.mainloop()

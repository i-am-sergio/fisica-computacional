def calcular_desplazamiento_uniforme(v, delta_t):
    """Calcula el desplazamiento en movimiento uniforme (en metros)."""
    return v * delta_t  # desplazamiento en metros

def calcular_desplazamiento_acelerado(Vi, alpha, delta_t):
    """Calcula el desplazamiento en movimiento con aceleración constante (en metros)."""
    return Vi * delta_t + 0.5 * alpha * delta_t**2  # desplazamiento en metros

def calcular_velocidad_final(Vi, alpha, delta_t):
    """Calcula la velocidad final en movimiento con aceleración constante (en metros/segundo)."""
    return Vi + alpha * delta_t  # velocidad final en m/s

def main():
    print("╔══════════════════════════════════╗")
    print("║  Calculadora de Cinemática (SI)  ║")
    print("╠══════════════════════════════════╣")
    print("║  1. Desplazamiento uniforme      ║")
    print("║     (Δx = v × Δt)                ║")
    print("║  2. Desplazamiento con           ║")
    print("║     aceleración                  ║")
    print("║     (Δx = ViΔt + (αΔt²)/2)       ║")
    print("║  3. Velocidad final              ║")
    print("║     (Vf = Vi + αΔt)              ║")
    print("╚══════════════════════════════════╝")

    opcion = int(input("Ingrese el número de la operación: "))

    if opcion == 1:
        v = float(input("Ingrese la velocidad (v) en m/s: "))
        delta_t = float(input("Ingrese el intervalo de tiempo (Δt) en segundos: "))
        desplazamiento = calcular_desplazamiento_uniforme(v, delta_t)
        print(f"Desplazamiento: Δx = {desplazamiento:.2f} metros")

    elif opcion == 2:
        Vi = float(input("Ingrese la velocidad inicial (Vi) en m/s: "))
        alpha = float(input("Ingrese la aceleración (α) en m/s²: "))
        delta_t = float(input("Ingrese el intervalo de tiempo (Δt) en segundos: "))
        desplazamiento = calcular_desplazamiento_acelerado(Vi, alpha, delta_t)
        print(f"Desplazamiento: Δx = {desplazamiento:.2f} metros")

    elif opcion == 3:
        Vi = float(input("Ingrese la velocidad inicial (Vi) en m/s: "))
        alpha = float(input("Ingrese la aceleración (α) en m/s²: "))
        delta_t = float(input("Ingrese el intervalo de tiempo (Δt) en segundos: "))
        Vf = calcular_velocidad_final(Vi, alpha, delta_t)
        print(f"Velocidad final: Vf = {Vf:.2f} m/s")

    else:
        print("Opción no válida.")

if __name__ == "__main__":
    while True:
        main()
        continuar = input("¿Desea realizar otra operación? (s/n): ")
        if continuar.lower() != "s":
            break

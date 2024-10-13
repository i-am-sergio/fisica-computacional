# Función para solicitar y verificar la masa
def solicitar_masa():
    while True:
        try:
            masa = float(input("Ingrese la masa en kilogramos (kg): "))
            if masa <= 0:
                print("La masa debe ser un valor positivo. Intente de nuevo.")
            else:
                return masa
        except ValueError:
            print("Entrada inválida. Por favor ingrese un número válido.")

# Función para solicitar y verificar la aceleración
def solicitar_aceleracion():
    while True:
        try:
            aceleracion = float(input("Ingrese la aceleración en metros por segundo cuadrado (m/s^2): "))
            if aceleracion == 0:
                print("La aceleración no puede ser cero. Intente de nuevo.")
            else:
                return aceleracion
        except ValueError:
            print("Entrada inválida. Por favor ingrese un número válido.")

# Función principal para calcular la fuerza neta
def calcular_fuerza():
    masa = solicitar_masa()
    aceleracion = solicitar_aceleracion()
    fuerza = masa * aceleracion
    print(f"La fuerza neta es: {fuerza} Newtons")

# Llamada a la función principal
calcular_fuerza()

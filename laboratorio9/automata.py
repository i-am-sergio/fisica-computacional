import numpy as np
import matplotlib.pyplot as plt

# Definir la regla de transición
def regla_transicion(izquierda, centro, derecha):
    if (izquierda == 0 and centro == 0 and derecha == 0):
        return 0
    elif (izquierda == 0 and centro == 0 and derecha == 1):
        return 1
    elif (izquierda == 0 and centro == 1 and derecha == 0):
        return 1
    elif (izquierda == 0 and centro == 1 and derecha == 1):
        return 1
    elif (izquierda == 1 and centro == 0 and derecha == 0):
        return 1
    elif (izquierda == 1 and centro == 0 and derecha == 1):
        return 0
    elif (izquierda == 1 and centro == 1 and derecha == 0):
        return 0
    elif (izquierda == 1 and centro == 1 and derecha == 1):
        return 0

# Función para evolucionar el autómata celular
def evolucion_autómata(celdas_iniciales, pasos):
    # Crear una matriz para guardar los estados de cada paso
    historia = np.zeros((pasos, len(celdas_iniciales)), dtype=int)
    historia[0] = celdas_iniciales
    
    # Evolucionar en el tiempo
    for t in range(1, pasos):
        for i in range(1, len(celdas_iniciales) - 1):
            izquierda = historia[t-1, i-1]
            centro = historia[t-1, i]
            derecha = historia[t-1, i+1]
            historia[t, i] = regla_transicion(izquierda, centro, derecha)
    
    return historia

# Configuración inicial
tamano = 101  # Tamaño de la fila de celdas
pasos = 50    # Número de generaciones a simular
celdas_iniciales = np.zeros(tamano, dtype=int)
celdas_iniciales[tamano // 2] = 1  # Inicializar la celda central activa

# Evolucionar el autómata
historia = evolucion_autómata(celdas_iniciales, pasos)

# Graficar el autómata celular
plt.imshow(historia, cmap='binary', interpolation='nearest')
plt.title("Autómata Celular - Regla de Selección")
plt.xlabel("Posición de la Celda")
plt.ylabel("Generación")

# save the plot
plt.savefig("automata_celular.png")
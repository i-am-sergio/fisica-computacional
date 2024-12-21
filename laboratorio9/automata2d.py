import numpy as np
import matplotlib
matplotlib.use('TkAgg')  # Cambia el backend a 'TkAgg' para usar una interfaz interactiva
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Dimensiones de la grilla
grid_size = 50

# Probabilidad de inicializar una celda como activa (1)
probabilidad_inicial = 0.2

# Función para inicializar la grilla
def inicializar_grilla(size):
    return np.random.choice([0, 1], size=(size, size), p=[1 - probabilidad_inicial, probabilidad_inicial])

# Regla de transición basada en las celdas vecinas
def aplicar_regla(grid):
    nuevo_estado = np.copy(grid)
    for i in range(1, grid.shape[0]-1):
        for j in range(1, grid.shape[1]-1):
            izquierda = grid[i-1, j]  # Celda a la izquierda
            centro = grid[i, j]      # Celda actual
            derecha = grid[i+1, j]   # Celda a la derecha
            
            # Aplicamos la regla de transición definida en la tabla
            if izquierda == 0 and centro == 0 and derecha == 0:
                nuevo_estado[i, j] = 0
            elif izquierda == 0 and centro == 0 and derecha == 1:
                nuevo_estado[i, j] = 1
            elif izquierda == 0 and centro == 1 and derecha == 0:
                nuevo_estado[i, j] = 1
            elif izquierda == 0 and centro == 1 and derecha == 1:
                nuevo_estado[i, j] = 1
            elif izquierda == 1 and centro == 0 and derecha == 0:
                nuevo_estado[i, j] = 1
            elif izquierda == 1 and centro == 0 and derecha == 1:
                nuevo_estado[i, j] = 0
            elif izquierda == 1 and centro == 1 and derecha == 0:
                nuevo_estado[i, j] = 0
            elif izquierda == 1 and centro == 1 and derecha == 1:
                nuevo_estado[i, j] = 0
    return nuevo_estado

# Función para visualizar el autómata
def visualizar(grid):
    plt.imshow(grid, cmap='binary')
    plt.axis('off')
    plt.show()

# Función para animar el autómata
def animar(grid):
    fig, ax = plt.subplots()
    ims = []
    
    for _ in range(100):  # Número de iteraciones
        im = ax.imshow(grid, cmap='binary', animated=True)
        ims.append([im])
        grid = aplicar_regla(grid)  # Aplicar la regla de transición
    
    ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True, repeat_delay=1000)
    plt.axis('off')
    plt.show()

# Inicializar la grilla
grid = inicializar_grilla(grid_size)

# Visualizar el autómata después de unas iteraciones
visualizar(grid)

# Animación del autómata
animar(grid)

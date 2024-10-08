import math

# Constantes
G = 6.67430e-11  # Constante de gravitación universal (Nm^2/kg^2)
M = 1.989e30     # Masa del sol en kg

# Datos de los planetas: (nombre, distancia al Sol en metros)
planets = [
    ("Mercurio", 5.791e10),
    ("Venus", 1.082e11),
    ("Tierra", 1.496e11),
    ("Marte", 2.279e11),
    ("Júpiter", 7.785e11),
    ("Saturno", 1.429e12),
    ("Urano", 2.871e12),
    ("Neptuno", 4.495e12)
]

# Tiempo que tarda en completar una órbita (en segundos)
t_orbital = 365.25 * 24 * 3600  # Un año en segundos

# Calcular velocidad orbital y velocidad MRU para cada planeta
for planet in planets:
    name, r = planet

    # Cálculo de la velocidad orbital usando la Ley de Gravitación Universal
    v_orbital = math.sqrt(G * M / r)

    # MRU: distancia recorrida (circunferencia de la órbita)
    d_orbital = 2 * math.pi * r

    # Velocidad usando MRU
    v_mru = d_orbital / t_orbital

    # Resultados
    print(f"Planeta: {name}")
    print(f"  Velocidad orbital (Ley de Gravitación): {v_orbital:.2f} m/s")
    print(f"  Velocidad orbital (MRU): {v_mru:.2f} m/s")

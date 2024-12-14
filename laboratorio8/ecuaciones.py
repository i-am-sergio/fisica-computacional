import numpy as np

def biseccion(f, a, b, tol=1e-6, max_iter=100):
    """
    Método de Bisección.
    """
    if f(a) * f(b) >= 0:
        raise ValueError("El teorema del valor intermedio no se cumple. f(a) y f(b) deben tener signos opuestos.")
    
    for _ in range(max_iter):
        c = (a + b) / 2
        if abs(f(c)) < tol or (b - a) / 2 < tol:
            return c
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    raise ValueError("El método no convergió después del número máximo de iteraciones.")

def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
    """
    Método de Newton-Raphson.
    """
    x = x0
    for _ in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if abs(fx) < tol:
            return x
        if dfx == 0:
            raise ValueError("Derivada cero. No se puede continuar.")
        x = x - fx / dfx
    raise ValueError("El método no convergió después del número máximo de iteraciones.")

def falsa_posicion(f, a, b, tol=1e-6, max_iter=100):
    """
    Método de Falsa Posición.
    """
    if f(a) * f(b) >= 0:
        raise ValueError("El teorema del valor intermedio no se cumple. f(a) y f(b) deben tener signos opuestos.")
    
    for _ in range(max_iter):
        c = b - (f(b) * (b - a)) / (f(b) - f(a))
        if abs(f(c)) < tol:
            return c
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    raise ValueError("El método no convergió después del número máximo de iteraciones.")

def secante(f, x0, x1, tol=1e-6, max_iter=100):
    """
    Método de la Secante.
    """
    for _ in range(max_iter):
        if abs(f(x1)) < tol:
            return x1
        if f(x1) - f(x0) == 0:
            raise ValueError("División por cero en la iteración. No se puede continuar.")
        x_temp = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        x0, x1 = x1, x_temp
    raise ValueError("El método no convergió después del número máximo de iteraciones.")


def probar_metodos(f, df=None, intervalo=None, inicial=None, tol=1e-6, max_iter=100):
    """
    Prueba los métodos de resolución de ecuaciones no lineales.
    
    Args:
        f: Función a resolver.
        df: Derivada de la función (solo para Newton-Raphson).
        intervalo: Tuple (a, b) para métodos de intervalo (bisección y falsa posición).
        inicial: Punto inicial (o iniciales) para métodos de punto único (Newton-Raphson, Secante).
        tol: Tolerancia para los métodos.
        max_iter: Máximo número de iteraciones permitidas.
    """
    metodos = {
        "Bisección": lambda: biseccion(f, intervalo[0], intervalo[1], tol, max_iter),
        "Newton-Raphson": lambda: newton_raphson(f, df, inicial, tol, max_iter),
        "Falsa Posición": lambda: falsa_posicion(f, intervalo[0], intervalo[1], tol, max_iter),
        "Secante": lambda: secante(f, inicial[0], inicial[1], tol, max_iter)
    }
    
    for nombre, metodo in metodos.items():
        try:
            resultado = metodo()
            print(f"{nombre}: Solución encontrada -> {resultado}")
        except Exception as e:
            print(f"{nombre}: No se puede con este método. Razón -> {e}")

# Funciones y derivadas
def f1(x): return np.log(x - 2)
def f2(x): return np.exp(-x)
def f3(x): return np.exp(x) - x
def f4(x): return 10 * np.exp(x / 2) * np.cos(2 * x)
def f5(x): return x**2 - 2
def f6(x): return np.sqrt(x - 2)
def f7(x): return x * np.cos(x) + x * np.sin(x)
def f8(x): return 2 / x

def df3(x): return np.exp(x) - 1
def df5(x): return 2 * x
def df7(x): return np.cos(x) - x * np.sin(x) + np.sin(x)
def df8(x): return -2 / (x**2)

# Pruebas
print("Ecuación 1: y = ln(x − 2)")
probar_metodos(f1, intervalo=(2.1, 4), inicial=(3, 4))

print("\nEcuación 2: y = e^−x")
probar_metodos(f2, intervalo=(0, 2), inicial=(0.5, 1))

# print("\nEcuación 3: y = e^x − x")
# probar_metodos(f3, df=df3, intervalo=(0, 1), inicial=(0.5, 1))

print("""
Ecuación 3: y = e^x − x
Bisección: No se puede con este método. Razón -> El teorema del valor intermedio no se cumple. f(a) y f(b) deben tener signos opuestos.
Newton-Raphson: No se puede con este método. Razón -> The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
Falsa Posición: No se puede con este método. Razón -> El teorema del valor intermedio no se cumple. f(a) y f(b) deben tener signos opuestos.
Secante: Solución encontrada -> -0.8333048903658308
""")

print("\nEcuación 4: y = 10e^(x/2)cos(2x)")
probar_metodos(f4, intervalo=(-2, 2), inicial=(-1, 0))

print("\nEcuación 5: y = x^2 − 2")
probar_metodos(f5, df=df5, intervalo=(0, 2), inicial=(1, 1.5))

print("\nEcuación 6: y = (x − 2)^(1/2)")
# probar_metodos(f6, intervalo=(3, 5), inicial=(3, 4))
print("""
Bisección: No se puede con este método. Razón -> El teorema del valor intermedio no se cumple. f(a) y f(b) deben tener signos opuestos.
Newton-Raphson: No se puede con este método. Razón -> The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
Falsa Posición: No se puede con este método. Razón -> El teorema del valor intermedio no se cumple. f(a) y f(b) deben tener signos opuestos.
Secante: Solución encontrada -> 2.0000833304890365
""")

print("\nEcuación 7: y = xcos(x) + xsen(x)")
probar_metodos(f7, df=df7, intervalo=(-1, 1), inicial=(0, 1))

print("\nEcuación 8: y = 2 / x")
probar_metodos(f8, df=df8, intervalo=(0.5, 2), inicial=(1, 1.5))

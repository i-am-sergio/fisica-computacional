import numpy as np
import time

def GSA(fun, x0, l=None, u=None, qv=2.7, qa=-5, Imax=500):
    """
    Generalized Simulated Annealing (GSA)
    Args:
        fun (callable): Objective function to minimize.
        x0 (numpy.ndarray): Initial solution.
        l (numpy.ndarray, optional): Lower bounds for the variables.
        u (numpy.ndarray, optional): Upper bounds for the variables.
        qv (float, optional): Exploration parameter for the visiting distribution. Default is 2.7.
        qa (float, optional): Acceptance parameter. Default is -5.
        Imax (int, optional): Maximum number of iterations. Default is 500.
    Returns:
        tuple: Best solution (xo), objective value (fo), and execution time (time_elapsed).
    """
    start_time = time.time()

    # Initialization
    x = np.array(x0, dtype=float)
    n = len(x)
    if l is None:
        l = -np.inf * np.ones_like(x)
    if u is None:
        u = np.inf * np.ones_like(x)

    xo = np.copy(x)
    fo = fun(xo)

    # Main loop
    for iter in range(1, Imax + 1):
        # Update temperatures
        Tqv = (1 + qv * iter) ** (-1 / (qv - 1))
        Tqa = (1 + qa * iter) ** (-1 / (qa - 1))

        # Generate new solution
        y = Tsallis_rnd(x, Tqv, qv, l, u)
        fy = fun(y)

        # Calculate the objective difference
        delta_f = fy - fo

        # Acceptance criterion
        if delta_f < 0 or np.random.rand() < (1 + qa * delta_f / Tqa) ** (1 / (1 - qa)):
            x = np.copy(y)
            fo = fy

        # Update the best solution
        if fy < fo:
            xo = np.copy(y)

    time_elapsed = time.time() - start_time
    return xo, fo, time_elapsed

def Tsallis_rnd(x, Tqv, qv, l, u):
    """
    Generate random numbers based on the Tsallis distribution.
    Args:
        x (numpy.ndarray): Current solution.
        Tqv (float): Temperature parameter for the visiting distribution.
        qv (float): Exploration parameter for the visiting distribution.
        l (numpy.ndarray): Lower bounds.
        u (numpy.ndarray): Upper bounds.
    Returns:
        numpy.ndarray: New solution.
    """
    n = len(x)
    r = np.random.uniform(-1, 1, n)
    step = r * (Tqv ** (1 / (qv - 1))) / np.linalg.norm(r)
    y = x + step

    # Enforce bounds
    y = np.maximum(l, np.minimum(y, u))
    return y

# Example usage
if __name__ == "__main__":
    # Define the objective function
    def f(x):
        x1 = np.array([100, 200])
        x2 = np.array([1e5, -3e5])
        return -10 * np.cosh(np.linalg.norm(x - x1)) - 20 * np.cosh(np.linalg.norm(x - x2) * 3e-4) - 1

    # Initial solution and bounds
    x0 = np.array([0.0, 0.0])
    l = np.array([-1e6, -1e6])
    u = np.array([1e6, 1e6])

    # Run the GSA algorithm
    xo, fo, t = GSA(f, x0, l, u, qv=2.7, qa=-5, Imax=500)

    print("Best solution:", xo)
    print("Objective value:", fo)
    print("Execution time:", t, "seconds")

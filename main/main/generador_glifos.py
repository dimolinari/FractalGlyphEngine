import numpy as np
from scipy.integrate import odeint

def duffing_modified(state, t, alpha, beta, gamma):
    x, y = state
    dxdt = y
    dydt = -alpha*y + beta*x - gamma*x**3 + 0.5*np.sin(2*np.pi*t)
    return [dxdt, dydt]

def generar_glifo(alpha, beta, gamma, num_puntos=10000):
    t = np.linspace(0, 100, num_puntos)
    sol = odeint(duffing_modified, [0.01, 0.01], t, args=(alpha, beta, gamma))
    x, y = sol.T
    return x, y

import numpy as np
import matplotlib.pyplot as plt

# Definimos la ecuación diferencial dy/dt = y
def f(t, y):
    return y

# Parámetros
t0 = 0
y0 = 1
h = 0.2
t_final = 1

# Método de Euler
t_values = np.arange(t0, t_final + h, h)
y_euler = []

y = y0
for t in t_values:
    y_euler.append(y)
    y = y + h * f(t, y)

# Solución exacta
y_exact = np.exp(t_values)

# Mostrar resultados
print("t\tEuler\tExacta")
for i in range(len(t_values)):
    print(f"{t_values[i]:.1f}\t{y_euler[i]:.5f}\t{y_exact[i]:.5f}")

# Graficar
plt.plot(t_values, y_exact, label="Solución Exacta", marker='o')
plt.plot(t_values, y_euler, label="Euler", marker='s')
plt.legend()
plt.xlabel("t")
plt.ylabel("y")
plt.title("Comparación: Solución Exacta vs Euler")
plt.grid()
plt.show()
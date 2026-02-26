# Comparación de Soluciones Analíticas y Numéricas

## Problema

Resolver la ecuación diferencial:

dy/dt = y

con condición inicial:

y(0) = 1

## Solución Analítica

Usando separación de variables:

dy/y = dt

ln(y) = t + C

y = Ce^t

Aplicando la condición inicial:

y(t) = e^t

## Método Numérico

Se aplicó el método de Euler en el intervalo [0,1]
con paso h = 0.2.

## Comparación

Se comparan ambas soluciones en tabla y gráfica.
Se observa que el método de Euler aproxima la solución,
pero presenta un pequeño error respecto a la solución exacta.
import time

# Función 1: Calcula la suma de los primeros N números usando un bucle
def suma_bucle(n):
    suma = 0
    for i in range(1, n+1):
        suma += i
    return suma

# Función 2: Calcula la suma de los primeros N números usando la fórmula matemática
def suma_formula(n):
    return n * (n + 1) // 2

# Definir N para que tarde mas
N = 1000000

# Medir tiempo de ejecución de la función 1
inicio_1 = time.time()
resultado_1 = suma_bucle(N)
final_1 = time.time()
tiempo_ejecucion_1 = final_1 - inicio_1

# Medir tiempo de ejecución de la función 2
inicio_2 = time.time()
resultado_2 = suma_formula(N)
final_2 = time.time()
tiempo_ejecucion_2 = final_2 - inicio_2

# Mostrar los resultados
print(f"Resultado función 1: {resultado_1}, Tiempo de ejecución: {tiempo_ejecucion_1} segundos")
print(f"Resultado función 2: {resultado_2}, Tiempo de ejecución: {tiempo_ejecucion_2} segundos")
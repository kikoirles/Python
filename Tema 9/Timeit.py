import timeit
# permite medir el tiempo de forma mas precisa pero realiza dicha funcion repiendo el la funcion en bucle X 
# Función 1: Calcula la suma de los primeros N números usando un bucle
def suma_bucle(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma

# Función 2: Calcula la suma de los primeros N números usando la fórmula matemática
def suma_formula(n):
    return n * (n + 1) // 2

# Definir N
N = 1000000

# Medir tiempo de ejecución de la función 1 usando timeit
tiempo_ejecucion_1 = timeit.timeit('suma_bucle(N)', globals=globals(), number=10)

# Medir tiempo de ejecución de la función 2 usando timeit
tiempo_ejecucion_2 = timeit.timeit('suma_formula(N)', globals=globals(), number=100000)

# Mostrar los resultados
print(f"Tiempo de ejecución función 1 (10 iteraciones): {tiempo_ejecucion_1} segundos")
print(f"Tiempo de ejecución función 2 (100000 iteraciones): {tiempo_ejecucion_2} segundos")
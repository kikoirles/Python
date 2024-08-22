# Nos permite pasar mas argumentos de entrada en las funciones de forma ipredecible a los usuarios
# ejemplo           def suma (num1 + num2):
    #                     return num1 + num2

# suma (1,2,3) esto le daria fallo al usuario por lo que deberemos relizar lo siguiente

# *args = arguments         def suma (*args):

def suma (a,b):
    return a+b

print(suma(1,2))

def suma (*args):
    total = 0
    # iteracion en una propia suma aumentado el total por el bucle
    for arg in args:
        total += arg
    return total

print(suma(2,3,4,5,6,5))

# Eleva los numeros que le introduzca el usuario independientemente de la cantidad que introduzca y los suma
def suma_cuadrados(*args):
    # Eleva al cuadrado cada número en args y suma los resultados
    total = sum(num**2 for num in args)
    return total

# Llama a la función con los argumentos de ejemplo
print(suma_cuadrados(2, 3, 4))

# suma sin importar si los numeros son positivos o negativos
def suma_absolutos(*args):
    # Calcula la suma de los valores absolutos de los argumentos
    total = sum(abs(num) for num in args)
    return total

# Ejemplo de llamada a la función
print(suma_absolutos(-5, 3, -2, 7))

# cuenta la cantidad de parametros
def cantidad_atributos(*args):
    solucion = len(args)
    print(solucion)

cantidad_atributos(1, 2, 3, 4, 1, 2)


# suma numeros no nombres
def numeros_persona(nombre, *args):
    # Calcula la suma de los números en args
    suma_numeros = sum(args)
    # Formatea el mensaje con el nombre y la suma de los números
    mensaje = f"{nombre}, la suma de tus números es {suma_numeros}"
    return mensaje

# Ejemplo de llamada a la función
print(numeros_persona("Ana", 10, 20, 30))



# Funciones dinamicas funciones con condiciones y bucles

def chequear_3_cifras(numero):
    return numero in range(100,1000)
resultado = chequear_3_cifras(543)

print(resultado)

# no esta en el rango ninguno de los 3 numeros

def chequear_3_cifras_new1(lista):

    for n in lista:
        if n in range (100,1000):
            return True
        else:
            pass
resultado2 = chequear_3_cifras_new1([55,33,6000])
print(resultado2)

# Funciones dinamicas bucle en este caso en la segunda vuelta la del 333 saca verdadero porque esta en el rango
def chequear_3_cifras_new2(lista):

    for n in lista:
        if n in range (100,1000):
            return True
        else:
            pass
resultado2 = chequear_3_cifras_new2([55,333,6000])
print(resultado2)

# Da salida de False si hay alguno que no es de 3 cifras
def chequear_3_cifras_new3(lista):

    for n in lista:
        if n in range (100,1000):
            return True
        else:
            pass

    return False

resultado2 = chequear_3_cifras_new3([55,3333,6000])
print(resultado2)

# la misma funcion que antes solo que ahora si esta en el rango el numero se guardara en la variable lista_3_cifras
def chequear_3_cifras_new4(lista):

    lista_3_cifras = []
    for n in lista:
        if n in range(100,1000):
            lista_3_cifras.append(n)
        else:
            pass

    return lista_3_cifras

resultado2 = chequear_3_cifras_new4([553,333,6000])
print(resultado2)

# Funcion de ejercicio devulve true si son positivos todos
lista_numeros = [1,2,3,-4,-6]
def todos_positivos(lista_numeros):
    for num in lista_numeros:
        if num < 0:
            return False
        else:
            pass
    return True

print(todos_positivos(lista_numeros))

# Funcion devulve la suma de los numeros que cumplen dichas condiciones mayores que 0 y menores que 1000
def suma_menores(lista_numeros):
    sumas = 0
    for num in lista_numeros:
        if 0 < num < 1000:
            sumas += num # va añadiendo los numeros y los suma
    return sumas    # Ojo esta debe de estar al mismo nivel que For

lista_numeros = [50,1500,-5,999,0,750,1000]
resultado = suma_menores(lista_numeros)
print(resultado)

# Funcion devulve la cantidad de numero que son pares

lista_numeros = [1, 50, 502, 5000, 755, 600, 33, 61]

def cantidad_pares(lista_numeros):
    cantidad = 0
    for numero in lista_numeros:
        if numero % 2 == 0:  # verifica si el numero es par
            cantidad += 1  # va añadiendo los numeros y los suma
        else:
            pass
    return cantidad

print(cantidad_pares((lista_numeros)))








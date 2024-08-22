# Nos permite gneral valores de forma incrementa segun los necesitemos para ahorrar memoria en el ordenador
def mi_funcion():
    return 4

def mi_generador():
    yield 4

print(mi_funcion())
# print(mi_generador()) # no funciona asi

ge = mi_generador()
print(next(ge))

def mi_funcion2():
    lista = []
    for x in range(1, 5):
        lista.append(x * 10) # lista del 1 al 4 * 10
    return lista

def mi_generador2():

    for x in range(1, 5):
        yield x * 10


print(mi_funcion2())

ge2 = mi_generador2()
print(next(ge2))
print(next(ge2)) # hace que me de el segundo generado

# Ejemplo Generador infinito

def secuencia_infinita():
    num = 0
    while True:
        num += 1
        yield num

generador = secuencia_infinita()

# Ejercicio Multiplos de 7 infinitos

def multiplos7():
    num = 0
    numerobase = 7
    while True:
        num += 1
        yield numerobase * num


generador = multiplos7()


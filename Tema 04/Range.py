lista = [1,2,3,4]

for numero in lista:
     print(numero)


# range sustituye a esto lista = [1,2,3,4] con range (5) tiene que se uno mas porque el 5 es el limite de 0 a 5
for numero in range(5):
     print(numero)

for numero in range(20,31):
     print(numero)

for numero in range(20,31,3):
    print(numero)

lista = list(range(1,101))
print(lista)

mi_lista = list(range(2500,2586))
print(mi_lista)

mi_lista = list(range(3,301,3))
print(mi_lista)

suma_cuadrados = 0

for numero in range(1,16):
    cuadrado = numero ** 2
    suma_cuadrados += cuadrado

print(suma_cuadrados)


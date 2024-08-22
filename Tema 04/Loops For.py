lista = ['a','b','c']

for letra in lista:
    print("letra: " + letra)


lista = ['a','b','c']

for letra in lista:
    numero_letra = lista.index(letra) + 1
    print(f"letra: {numero_letra}:{letra}")


numeros = [1,2,3,4,5]
mi_valor = 0

for numero in numeros:
    mi_valor = mi_valor + numero

    print(mi_valor)


palabra = 'python'

for letra in palabra:
    print(letra)


alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]

for nombre in alumnos_clase:
    print("Hola " + nombre)

lista_numeros = [1, 5, 8, 7, 6, 8, 2, 5, 2, 6, 4, 8, 5, 9, 8, 3, 5, 4, 2, 5, 6, 4]
suma_numeros = 0

for numero in lista_numeros:
    suma_numeros = suma_numeros + numero

    print(suma_numeros)


lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0

for numero in lista_numeros:
    if numero % 2 == 0:
        suma_pares = suma_pares + numero
    elif numero % 2 == 1:
        suma_impares = suma_impares +numero
    else:
        print("algo salio mal")
    print(suma_pares)
    print(suma_impares)


lista_numeros = [4, 5, 8, 7, 6, 9, 8, 2, 4, 5, 7, 1, 9, 5, 6, -1, -5, 6, -6, -4, -3]

for numero in lista_numeros:
    if numero >= 0:
        print(numero)
    else:
        break

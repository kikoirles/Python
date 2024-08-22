from random import *

aleatorio = randint(1,50)
print(aleatorio)

aleatorio2 = round(uniform(1,5),2)
print(aleatorio2)

aleatorio3 = random()
print(aleatorio3)

colores = ['azul','verde','rojo']
seleccion_color = choice(colores)
print(seleccion_color)

numeros = list(range(5,50,5))
print(numeros)
shuffle(numeros)
print(numeros)

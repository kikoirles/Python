lista = ['a','b','c']
indice = 0

for indice,item in enumerate(lista):
    print(indice,item)


indice = 0

for indice,item in enumerate(range(50,55)):
    print(indice,item)

lista = ['a','b','c']
mis_tuples = list(enumerate(lista))
print(mis_tuples)

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
indice = 0

for indice,nombre in enumerate(lista_nombres):
    print(f'{nombre} se encuentra en el índice {indice}')

cadena = "Python"
lista_indices = list(enumerate(cadena))
print(lista_indices)


lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice, nombre in enumerate(lista_nombres):
    if nombre.startswith('M'):
        print(nombre)
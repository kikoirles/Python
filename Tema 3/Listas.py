#    Listas
mi_lista = ['a','b','c']
otra_lista = ['alo',54,6.4]
lista_final = mi_lista + otra_lista
resultado = mi_lista[0:1]
print(resultado)
print(mi_lista + otra_lista)
print(type(mi_lista))

#  modificar posicion de lista un valor
lista_final[0] = "alfa"
print(lista_final)

# Añadir a listas
lista_final.append("g")
print(lista_final)

# Listas elimina caracteres ultimo caracter
lista_final.pop()
print(lista_final)
# Listas elimina caracteres posicion 4
lista_final.pop(3)
print(lista_final)
# Listas elimina caracteres posicion 3 y lo almacena en varaible
frutas = ["manzana", "banana", "mango", "cereza", "sandía"]
eliminado = frutas.pop(2)
print(frutas)
print(eliminado)

# Listas ordenadas
mi_lista_o = ['c','a','b','e']
mi_lista_o.sort()
print(mi_lista_o)

# Listas desordenadas
mi_lista_od = ['c','a','b','e']
mi_lista_od.reverse()
print(mi_lista_od)
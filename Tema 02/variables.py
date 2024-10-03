# tipos de datos
"""
Camel case
En Camel case debes empezar con la primera letra minúscula y la primera letra de cada nueva palabra subsecuente en mayúscula:

cosasParaHacer
edadDelAmigo
valorFinal

Pascal case
También conocido como "upper camel case" o "capital case", Pascal case combina palabras poniéndolas todas con la primera letra en mayúscula:

CosasParaHacer
EdadDelAmigo
ValorFinal

Snake case
En Snake case, conocido también como "underscore case", se utiliza guión bajo (underscore) en lugar de espacio para separar las palabras. Cuando snake case está en mayúsculas, se le conoce como "screaming snake case":

cosas_para_hacer
edad_del_amigo
valor_final

Kebab case
En Kebab case se utiliza el guión para combinar las palabras. Cuando el Kebab case está en mayúsculas, se llama "screaming kebab case":

cosas-para-hacer
edad-del-amigo
valor-final
"""

# string(str) "hola","232"," "
# integer(int) 150,1,555,-15,0
# floating(float) 1.23,12.0,-73.2
# listas(list) ["hola","232",1.23,12.0,]  (la primera posion simpre es 0)
# dicionarios(dic) {'arte:cine','color:rojo'}
# tuples(tuple) ('lun','mar','mie','jue','vie') (su orden es inmutable no se puede modificar)
# sets(set) {'a','b','c','d','e','f'} (elementos unicos no se repiten)
# booleanos(bool) True,False


# variables
nombre = "juan"
print(nombre)

nombre = "Laura"
print(nombre)


nombre = "juan"
nombre = "Laura"      # Notifica un fallo ya que es mala practica cambair nombre valores de varibales
print(nombre)

edad = 30
print(edad)

edad = 30
edad2 = 20
print(edad + edad2)

nombre = input("dime tu nombre:")
print("tu nombre es " + nombre)

nombre1 = "hola "
nombre2 = "paco"
saludo = nombre1 + nombre2
print(saludo)

num1 = 40
num2 = 60
total = num1 + num2
print(total)


mi_numero = 1
print(mi_numero)

# imprime el typo de dato que utiliza esta variable
print(type(mi_numero))

mi_numero = 2.3
print(mi_numero + mi_numero)

# imprime el typo de dato que utiliza esta variable
print(type(mi_numero))

mi_numero = 2.0
mi_numero2 = 20
print(mi_numero + mi_numero2)

# imprime el typo de dato que utiliza esta variable
print(type(mi_numero))

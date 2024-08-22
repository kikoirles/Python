from random import shuffle
# juegos de palitos pierde el que saca el palito mas coto

# lista incial palitos
palitos =['-','--','---','----']

# mezclar palitos
def mezclar (lista):
    shuffle(lista)
    return lista # mezclar los palitos y los devuelve mezclados

# print(mezclar(palitos)) # como funciona mezclo

# pedirle intento

def probar_suerte():
    intento = ''
    while intento not in ['1','2','3','4']: # bucle no para de pedir al usuario hasta que introduzca el un numero de 1 al 4
        intento = input("Elige un numero del 1 al 4: ")

    return int(intento) # devueleve el numero en valor en int


# Comprobar intento
def chequear_intento(lista,intento):
    if lista[intento -1] == '-': # esto es para que el usuario si introduce el 1 el indice de la lista pilla el 2,
        print("A lavar los platos")     # restando 1 al del usuaurio se arregla # ya que las lista comienzan por el 0
    else:
        print("Esta vez te has salvado")

    print(f"te ha tocado el palo {lista[intento-1]}")


# Compilacion de funciones
palitos_mezclados = mezclar(palitos) # variable almacena los palitos mezclados
seleccion = probar_suerte()
chequear_intento(palitos_mezclados,seleccion)





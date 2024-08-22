# Decoradores modifican el comportamiento de otras funciones
# pemite jecutar funciones que a us vez ejecuta una funcion segun una condicion en
# 1 ejemplo asignamos una funcion a una varible
def mayuscula(texto):
    print('--Hola')
    print(texto.upper())
    print('--Adios')

def minuscula(texto):
    print(texto.lower())

# mayuscula('hola')

mi_funcion = minuscula
mi_funcion2 = mayuscula

mi_funcion("-python ")
mi_funcion2("--loco")
# pasamos 2 funciones a la funcion cambiar_letras
def cambiar_letras(tipo):

    def mayuscula2(texto):
        print(texto.upper())

    def minuscula2(texto):
        print(texto.lower())

    if tipo == "mayus":
        return mayuscula2
    elif tipo == "minus":
        return minuscula2

# Aquí se asigna la función que cambia a mayúsculas a la variable 'operacion'
operacion = cambiar_letras('mayus')

# Se llama a la función con el texto 'palabra'
operacion('palabra')

# Aquí se asigna la función que cambia a mayúsculas a la variable 'operacion'
operacion = cambiar_letras('minus')

# Se llama a la función con el texto 'palabra'
operacion('palabra')


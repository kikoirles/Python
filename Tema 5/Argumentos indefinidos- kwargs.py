# es lo mismo que args pero a nivel de diccionario

def suma(**kwargs):
    total = 0
    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")
        total += valor
    return total

print(suma(x=3,y=5,z=2))# esto no es un diccionario

def prueba(num1,num2,*args,**kwargs):

    print(f"El primer numero es {num1}")
    print(f"El primer numero es {num2}")

    for arg in args:
        print(f"arg = {arg}")

    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")

prueba(15,58,100,200,300,4000,x='uno',y='dos',z='tres')

# Cuenta la cantidad de parametros
def cantidad_atributos(**kwargs):
    cantidad = 0
    for clave in kwargs.items():
        cantidad += 1
    return cantidad


# Funcion que dvuelva en forma de lista los valores de los atributos entregados

def lista_atributos(**kwargs):
    lista = []
    for valor in kwargs.values():
        lista.append(valor)
    return lista

# Funcion que tome como parámetros su nombre y luego una cantidad indetermida de parametros de argumento

def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")
    for clave, valor in kwargs.items():
        print(f'{clave}: {valor}')
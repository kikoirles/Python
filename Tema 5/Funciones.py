# creacion de funciones
# importante usar una tabulacion por debajo siempre en la funcion ya que es lo que ejecuta la funcion
def mi_funcion (nombre):
    # imprime Hola
    # Nombre en formato str espera
    print("Hola " + nombre)

mi_funcion("chris")
mi_funcion("vanessa")


# Nombre de persona bienvenida funcion ya establecida con variable pero ni funciona
nombre_persona = "Luis"
def bienvenida(nombre_persona):
    print(f'¡Bienvenido {nombre_persona}!')
bienvenida("Luis")

# funcion calculo de cuadrado de un numero solicitado esta simpre es la mejor opcion
def cuadrado(un_numero):
    print(un_numero ** 2)
cuadrado(4)

# Return
# Return diferencias con varibales
def sumar(num1,num2):
    return num1 + num2

resultado = sumar(10,20)
print(resultado)

# Return diferencias sin variable
def multiplicar(num3,num4):
    return num3 * num4

print(multiplicar(40,2))

# Return diferencias con variable en return
def multiplicar(num3,num4):
    var1 = num3 * num4
    return(var1)

print(multiplicar(40,2))

# Return almacena el dato resultante en la funcion
# print solo lo muestra por pantalla

def usd_a_eur(num_dolars):
    return num_dolars * 0.90

print(usd_a_eur(4000))

# ejemplo
dolares = 1200
def usd_a_eur(dolares):
    return dolares * 0.90


palabra = ("queso")
def invertir_palabra(palabra):
    return palabra[::-1].upper()

print(invertir_palabra(palabra))
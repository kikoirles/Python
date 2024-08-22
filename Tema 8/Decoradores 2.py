# Definimos el decorador correctamente
def decorar_saludo(funcion):

    def otra_funcion(palabra):
        print('Hola')
        funcion(palabra)
        print('Adiós')
    return otra_funcion  # Devuelve la función sin paréntesis

# Decoramos la función con el decorador
@decorar_saludo # (decorador)
def mayusculas(texto):
    print(texto.upper())

# Función para convertir el texto en minúsculas (no decorada)
@decorar_saludo
def minusculas(texto):
    print(texto.lower())

# Usamos el decorador manualmente sin usar el '@'
mayusculas("Python")
print("\n")
minusculas("python")

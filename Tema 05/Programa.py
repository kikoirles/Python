# Juego del ahorcado

from random import *
cosas = [
    "armario","balcón", "baño", "comedor", "habitación", "despacho", "dormitorio", "espejo",
    "fregadero", "horno", "horno microondas", "jardín", "lavabo", "lavadero", "lavaplatos",
    "pasillo", "patioi", "salón", "sótano", "techo", "bañera", "cama", "cocina", "cocina",
    "escalera","lavadora", "mesa", "nevera", "puerta", "silla", "terraza", "ventana"
     ]
# palabra secreta
def palabra_secreta (): # palabra secreta lamacenada
    secret_word = choice(cosas)
    return secret_word

# pedir al usuario una letra

def pedir_letra(): # almacena la letra solicitada
    valor = input("Usuario introduce una letra: ")
    if valor.isalpha() and len(valor) == 1: # validar si el usuario ha introducido una letra de tipo
        return valor
    else:
        print("Por favor, introduce una sola letra.")

    return valor


# Función para mostrar el estado actual de la palabra
def mostrar_estado(palabra, letras_adivinadas):
    estado = ""  # Cadena para almacenar el estado actual de la palabra
    for letra in palabra:
        if letra in letras_adivinadas:  # Si la letra ha sido adivinada
            estado += letra + " "  # Añadir la letra seguida de un espacio
        else:
            estado += "_ "  # Añadir un guion bajo seguido de un espacio para las letras no adivinadas
    return estado.strip()  # Devolver el estado sin espacios al final


# Función principal del juego del ahorcado
def juego_ahorcado():
    palabra = palabra_secreta()  # Obtener la palabra secreta de forma aleatoria
    letras_adivinadas = []  # Lista para almacenar las letras que el jugador ha adivinado
    intentos_fallidos = 0  # Contador para el número de intentos fallidos
    max_intentos = 6  # Número máximo de intentos fallidos permitidos

    # Introducción al juego
    print("¡Bienvenido al juego del Ahorcado!")
    print("Adivina la palabra relacionada con cosas de la casa.")
    print(mostrar_estado(palabra, letras_adivinadas))  # Mostrar el estado inicial

    # Bucle principal del juego
    while intentos_fallidos < max_intentos and set(letras_adivinadas) != set(palabra):
        letra = pedir_letra()  # Pedir al usuario que introduzca una letra

        if letra in letras_adivinadas:
            # Si la letra ya ha sido adivinada antes
            print(f"Ya has adivinado la letra '{letra}'. Intenta con otra.")
        elif letra in palabra:
            # Si la letra está en la palabra secreta
            letras_adivinadas.append(letra)  # Añadir la letra a la lista de letras adivinadas
            print(f"¡Bien hecho! La letra '{letra}' está en la palabra.")
        else:
            # Si la letra no está en la palabra secreta
            intentos_fallidos += 1  # Incrementar el contador de intentos fallidos
            print(f"La letra '{letra}' no está en la palabra. Te quedan {max_intentos - intentos_fallidos} intentos.")

        print(mostrar_estado(palabra, letras_adivinadas))  # Mostrar el estado actualizado de la palabra

    # Verificar si el jugador ha ganado o perdido
    if set(letras_adivinadas) == set(palabra):
        # Si todas las letras de la palabra han sido adivinadas
        print(f"¡Felicidades! Has adivinado la palabra '{palabra}'.")
    else:
        # Si se han agotado los intentos fallidos sin adivinar toda la palabra
        print(f"¡Has perdido! La palabra era '{palabra}'.")


# Ejecutar el juego
juego_ahorcado()
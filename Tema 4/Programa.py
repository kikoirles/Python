from random import *

# La consigna es esta: el programa le va a preguntar al usuario su nombre, y luego le va a decir
# algo así como “Bueno, Juan, he pensado un número entre 1 y 100, y tienes solo ocho intentos
# para adivinar cuál crees que es el número”. Entonces, en cada intento el jugador dirá un
# número y el programa puede responder cuatro cosas distintas:

Nombre = input("Dime tu nombre: ")
print(f"Buenas {Nombre}, he pensado un número del 1 al 100 y tienes 8 intentos para adivinarlo.")

# Genera un número aleatorio entre 1 y 100
Numero_aleatorio_secreto = randint(1, 100)

# Establece el número máximo de intentos y el contador de intentos
max_intentos = 8
intentos = 0

# Bucle para permitir al usuario adivinar el número
while intentos < max_intentos:
    intentos += 1
    # Solicita al usuario que ingrese un número
    Numero_user = int(input(f"Intento {intentos}/{max_intentos}: ¿Qué número crees que es? "))

    # Verifica si el número ingresado está dentro del rango permitido
    if Numero_user > 100 or Numero_user < 1:
        print("Ese número no está permitido. Debe estar entre 1 y 100.")
    # Compara el número ingresado con el número secreto
    elif Numero_user > Numero_aleatorio_secreto:
        print(f"El número está por debajo de {Numero_user}.")
    elif Numero_user < Numero_aleatorio_secreto:
        print(f"El número está por encima de {Numero_user}.")
    else:
        print(f"¡Enhorabuena! Has ganado. Has acertado, mi número era {Numero_aleatorio_secreto}.")
        break
else:
    print(f"Se han agotado los intentos. El número era {Numero_aleatorio_secreto}.")



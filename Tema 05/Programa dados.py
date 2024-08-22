from random import randint,choice,random


# Ejercicio lanzar 2 dados se suma su conjunto y se expresa su puntuancion final
def lanzar_dados():
    # Generar dos números aleatorios entre 1 y 6
    numero_1 = randint(1, 6)
    numero_2 = randint(1, 6)
    return numero_1, numero_2

resultado = lanzar_dados()  # Llama a la función correctamente
suma_dados = resultado[0] + resultado[1]  # Suma los dos números en una variable externa

def evaluar_jugada(num):
    if num <= 6:
        print(f"La suma de tus dados es {suma_dados}. Lamentable")
    elif num > 6 and num < 10:
        print(f"La suma de tus dados es {suma_dados}. Tienes buenas chances")
    elif num >= 10:
        print(f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora")
    else:
        print("Resultado no válido")

evaluar_jugada(suma_dados)


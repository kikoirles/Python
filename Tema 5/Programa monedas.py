# Lanzar moneda al aire y segun la elecccion se destruira una lista de datos o no

lista_numeros = [1, 2, 15, 7, 2, 8]  # lista a destruir

def lanzar_moneda():
    resultado = random.choice(["Cara", "Cruz"])  # moneda de resultado
    return resultado

def probar_suerte(moneda, lista):
    if moneda == "Cara":
        print("La lista se autodestruirá")  # destrucción de lista
        return []
    elif moneda == "Cruz":
        print("La lista fue salvada")
        return lista

# Lanzar la moneda y almacenar el resultado
resultado = lanzar_moneda()
# Aplicar la función de suerte a la lista
lista_resultado = probar_suerte(resultado, lista_numeros)

# Mostrar resultados
print("Resultado de la moneda:", resultado)
print("Lista final:", lista_resultado)

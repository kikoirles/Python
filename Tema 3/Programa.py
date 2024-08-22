#  programa analizador de texto

texto = input("introduce el texto a analizar:")
letras = input("introduce 3 letras a buscar seguidas sin espacios que esten en el texto:")
print("\n")
texto = texto.lower()
letras = letras.lower()

lista_letras = list(letras)

# Primera, contar la veces que sale letras
valor_buscar_1 = texto.count(lista_letras[0])
print("Se ha encontrador " + str(valor_buscar_1) + " veces la segunda letra")
valor_buscar_2 = texto.count(lista_letras[1])
print("Se ha encontrador " + str(valor_buscar_2) + " veces la segunda letra")
valor_buscar_3 = texto.count(lista_letras[2])
print("Se ha encontrador " + str(valor_buscar_3) + " veces la segunda letra")
print("\n")
# Cuantas palabras hay en total

total_letras = len(texto)
print("total de letras " + str(total_letras))
print("\n")
# primera y ultima letra del texto
primera_letra = texto[0]
ultima_letra = texto[-1]

print("Primera letra: " + primera_letra)
print("Última letra: " + ultima_letra)
print("\n")
# Texto a la inversa
texto_inverso = texto[::-1]

print("Texto inverso: " + texto_inverso)
print("\n")
# buscar la palabra Python
print("buscando la palabra python en el texto")
verificacion_Python = "python" in texto
dic_conversor = {True:"si", False:"no"}
print(f"La palabra python {dic_conversor[verificacion_Python]} se encuentra en el textp")



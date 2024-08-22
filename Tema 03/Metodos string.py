# upper() -pasar a mayuscualar
# lower() -pasar a minusculas
# split() -separalo en partes(lista)
# join() -unir items usando un separador
# find() -encontrar un sub string
# replace() - reemplazar un substring

texto = "Este es el texto de Federico"
resultado = texto.upper()
print(resultado)

texto = "Este es el texto de Federico"
resultado = texto[2].upper()
print(resultado)

texto = "Este es el texto de Federico"
resultado = texto.lower()
print(resultado)

texto = "Este es el texto de Federico"
resultado = texto.split()
print(resultado)

texto = "Este es el texto de Federico"
resultado = texto.split("t")
print(resultado)



a = "Aprender"
b = "Python"
c = "ya"
texto = "-".join([a,b,c])
print(texto)

texto = "Este es el texto de Federico"
resultado = texto.find("t")
print(resultado)

texto = "Este es el texto de Federico"
resultado = texto.find("g")
print(resultado)

texto = "Este es el texto de Federico"
resultado = texto.replace("Federico","todos")
print(resultado)

texto = "Este es el texto de Federico"
resultado = texto.replace("e","X")
print(resultado)



lista_palabras = ["La","legibilidad","cuenta."]

resultado = " ".join(lista_palabras)
print(resultado)

# Dos replaces
frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."

resultado = frase.replace("difícil","facil").replace("mala","buena")

print(resultado)


n1 = "karin"
n2 = "na"
print(n1 + n2)
print(n1 * 5)


#  salto de lineas codigo de ejemplo
# poema = """ Mil pequeños peces blancos """"



print("agua" in poema)
print("sol" in poema)
print("sol" not in poema)

nueva2 = "hola mundo"
print(len(nueva2))

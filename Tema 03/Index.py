
# index
mi_texto = "Esta es una prueba"
resultado = mi_texto[0]
print(resultado)

mi_texto = "Esta es una prueba"
resultado = mi_texto[6]
print(resultado)

mi_texto = "Esta es una prueba"  # -0... -4 -3 -2 -1
resultado = mi_texto[-4]
print(resultado)

mi_texto = "Esta es una prueba"
resultado = mi_texto.index("e")
print(resultado)

mi_texto = "Esta es una prueba"
resultado = mi_texto.index("prueba")
print(resultado)

mi_texto = "Esta es una prueba"
resultado = mi_texto.index("e",7,20)
print(resultado)

# r de reverse de derecha a izquierda rindex
mi_texto = "Esta es una prueba"
resultado = mi_texto.rindex("e")
print(resultado)

texto = "ABCDEFGHIJKLM"
fragmento = texto[2:5]
print(fragmento)

texto = "ABCDEFGHIJKLM"
fragmento = texto[:5]
print(fragmento)

texto = "ABCDEFGHIJKLM"
fragmento = texto[5:]
print(fragmento)

texto = "ABCDEFGHIJKLM"
fragmento = texto[2:10:2] # salta 1
print(fragmento)

texto = "ABCDEFGHIJKLM"
fragmento = texto[2:10:1]
print(fragmento)

# texto a la inversa
texto = "ABCDEFGHIJKLM"
fragmento = texto[::-1] # reverser
print(fragmento)

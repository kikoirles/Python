monedas = 5

while monedas > 0:
    print(f"tengo {monedas} monedas")
    monedas = monedas -1

monedas = 5

while monedas > 0:
    print(f"tengo {monedas} monedas")
    monedas = monedas -1
else:print("no tengo mas dinero")


respuesta = 's'
while respuesta == 's':
    respuesta = input("quieres seguir? (s/n)")
else:
    print("gracias")

# ticket pass para omitir el bucle while en el codigo

for i in range(5):
    if i == 3:
        pass  # Esto no hace nada y el bucle continúa
    print(i)

print("Fin del bucle")

# ticket break
for i in range(5):
    if i == 3:
        break  # El bucle termina cuando i es 3
    print(i)

print("Bucle terminado con break")

for i in range(5):
    if i == 3:
        continue  # Salta el resto del código en esta iteración
    print(i)

print("Bucle terminado con continue")



numero = 11

while numero > 0:
    numero = numero -1
    print(numero)


numero = 50

while numero >= 0:
    if numero % 5 == 0:
        print(numero)
        numero = numero - 1
    else:
        numero = numero - 1

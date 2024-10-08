# Calculo

x2 = 6
y2 = 2
z2 = 7

print(f"{x2} mas {y2} es igual a {x2+y2}")        # Este tipo de cadena permite incluir expresiones dentro de llaves {}
print(f"{x2} menos {y2} es igual a {x2-y2}")
print(f"{x2} multiplicado {y2} es igual a {x2*y2}")
print(f"{x2} entre {y2} es igual a {x2/y2}")
print(f"{x2} entre {y2} es igual a {x2//y2}")

print(f"{z2} entre {y2} es igual a {z2/y2}")
print(f"{z2} entre {y2} es igual a {z2//y2}")

print(f"{z2} modulo de {y2} es igual a {z2 % y2}")    # resto de division  se suele usar para numero par
print(f"{z2} elevado a {y2} es igual a {z2**y2}")
print(f"{z2} elevado a {3} es igual a {z2**3}")
print(f"La raiz cuadrada de {x2} es {x2**0.5}")

# redondeo
resultado = (round(90/7))           # redondeo
print(resultado)

valor = round(95.666666666666,2)    # redondeo a 2 deciamles
print(valor)

valor = round(95.666666666666,4)    # redondeo a 4 deciamles
print(valor)

valor = round(95.666666666666)
print(valor)

print(type(valor))                   # extrae el typo de valor en la varible valor

valor = 10.676767
print(round(valor))

num1 = 10/3
print(round(num1,2))

# Necesario el modulo Math para redondeo hacia abajo

import math

# Ejemplo de redondeo hacia arriba
numero = 3.2
redondeo_arriba = math.ceil(numero)
print(redondeo_arriba)
print(f"Redondeo hacia arriba de {numero}: {redondeo_arriba}")

# Ejemplo de redondeo hacia abajo
redondeo_abajo = math.floor(numero)
print(redondeo_abajo)
print(f"Redondeo hacia abajo de {numero}: {redondeo_abajo}")


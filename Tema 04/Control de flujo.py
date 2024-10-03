
# if una_condicion:
#   print(codigo_a)
# elif otra_condicion:
#   print(codigo_b)
# elif otra_extra_condicion:
#   print(codigo_c)
# else:
# print(codigo_a)

if 10 > 9:
    print('Es correcto')


x = True
if x:
    print('Es correcto')



mascota = 'perro'

if mascota == 'gato':
    print("tengo un gato")
elif mascota == 'perro':
    print('tienes un perro')
else:
    print("No se que animal tienes")


# If dentro de if

edad = 16
calificacion = 9

if edad < 18:
    print('Eres menor de edad')
    if calificacion >= 7:
        print('aprobado')
    else:
        print('suspendido')
else:
    print('Eres adulto')


num1 = int(input("Ingresa un número:"))
num2 = int(input("Ingresa otro número:"))

if num1 > num2:
    print('numero 1 es mayor que numero 2')
elif num2 > num1:
    print('numero 2 es mayor que numero 1')
elif num1 == num2:
    print('numero 1 es igual que numero 2')
else:
    print('algo salio mal')




num1 = int(input("Ingresa un número:"))
num2 = int(input("Ingresa otro número:"))

if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num2 > num1:
    print(f"{num2} es mayor que {num1}")
else:
    print(f"{num1} y {num2} son iguales")



edad = 18
tiene_licencia = True

if edad >= 18 and tiene_licencia == True:
    print('Puedes conducir')
elif edad >= 18 and tiene_licencia == False:
    print('No puedes conducir. Necesitas contar con una licencia')
else:
    print('No puedes conducir aún. Debes tener 18 años y contar con una licencia')


habla_ingles = True
sabe_python = False

if  habla_ingles == True and sabe_python == True:
    print("Cumples con los requisitos para postularte")
elif habla_ingles == False and sabe_python == True:
    print("Para postularte, necesitas tener conocimientos de inglés")
elif habla_ingles == True and sabe_python == False:
    print("Para postularte, necesitas saber programar en Python")
else:
    print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")

# calculo de circunferencia
radius = float(input("Introduce el radio: "))
Pi = 3.14
Circumference = 2 * radius * Pi
print(f"La circunferencia es de {Circumference}")

Area = Pi * radius * radius
print(f"La area es de {Area}")

# Años bisiestos
year = int(input("Enter the year: "))
leap_year = (
    (year % 4 == 0 and year % 100 != 0) or 
    (year % 400 == 0)
)
print(leap_year)

# Calcular impar año
year = int(input("Enter the year: "))
if year % 2 != 0:
    print(f"El año {year} es par")
else:
    print(f"El año {year} es impar")

# calcular si un numero esta entre 0 y 10
number =int(input("Enter the number: "))
if number >=0 and number <=10:
    print(f"El numero {number} esta entre 0 y 10")
else:
    print(f"El año {number} es mayor de 10 o menor que 0")


# expresiones regulares

# caracteres especiales
# car      descripción                 ejemplo
# /d       digitonumérico              v\d.\d\d
# /w       caracter alfanumérico       \w\w\w-w\w
# /s       espacio en blanco           número\s\d\d
# /D       NO numérico                 \D\D\D\D
# /W       NO alfanumérico             \w\w\w
# /S       NO espacio blanco           \S\S\S\S

#  cuantificadores
# car         descripción                       Ejemplo
# +           1 o más veces                     código_\d-\d+
# {n}         se repite n veces                 \d-\d{4}
#{n, m}       se repite de n a m veces          w{3, 5}
#{n,}         desde n hacia arriba              -\d{4, }-
# ⭑           0 ó más veces                     \w\s*\w
#?             160                               casas?



# Basico como se hace sin expresiones regulares
texto = "Si necesitas ayuda llma al (658-654-9977 las 24 horas al servicion de ayuda online"

palabra = 'ayuda' in texto
print(palabra)

# busqueda que coincida el patron
import re
patron = 'nada'
busqueda = re.search(patron, texto)
print(busqueda)

# busqueda que coincida el patron al inicio, es decir si hay 2 devuelve la de la posion mas cerca al inicio
patron2 = 'Si'
busqueda2 = re.search(patron2, texto)
print(busqueda2.start())

# busqueda que coincida el patron al final
patron3 = 'Si'
busqueda3 = re.search(patron3, texto)
print(busqueda3.end())

# busqueda que coincida el patron varias veces
patron4 = 'ayuda'
busqueda4 = re.findall(patron4, texto)
print(len(busqueda4))

# busqueda por patron que coincida
texto = "llama al 564-456-234 ya mismo"

patron = r'\d\d\d-\d\d\d-\d\d\d'
patron2 = r'\d{3}-\d{3}-\d{3}'
patron3 = re.compile(r'(\d{3})-(\d{3})-(\d{3})')
resultado = re.search(patron, texto)
resultado3 = re.search(patron3, texto)
print(resultado)
print(resultado.group())
print(resultado3.group(2))


# clave con restricciones de patron segun la contraseña que se introduzca
'''
clave = input("clave:")
patronc = 'r\D{1}\w{7}'
chequear = re.search(patronc, clave)
print(chequear)
'''


# Encuentra un patron o otro
textor = "No abrimos los lunes ni los martes"
buscar7 = re.search(r'lunes|martes', textor)
print(buscar7)


# ejercico ver si una frase saluda o no con hola al principio

import re
def verificar_saludo(frase):
    patron = 'Hola'
    verificar = re.search(patron, frase)
    if verificar:
        print('OK')
    else:
        print('No has saludado')

verificar_saludo('Hola ')

# verificar Email
import re
def verificar_email(email):
    patron = r'@\w+\.com'
    verificar = re.search(patron, email)
    if verificar:
        print("Ok")
    else:
        print("La dirección de email es incorrecta")

# codigo postal 2 alfanumericos y 4 numericos

import re
def verificar_cp(cp):
    patron = r'\w{2}\d{4}'
    verificar = re.search(patron, cp)
    if verificar:
        print("Ok")
    else:
        print("El código postal ingresado no es correcto")
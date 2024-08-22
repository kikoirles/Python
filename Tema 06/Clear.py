# esto funciona en este editor, es una forma de limpiar la pantalla tras ejecutar varios prints
from os import system

nombre = input("dime tu nombre: ")
edad = input("Dime tu nombre: ")

system('cls')

print(f"Tu nombre es {nombre}  y tienes {edad}")

# configuracion en Pycharm par asimular una consolo de sistema
# Run> Debug> Edit configuration> Añadir configuracion> nombre de la configuracion> modify configuracion> enable terminla in output console


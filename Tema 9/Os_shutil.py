import os
import shutil
import send2trash
'''
# ver ruta directorio actaul
print(os.getcwd())

# repaso crear archivo si no existe y escribirlo de nuevo
archivo = open('curso.txt', 'w')
archivo.write('texto de prueba')
archivo.close()
'''
# Ejecutar codigo por partes si no no funciona bien
'''
# mover archivo
shutil.move('curso.txt', "C:\\Users\\cirles\\Desktop\\Python\\Tema1\\Tema 9\\new place")
'''
# Ejecutar codigo por partes si no no funciona bien
'''
shutil.move('curso.txt', "C:\\Users\\cirles\\Desktop\\Python\\Tema1\\Tema 9")
'''
# Ejecutar codigo por partes si no no funciona bien
# eliminar archivo
'''
send2trash.send2trash('curso.txt')
'''
# walk
ruta = "C:\\Users\\cirles\\Desktop\\Python\\Tema1"

for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f"En la subcarpeta: {carpeta}")
    print(f"Las subcarpetas son: ")
    for sub in subcarpeta:
        print(f'\t{sub}')
    print("Los archvios son: ")
    for arch in archivo:
        print(f'\t{arch}')
        print("\n")



import os

ruta = 'C:\\Users\\cirles\\Desktop\\Python\\Tema1\\Tema 6\\Prueba.txt'

elemento = os.path.basename(ruta)
print(elemento) # muesta el final el archivo final

ruta2 = 'C:\\Users\\cirles\\Desktop\\Python\\Tema1\\Tema 6\\Prueba.txt'

elemento2 = os.path.dirname(ruta2)
print(elemento2) # primera parte del elemento sin prueba

ruta3 = 'C:\\Users\\cirles\\Desktop\\Python\\Tema1\\Tema 6\\Prueba.txt'

elemento3 = os.path.split(ruta3)
print(elemento3) # juntos seprado por tupla

os.rmdir('C:\\Users\\cirles\\Desktop\\Python\\Tema1\\Tema 6\\Tema nuevo') # si existe borrara base solo 'Tema nuevo' da error por eso ya que no existe

from pathlib import Path
carpeta = Path('/Users/cirles/Desktop/Python/Tema1/Tema 6') # vale tanto pra linux como para mac o windows
archivo = carpeta / 'prueba.txt'

mi_archivo = open(archivo)
print(mi_archivo)




carpeta = Path('/Users/cirles/Desktop/Python/Tema1/Tema 6') #Leer contenido de archivo con path

print(carpeta.read_text())# Leer contenido
print(carpeta.name) # nombre del archivo
print(carpeta.suffix) # tipode archivo
print(carpeta.stem) # el nombre sin .txt
if not carpeta.exists():
    print('Este archivo no existe')
else:
    print('Genial existe')










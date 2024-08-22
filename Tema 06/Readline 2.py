mi_archivo = open('prueba.txt')  # abrir el archvio

una_linea = mi_archivo.readline()
print(una_linea.upper())

una_linea = mi_archivo.readline()
print(una_linea.strip())

una_linea = mi_archivo.readline()
print(una_linea.lower())

mi_archivo.close()  # cerrar el archivo por memoria
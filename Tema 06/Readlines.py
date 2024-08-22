mi_archivo = open('prueba.txt')  # abrir el archvio

todas = mi_archivo.readlines()   # listas
print(todas)

todas = todas.pop()

mi_archivo.close()  # cerrar el archivo por memoria
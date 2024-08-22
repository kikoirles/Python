mi_archivo = open('Prueba.txt')

linea1 = (mi_archivo.readline())
linea1 = (mi_archivo.readline()) # repetir tantas veeces como linas quieres saltar
print(linea1)                    # va sustituyendo el valor de la varible

mi_archivo.close()
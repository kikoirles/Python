mi_archivo = open('prueba.txt') # abrir el archvio

print(mi_archivo.readline()) # lee y muestra la primera linea pero se la guarda
                             # de tal forma que el siguiente readline puesto empezara por la segunda

# primera_linea = mi_archivo.readline()
# print(primera_linea)                # lee y muestra la primera linea en una variable
                                    # es una mejor forma de guara los print

mi_archivo.close() # cerrar el archivo por memoria


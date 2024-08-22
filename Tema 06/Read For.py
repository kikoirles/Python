mi_archivo = open('prueba.txt')  # abrir el archvio

for l in mi_archivo:
    print('Aqui dice' + l)

mi_archivo.close()  # cerrar el archivo por memoria
# Utiliza el método writelines para escribir los valores de la siguiente lista al final del archivo "registro.txt" . Inserta un tabulador entre cada elemento de la lista para separarlos.

# registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

# Imprime el contenido completo de "registro.txt" al finalizar.


registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

"Nuevo inicio de sesión"

archivo = open('registro.txt','a')

for item in registro_ultima_sesion:
    archivo.writelines(item +'\t')

archivo.close

archivo = open('registro.txt','r')

lectura = archivo.read()
print(lectura)

archivo.close
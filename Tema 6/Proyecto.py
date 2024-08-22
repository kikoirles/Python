# imports
import sys
import shutil
import os
from pathlib import Path

# Titulo de bienvenida cuenta los parametros de uan funcion mas adelante
Bienvenida = "\n"f"Buenas este es un inventario de recetas"
print(Bienvenida.upper())

# Directorio mostrar categorias
archivos_categorias = Path(r"C:\Users\cirles\Desktop\Python\Tema1\Tema 6\Recetas\Recetas")

# Directorio todas las recetas
archivos_recetas = Path(Path.home(),"Desktop","Python","Tema1","Tema 6","Recetas")
print("\n"f"Las recetas estan en {archivos_recetas}")

# Directorio recetas carne
archivos_recetas_carnes = Path(r"/Tema 6/Recetas/Recetas/carnes")

# Directorio recetas ensalada
archivos_recetas_ensaladas = Path(r"/Tema 6/Recetas/Recetas/ensaladas")

# Directorio recetas pastas
archivos_recetas_pastas = Path(r"/Tema 6/Recetas/Recetas/pastas")

# Directorio recetas postres
archivos_recetas_postres = Path(r"/Tema 6/Recetas/Recetas/postres")


print("\n""LISTA DE RECETAS""\n")

# Funcion para mostrar todas la categorias
def mostrar_all_categorias():
    categorias = list(archivos_categorias.iterdir())
    for categorias in categorias:
        print(categorias.name)



mostrar_all_categorias()

# Función para buscar recestas carne
def buscar_recetas_carnes():
    # Inicializar el contador de recetas (lista de archivos .txt de carnes)
    recetas = list(archivos_recetas_carnes.rglob("*.txt"))

    # Imprimir cada receta encontrada (nombre del archivo sin extensión)
    for receta in recetas:
        print(receta.stem)

# Función para buscar recestas de ensaladas
def buscar_recetas_ensaladas():
    # Inicializar el contador de recetas (lista de archivos .txt de carnes)
    recetas = list(archivos_recetas_ensaladas.rglob("*.txt"))

    # Imprimir cada receta encontrada (nombre del archivo sin extensión)
    for receta in recetas:
        print(receta.stem)


# Función para buscar recestas de pastas
def buscar_recetas_pastas():
    # Inicializar el contador de recetas (lista de archivos .txt de carnes)
    recetas = list(archivos_recetas_pastas.rglob("*.txt"))

    # Imprimir cada receta encontrada (nombre del archivo sin extensión)
    for receta in recetas:
        print(receta.stem)

# Función para buscar recestas de postres
def buscar_recetas_postres():
    # Inicializar el contador de recetas (lista de archivos .txt de carnes)
    recetas = list(archivos_recetas_postres.rglob("*.txt"))

    # Imprimir cada receta encontrada (nombre del archivo sin extensión)
    for receta in recetas:
        print(receta.stem)


# Total Función para buscar y contar recetas todas
def buscar_recetas():
    # Inicializar el contador de recetas
    recetas = list(archivos_recetas.rglob("*.txt"))
    # Imprimir cada receta encontrada
    for receta in recetas:
        print(receta.stem)
    # Retornar el número total de recetas
    return len(recetas)

# Funcion obtenr todas la recetas
def buscar_todas_recetas():
    # Inicializar el contador de recetas
    recetas = list(archivos_recetas.rglob("*.txt"))
    # Imprimir cada receta encontrada
    for receta in recetas:
        print(receta.stem)
    # Retornar el número total de recetas
    return len(recetas)


# Llamada a la función y mostrar el total de recetas
cantidad_recetas = buscar_recetas()
print("\n"f"La cantidad total de recetas es: {cantidad_recetas}")


# mostrar menu
def mostrar_menu():
    print("\n""Seleccione una opción del menú a realizar :")
    print("1- Leer receta")
    print("2- Crear receta")
    print("3- Crear categoria")
    print("4- Eliminar receta")
    print("5- Eliminar categoria")
    print("6. Salir")
    return "Opción no válida"

def ejecutar_opcion(opcion):
    if opcion == 1:
        print(mostrar_all_categorias())
        categoria = input("¿Qué categoría seleccionas? ")                                                   # Preguntar la categoria primer if alto
        if categoria.lower() == "carnes":
            print("Has seleccionado la categoría de carnes.")
            print(buscar_recetas_carnes())                                                                  # muestra el resultado de la funcion llamada
            archivo_lectura_carne = input("Selecciona un archivo para leer (sin extensión): ") + ".txt"     # Preguntar el archivo
            ruta_archivo_carne = Path(r"/Tema 6/Recetas/Recetas/carnes") / archivo_lectura_carne            # establece la ruta del archivo
            if ruta_archivo_carne.exists() and ruta_archivo_carne.is_file():                                # verifica l existencia del directorio y si esta el archivo
                with ruta_archivo_carne.open('r') as mi_archivo_carne:                                      # Abrir el archivo en lectura
                    contenido = mi_archivo_carne.read()
                    print(contenido)

        elif categoria.lower() == "ensaladas":
            print("Has seleccionado la categoría de ensaladas.")
            print(buscar_recetas_ensaladas())
            archivo_lectura_ensalada = input("Selecciona un archivo para leer (sin extensión): ") + ".txt"  # Preguntar el archivo
            ruta_archivo_ensalada = Path(r"/Tema 6/Recetas/Recetas/ensaladas") / archivo_lectura_ensalada
            if ruta_archivo_ensalada.exists() and ruta_archivo_ensalada.is_file():
                with ruta_archivo_ensalada.open('r') as mi_archivo_ensalada:
                    contenido = mi_archivo_ensalada.read()
                    print(contenido)


        elif categoria.lower() == "pastas":
            print("Has seleccionado la categoría de pastas.")
            print(buscar_recetas_pastas())
            archivo_lectura_pasta = input("Selecciona un archivo para leer (sin extensión): ") + ".txt"
            ruta_archivo_pasta = Path(r"/Tema 6/Recetas/Recetas/pastas") / archivo_lectura_pasta
            if ruta_archivo_pasta.exists() and ruta_archivo_pasta.is_file():
                with ruta_archivo_pasta.open('r') as mi_archivo_pasta:
                    contenido = mi_archivo_pasta.read()
                    print(contenido)

        elif categoria.lower() == "postres":
            print("Has seleccionado la categoría de postres.")
            print(buscar_recetas_postres())
            archivo_lectura_postre = input("Selecciona un archivo para leer (sin extensión): ") + ".txt"
            ruta_archivo_postre = Path(r"/Tema 6/Recetas/Recetas/postres") / archivo_lectura_postre
            if ruta_archivo_postre.exists() and ruta_archivo_postre.is_file():
                with ruta_archivo_postre.open('r') as mi_archivo_postre:
                    contenido = mi_archivo_postre.read()
                    print(contenido)
        else:
            print("Categoría no válida.")


    elif opcion == 2:
        print(mostrar_all_categorias())                                                                   # muestra todas la categorias para que la siguiente pregunta se mas vistosa
        ruta_base = Path(r"C:\Users\cirles\Desktop\Python\Tema1\Tema 6\Recetas\Recetas")
        busqueda_categoria = input("¿En que categoria va a estar la receta que vamos a crear? ")          # sin esto no podemos saber a que receta desea borrar

        ruta = os.path.join(ruta_base,busqueda_categoria)                                                 # juntamos la varible del campo tipo de recetas hemos pedido antes con la url base
        os.chdir(ruta)                                                                                    # cambio de directorio# nos cambiamos al directorio de la categoria que le hemos juntado antes previamente de haber preguntado el tipo

        new_receta = input("¿Como se llama la nueva receta? ")
        contenido_receta = input("¿Pasos de la receta: ")

        if not os.path.exists(new_receta):
            # Crea y abre el archivo en modo escritura, esto también lo crea si no existe
            with open(new_receta, 'w') as f:
                f.write(contenido_receta)  # Escribe contenido vacío o inicial si lo deseas
            print(f"Archivo '{new_receta}' creado exitosamente.")
        else:
            print(f"El archivo '{new_receta}' ya existe.")



    elif opcion == 3:
        print("Has seleccionado la Opción 3.")
        new_categoria_directory = input("¿Como se llama la nueva categoria? ")
        ruta_base = Path(r"C:\Users\cirles\Desktop\Python\Tema1\Tema 6\Recetas\Recetas")
        os.chdir(ruta_base)                                                                     # Establecemos la ruta donde se crearan los directorios
        if not os.path.exists(new_categoria_directory):
                                                                                                # Crea el directorio
            os.makedirs(new_categoria_directory)
            print(f"Categoria '{new_categoria_directory}' creado exitosamente.")
        else:
            print(f"La categoria '{new_categoria_directory}' ya existe.")

    elif opcion == 4:
        print(mostrar_all_categorias())                         # muestra todas la categorias para que la siguiente pregunta se mas vistosa
        ruta_base = Path(r"C:\Users\cirles\Desktop\Python\Tema1\Tema 6\Recetas\Recetas")
        busqueda_categoria = input("¿En que categoria esta? ")  # sin esto no podemos saber a que receta desea borrar

        ruta = os.path.join(ruta_base, busqueda_categoria)      #  nos cambiamos al directorio de la categoria que le hemos peguntado antes
        os.chdir(ruta)                                          # cambio de directorio
        print(buscar_todas_recetas())                           #  esto se podria cambiar y que mostrase solo las de la categoria que se elgio antes pero habria que multipilcar el codigo por cada categoria al crear una nueva

        archivo_a_eliminar = input("¿Qué receta deseas eliminar? ")
        if os.path.exists(archivo_a_eliminar):
            try:
                os.remove(archivo_a_eliminar)
                print(f"La receta {archivo_a_eliminar} ha sido eliminado.")
            except PermissionError:
                print(f"No tienes permiso para eliminar el archivo {archivo_a_eliminar}.")
            except Exception as e:
                print(f"Ocurrió un error al intentar eliminar el archivo: {e}")
        else:
            print(f"El archivo {archivo_a_eliminar} no se encuentra en el directorio.")


        # mostrar todas las categorias
        # vamos a indicar que categoria queremos eliminar

    elif opcion == 5:
        print(mostrar_all_categorias())                                                         # mostrar todas las categorias
        ruta_base = Path (r"C:\Users\cirles\Desktop\Python\Tema1\Tema 6\Recetas\Recetas")       # Ruta base de recetas
        categoria_eliminar = input("¿Qué categoría deseas eliminar? ")                          # preguntamos que categoria a eliminar
        ruta = os.path.join(ruta_base, categoria_eliminar)                                      # unificacmos la base mas el directorio o la categoria a eliminar
        if os.path.exists(ruta):
            try:
                shutil.rmtree(ruta)                                                             # Eliminamos la ruta comple, pero python solo borra el ultimo
                print(f"La categoria '{categoria_eliminar}' se a eliminado exitosamente.")
            except Exception as e:
                print(f"Error al eliminar la categoria '{categoria_eliminar}': {e}")
        else:
            print(f"El directorio '{categoria_eliminar}' no existe.")

        # salir del programa

    elif opcion == 6:
        sys.exit()                                                                              # Sale del programa
        print("Saliendo del programa...")
    else:
        print("Opción no válida. Por favor, intenta de nuevo.")



# Funcion final introducir un numero
# muestra la funcion de mostrar menu
# especificamos que le pase un numero, si no para el codigo
# si le pasamos un numero ejecutamos la funcion ejecutar opcion

def numero():
    while True:
        mostrar_menu()
        try:
            opcion = int(input("\n""Introduce el número de tu elección: "))
            if opcion == 0:
                ejecutar_opcion(opcion)
                break
            else:
                ejecutar_opcion(opcion)
        except ValueError:
            print("Entrada inválida. Por favor, introduce un número.")

numero()


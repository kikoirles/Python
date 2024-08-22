# try       intenta esto...
# except    si sale mal, haz esto ...
# finaly    pase lo que pase, haz esto ..

def suma():
    print(10 + 30)
    input("No hay error")

def suma2():
    n1 = int(input("numero 1: "))
    n2 = int(input("numero 2: "))
    print(n1 +n2)
    print("Gracias por sumar")

# suma2()

try:
    suma2()
    # codigo que queremos probar
except TypeError:
    print("Estas intentando Concatenar tipos distintos")
    # codigo a ejecutar dependiendo de error
except ValueError:
    print("Ese no es un numero")
else:
    print("hicistes todo bien")
    # codigo a ejecutar si no hay un error
finally:
    print("Eso fue todo")
    # codigo que se va a ejecutar de todos modos

def pedir_numeor():

    while True:
        try:
            numero = int(input("Dame un numero: "))
        except:
            print("Ese no es un numero")
        else:
            print(f"ingresastes un nuemro {numero}")
            break
    print("Gracias")

pedir_numeor()

# Ejercicio Erro completo

def abrir_archivo(nombre_archivo):
    try:
        archivo = open(nombre_archivo)
    except FileNotFoundError:
        print("El archivo no fue encontrado")
    except:
        print("Error desconocido")
    else:
        print("Abriendo exitosamente")
    finally:
        print("Finalizando ejecución")

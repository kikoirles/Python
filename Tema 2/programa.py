# programa final de de ventas

nombre = input("cual es tu nombre:")
cantidad_ventas = input("Dinero total de ventas que has realizado:")

# cantidad de ventas a Float
cantidad_ventas_float = float(cantidad_ventas)
# nombre en str
nombre_str = str(nombre)

comison = ((cantidad_ventas_float * 13) / 100)
comison_r = round(comison,2)

print(f"{nombre_str} a obtenido de comison {comison_r} beneficos por su ventas ")


# programa final de ventas version simple

nombre = input("Por favor, dime tu nombre: ")
ventas = int(input("Diga sus ventas totales del mes: "))

comision = round(ventas * 13 / 100,2)

print(f"Hola {nombre}, tus comisiones de este mes son de ${comision}")
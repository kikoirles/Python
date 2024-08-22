# Devuelve_todo el tuple

precios_cafe = [('Capuchino',1.5),('Expreso',1.2),('Moka',1.9)]

for elemento in precios_cafe:
    print(elemento)

# Devuelve el precio multiplicado referente a su cafe
precios_cafe = [('Capuchino',1.5),('Expreso',1.2),('Moka',1.9)]

for elemento,precio in precios_cafe:
    print(elemento,precio * 0.25)

# saber cual es el cafe mas caro
precios_cafe = [('Capuchino',1.5),('Expreso',1.2),('Moka',1.9)]

def cafe_mas_caro(lista_precios):
    precio_mayor = 0 # variable que guarda el precio mayor de la lista
    cafe_caro = ''   # variable que guarda el cafe mas caro de la lista

    for cafe,precio in  lista_precios:
        if precio > precio_mayor:  #compara si el precio del cafe es mas alto que 0 en el primer bucle,luego 2 bucle 1,5
            precio_mayor = precio # asigna el valor mas alto de precios a la variable precios_mayot
            cafe_caro = cafe # asigna el valor mas alto de cafe a la variable cafe_caro
        else:
            pass
    return (cafe_caro,precio_mayor) # devuelve el valor de las dos variables
print(cafe_mas_caro(precios_cafe))

cafe, precio = cafe_mas_caro(precios_cafe) # asiganacion a varible doble del dels resultado de la función
print(f"El cafe mas caro es {cafe} cuyo precio es {precio}")
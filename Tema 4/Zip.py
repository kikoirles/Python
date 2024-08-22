nombre = ['Ana','Hugo','Valeria']
edades = [65,29,21]
ciudades = ["Lima","Madrid","Alicante"]

combinacion = list(zip(nombre,edades,ciudades))
print(combinacion)

for nombre,edad,ciudad in combinacion:
    print(f"{nombre} con {edad} años vive en {ciudad}")


capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

combinacion = list(zip(capitales,paises))

for paises,capitales in combinacion:
    print(f"La capital de {paises} es {capitales}")




marcas = ["Nike", "Lenovo", "Nissan"]
productos = ["zapatillas", "notebook", "automóviles"]

mi_zip = zip(marcas, productos)
print(list(mi_zip))
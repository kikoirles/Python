dic = {'calve1':2000,'cleve2':200}

a = dic.popitem()
print(a)
print(dic)

"""
manteniendo el cursor encima del nuevo metodo sale la documentacion de python
Este módulo proporciona compatibilidad en tiempo de ejecución con sugerencias de tipo.

Considere la siguiente función:

def surface_area_of_cube(edge_length: float) -> str:
    return f"The surface area of the cube is {6 * edge_length ** 2}."
La función toma un argumento que se espera que ser una instancia de , como se indica en el tipo hint . Se espera que la función devuelva una instancia de , como lo indica la sugerencia.surface_area_of_cubeedge_length: float-> str

Si bien las sugerencias de tipo pueden ser clases simples como o , También pueden ser más complejos. El módulo proporciona un vocabulario de Sugerencias de tipo más avanzadas.
"""
# remover cracteres de la izquierda
print(",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#".lstrip(",:%_#"))

# insert en posicion de arrary indicada
frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]

frutas.insert(3,"naranja")

print(frutas)

# valor booleano entre dos listas si son iguales en este caso falso
marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}

marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)


print(conjuntos_aislados)
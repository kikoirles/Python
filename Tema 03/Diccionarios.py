# Diccionarios
diccionario = {'c1':'valor1','c2':'valor2'}
print(type(diccionario))
print(diccionario)

resultado = diccionario['c2']
print(resultado)

#  caos de diccionario con listas
dic = {'c1':55,'c2':[10,20,30],'c3':{'s1':100,'s2':200}}
print(dic['c3']['s2'])

# actividad
dic = {'c1':['a','b','c'],'c2':['d','e','f']}
clave_E = dic['c2'][1].upper()
print(clave_E) # devuelve E porque d es el 0 le hemos pdedido el 1

dic = {1:'a',2:'b'}
print(dic)

dic[3] = 'c'
print(dic)

dic[2] = '8'
print(dic)

print(dic.keys())
print(dic.values())
print(dic.items())


# actividad
mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
print(mi_dict)

resultado = mi_dict['puntos']['points2'][1]
print(resultado)

mi_dic2 = {"nombre":"Karen","apellido":"Jurgens","edad":35,"ocupacion":"Periodista"}

mi_dic2["pais"] = "Colombia"
mi_dic2["edad"] = 36
mi_dic2["ocupacion"] = "Editora"

print(mi_dic2)
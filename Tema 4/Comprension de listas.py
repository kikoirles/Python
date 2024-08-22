palabra = 'python'
lista = []

for letra in palabra:
    lista.append(letra)
print(lista)


palabra = 'python'

lista2 = [letra for letra in palabra]
print(lista2)


lista3 = [num for num in range(0,21,2)]
print(lista3)



lista3 = [num if num * 2 > 10 else 'no' for num in range(0,21,2)]
print(lista3)

pies = [10,20,30,40,50]
metro = [pie * 3.87 for pie in pies]
print(metro)


pies = [10, 20, 30, 40, 50]
metro = [pie * 3.87 for pie in pies]
metro_redondeado = [round(valor, 2) for valor in metro]
print(metro_redondeado)


valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_pares = [valor for valor in valores if valor % 2 == 0]
print(valores_pares)

temperatura_fahrenheit = [32, 212, 275]
grados_celsius = [(temp - 32) * (5/9) for temp in temperatura_fahrenheit]
print(grados_celsius)
archivo = open('prueba1.txt', 'w')

lista = ['hola', 'mundo', 'estoy', 'aqui']

for p in lista:
    archivo.writelines( p + '\n')

archivo.close

# hola
# mundo
# estoy
# aqui
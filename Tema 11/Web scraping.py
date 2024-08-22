import bs4
import requests
import lxml # da un error si no se importa el numero aun uqe nos indique que no se usa

resultado = requests.get("https://escueladirecta-blog.blogspot.com/")
print(type(resultado)) # guarda los datos de una peticion get en una variable

print(resultado.text)

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')
print(sopa) # hace una cnversion de los valores a lxml

# imprimr solo una etiqueta: [<title>Escuela Directa | Blog</title>]
print(sopa.select('title'))

# imprimir solo una etiqueta seleccionada pero sin en nombre de etiqueta
print(sopa.select('title')[0].getText())
                            # indice 0 equivale a la linea en caso de que
                            # busque y encuentra varias lienas


columna_lateral = sopa.select('.content p')

for p in columna_lateral:
    print(p.getText)




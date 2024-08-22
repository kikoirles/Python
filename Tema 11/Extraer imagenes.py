import bs4
import requests
import lxml

resultado = requests.get('https://www.escueladirecta.com/courses/')

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

imagenes = sopa.select('img')
for imagen in imagenes:
    print(imagen)

print('\n')


sopa2 = bs4.BeautifulSoup(resultado.text, 'lxml')

# pogamos que solo queremos la imagens de los cursos de class ='couse'

imagenes2 = sopa2.select('.course-box-image')[0]['src']
for imagen2 in imagenes2:
    print(imagen2)

imagen_curso_1 = requests.get(imagenes2)
 # guardamos la imagen del curso en una variable


f = open('mi_imagen.jpg', 'wb') # generamos un archivo binario de lectura
f.write(imagen_curso_1.content) # solicitamos guardar el contenido de la imagen el archivo creado 
f.close()


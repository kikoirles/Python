# archivo = open('prueba.txt','r') modo solo lectura
# archivo = open('prueba.txt','w') modo escritura
# archivo = open('prueba.txt','a') modo escritua desde el final

# archivo = open('prueba.txt', 'r')
# archivo.write('soy el nuevo texto') # da eRRor ya que esta en modo lectura
# archivo.close()

archivo = open('prueba1.txt', 'w')
archivo.write('soy el nuevo texto \n')      # Dos lineas escritas tambie con ''' al principio y al final registas los enter
archivo.write('linaa 2 ')                   # escirtura basica pero si pones un archivo ya con lias lo borra
archivo.close()

# Clase nos permite hacer programacion orientada a objetos
# clase > atributos
#       > metodos
# Ejmplo
# clase pajaro > atributos color,tamaño,tipo,habitat,peso
#              > metodos   volar,comer,piar

# podemos hacer que hayan varios pajaros ejemplo

# clase pajaro > atributos color,tamaño,tipo,habitat,peso
#              > metodos   volar,comer,piar
#              > objetos  twity,pepe(nombre de cada pajaro)

class Pajaro:
    pass

mi_pajaro = Pajaro()    # son dos pajaros que tienen la misma clase
otro_pajaro = Pajaro()

print(type(mi_pajaro))
print((mi_pajaro))
print((otro_pajaro)) # pero existen cada uno con su identificador

# Otro ejemplo basico

class Dinosaurio:
    pass

velociraptor = Dinosaurio()
tiranosaurio_rex = Dinosaurio()
braquiosaurio = Dinosaurio()
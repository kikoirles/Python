# Atributos de instancia (que varian)
class Pajaro:

    def __init__(self, color):
        self.color = color


mi_pajaro = Pajaro('Negro')

mi_pajaro.color

print(mi_pajaro.color)



class Pajaro3:

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie


mi_pajaro3 = Pajaro3('Negro','Tucan')

mi_pajaro3.color
mi_pajaro3.especie

print(f"Mi pajaro es un {mi_pajaro3.especie} y es de color {mi_pajaro3.color}")


# atributos de clase se aplican a todos los objetos de clase ejemplo alas

class Pajaro4:

    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie


mi_pajaro4 = Pajaro4('Negro','Tucan') # mi Pajaro 4 tiene atributos Alas , Negro y Tucan
mi_pajaro43 = Pajaro4                              # mi Pajaro 43 tiene atributos Alas solamente
mi_pajaro4.color
mi_pajaro4.especie

print(f"Mi pajaro es un {mi_pajaro4.especie} y es de color {mi_pajaro4.color}")

print(mi_pajaro4.alas)
print(mi_pajaro4.especie)
print(mi_pajaro43.alas)
print(mi_pajaro43.especie)

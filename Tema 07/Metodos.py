# Metodos
class Pajaro:

    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print('pio')

    def volar(self, metros):
        print(f"El pajaro ha volado {metros} metros")

    def piar_color(self):
        print('pio, mi color es {}'.format(self.color))     #es una forma de llamara a otro atributo que no se llama en la funcion

piolin = Pajaro('amarillo','canario')          # hemos definido piolin a la clase pajaro
                                                                # atributo estatico alas Aplicado
                                                                # atributos varible color y especie Aplicado

piolin.piar()           # la funcion piar aplica solo a la clase pajaros y es llaada asi
#pajaro_loco.piar()     # No esta definido en la clase Pajaro no pude acceder a la funcion

piolin.volar(50)

piolin.piar_color()

# Ejemplos de metodos

class Perro:
    def ladrar(self):
        print('Guau!')

mi_perro = Perro()  # Crear una instancia de la clase Perro
mi_perro.ladrar()  # Llamar al método ladrar en la instancia



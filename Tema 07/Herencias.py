# Herencia nos permite hacer nuevas clases que esta relacionadas y pertenecen a otras clases con atributos que son iguales pero hay otro distintintos o nuevo
class Animal:                           # Animales > Pajaros(Animales)
                                        #          > Peces(Animales)

    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("Este animal ha nacido")

class Pajaro(Animal):
    pass

    def alas(self):
        print("Al ser un animal tipo volador tiene alas tambien")



print(Animal.__subclasses__())
print(Pajaro.__bases__)

piolin = Pajaro(2, 'amarilo')

piolin.nacer()

# Ejemplo Crea una clase llamada Persona, que tenga los siguientes
# atributos de instancia: nombre, edad. Crea otra clase, Alumno, que herede de la primera estos atributos.

class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


class Alumno(Persona):
    pass

# Otro ejemplo de Herencia

class Vehiculo:

    def acelerar(self):
        print("Estoy Acelerando")

    def frenar(self):
        print("Estoy frenando")


class Automovil(Vehiculo):
    pass
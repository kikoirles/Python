# Tambien es posible hacer herencia multiples
# Ejemplo   Manule y Sara tienen un hijo Raul
#           Padre Manuel        Manuel
#           Madre Sara          Sara
#           Hijo Raul           Raul(manuel,Sara)
#           nIesto Paco         Paco(Raul)

class Animal:


    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("Este aniaml ha nacido")

    def hablar(self):
        print("Este animal emite un sonido")

class Pajaro(Animal):   # Para la clase pajaro el metodo init nos pide dos parametros
                        # Pero nosotros queremos agregar uno nuevo a los que ya estan

    def __init__(self, edad, color, altura_vuelo):
            self.edad = edad
            self.color = color
            self.altura_vuelo = altura_vuelo

    def hablar(self): # lo sobreescrive el nuevo metodo Hablar de pajaro es pio
        print("pio")

    def volar(self, metros): # nuevo metodo de pajaro
        print(f"El pajaro vuela {metros} metros")

# piolin = Pajaro(3, 'amarillo') # da fallo ahora pide 3 atributos

cerdo = Animal(4, "rosa")
piolin = Pajaro(4, "amarillo", 20)

piolin.nacer()

piolin.volar(100)




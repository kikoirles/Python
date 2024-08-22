class Padre:
    def hablar(self):       # Va primero orden ascendente
        print("hola")

class Madre:
    def reir(self):
        print("ja ja")

    def hablar(self):
        print("que tal")

class Hijo(Padre, Madre):   # Padre el hablar prevalece porque esta antes aqui si cambias
                            # El orden, Madre primero el hbalar seria primero el de madre ja ja
    pass

class Nieto(Hijo):
    pass

mi_nieto = Nieto()

mi_nieto.hablar()

print(Nieto.__mro__) # Muestra el odden de resolucion a buscar un metdo en clase

# Ejercicio sustitucion de nuevo metodo en herencia
class Padre():
    color_ojos = "marrón"
    tipo_pelo = "rulos"
    altura = "media"
    voz = "grave"
    deporte_preferido = "tenis"

    def reir(self):
        return "Jajaja"

    def hobby(self):
        return "Pinto madera en mi tiempo libre"

    def caminar(self):
        return "Caminando con pasos largos y rápidos"


class Hijo(Padre):
    def hobby(self):
        return "Juego videojuegos en mi tiempo libre"


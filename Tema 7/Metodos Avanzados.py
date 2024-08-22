# Tipos de metodos

# Método de Instancia:
# - Definido con def.
# - Recibe self como primer parámetro.
# - Puede acceder y modificar los atributos de la instancia.

# Método de Clase:
# - Definido con @classmethod.
# - Recibe cls como primer parámetro.
# - Puede acceder y modificar atributos de la clase.

# Método Estático:
# - Definido con @staticmethod.
# - No recibe self ni cls.
# - No puede acceder ni modificar atributos de la instancia o de la clase.

# Metodos de instancia vistos antes en metodos
class Pajaro:

    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print('pio')

    def volar(self, metros):
        print(f"El pajaro ha volado {metros} metros")
        self.piar()

    def pintar_negro(self):
        self.color = 'negro'
        print(f"Ahora el pajaro es {self.negro}")

# piolin = Pajaro('amarillo','canario')
# piolin.pintar_negro()
# piolin.volar(50)
# piolin.alas = False

# Metodos de clase

class Jugador:
    vivo = False

    @classmethod
    def revivir(cls):
        cls.vivo = True

Jugador.revivir()

# Metodo estatico

class Mascota:
    @staticmethod
    def respirar():
        print("Inhalar... Exhalar")

Mascota.respirar()

# Ejerccio chungo
# Tiene que tener esto el Ornitorrinco
# - poner_huevos()

# - tiene_pico = True

# - vertebrado = True

# - venenoso = True

- nadar()

- caminar()

- amamantar()
class Vertebrado:
    vertebrado = True

class Ave(Vertebrado):
    tiene_pico = True
    def poner_huevos(self):
        print("Poniendo huevos")

class Reptil(Vertebrado):
    venenoso = True

class Pez(Vertebrado):
    def nadar(self):
        print("Nadando")
    def poner_huevos(self):
        print("Poniendo huevos")

class Mamifero(Vertebrado):
    def caminar(self):
        print("Caminando")
    def amamantar(self):
        print("Amamantando crías")

class Ornitorrinco(Mamifero, Pez, Reptil, Ave): # No entra vetebrado ya que con poner una clase Pez, Reptil, Ave o Mamifero,
        pass                                    # La subclase pez por ejemplo ya tiene el metod buscado de la clase vertebrado


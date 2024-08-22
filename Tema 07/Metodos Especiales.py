class CD:

    def __init__(self, autor, titulo, canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones

    def __str__(self):                                  # Metodo especialpermite definir la forma que devuelve un string
        return f"Album: {self.titulo} de {self.autor}"  # Dar formato de salida

    def __len__(self):
        return self.canciones   # devuelve el numero caciones

    def __del__(self):          # devuelve el mensaje que necesita del de abajo del codigo
        print("se ha eliminado el CD")

mi_cd = CD('Pink Floyd', 'The Wall', 24)

print(mi_cd)

del mi_cd # ahora a parte de borralo con el __del__ informa que lo ha borrrado



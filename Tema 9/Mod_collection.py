from collections import Counter, deque
from collections import defaultdict
from collections import namedtuple
# counter
# defaultdict
# namedtuple

# counter cuenta los numero, tiene varios modulos como opciones
numeros = [8,6,9,5,7,1,3,4,6,7,8]
frase = "al pan pan y el vino vino"
print(Counter(numeros))
print(Counter(frase.split()))

serie = Counter([8,6,9,5,7,1,3,4,6,8,7,8])
print(serie.most_common())

mi_dic = {'uno':'rojo','dos':'amarillo','tres':'verde' }
print(mi_dic['dos'])

# defaultdict añade en caso de estar vacio un campo del diccionar le asigna un valor
mi_dic2 = defaultdict(lambda: 'nada')

mi_dic2['uno'] = 'verde'
print(mi_dic2['dos'])

print(mi_dic2)

# namedtuple

Persona = namedtuple('Persona',['nombre', 'altura', 'peso'])
ariel = Persona('Ariel', 1.57, 78)

print(ariel[2])


# Metodo de Counter añadir en una lista por la parte izquierda

lista_ciudades = deque(["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"])

lista_ciudades.appendleft("Barcelona")

print(lista_ciudades)
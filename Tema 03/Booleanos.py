
# Booleano
var1 = True
Var2 = False
print(type(var1))
print(var1)

numero = 5 > 2 + 3
print(type(numero)) # Fasle 5>5
print(numero)

numero1 = 5 >= 2 + 3
print(type(numero)) # True 5>= 5
print(numero1)

numero2 = bool(5 < 6) # True 5 < 6
print(numero2)


lista = [1,2,3,4] # False 5 no esta en lista 
control = 5 in lista
print(control)

# Booleano ejemplos
print(bool(1))         # True
print(bool(0))         # False
print(bool(True))      # True
print(bool(False))     # False
print(bool(-1))        # True
print(bool(None))      # False
print(bool(''))        # False
print(bool("hello"))   # True
print(bool([]))        # False
print(bool([10, 20]))  # True

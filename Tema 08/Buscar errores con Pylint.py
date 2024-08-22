# para ello instalar Pylint Primeramente
numero1 = 500
print(numero)

# C:\Users\cirles\Desktop\Python\Tema1\Tema 8>pylint "Buscar errores con Pylint.py" -r y

# Buscar errores con Pylint.py:1:0: C0103: Module name "Buscar errores con Pylint" doesn't conform to snake_case naming style (invalid-name)
# Buscar errores con Pylint.py:2:0: C0103: Constant name "numero1" doesn't conform to UPPER_CASE naming style (invalid-name)

# Esta es la que interesa
# Buscar errores con Pylint.py:3:6: E0602: Undefined variable 'numero' (undefined-variable)
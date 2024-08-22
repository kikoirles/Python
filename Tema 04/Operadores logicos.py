
# Operadores logicos
# Mayor que     >
# menos que     <
# mayor o igual >=
# menor o igual <=
# igual         == # nota esto compara = solo asigna variable = 'rojo'
# Diferente     !=

var1_bol = 10 == 20
print(var1_bol)

var2_bol = 20 == 20
print(var2_bol)

var1_bol_color = 'blaco' == 'negro'
print(var1_bol_color)

var1_bol_color1 = 'blaco' != 'negro'
print(var1_bol_color1)

var1_bol_color2 = 'blanco' == 'Blanco'.lower()
print(var1_bol_color2)

# operadores logico que concatenan 3
mi_bool1 = 4 < 5 and 5 > 6      # F tienen que cumplirse las dos condiciones
print(mi_bool1)

texto = "esta frase es breve"
mi_bool12 = ('frase' in texto) and ('es' in texto)
print(mi_bool12)

mi_bool2 = 1 == 10 or 3 == 3     # V se cumple al menos una condicion
print(mi_bool2)

mi_bool23 = not 'a' == 'a'   # F convierte la expresiona al reves en ese caso a == a --> verdadero
print(mi_bool23)                                                          # not a == a ---> falso

mi_bool23 = not 'b' == 'a'   # niega la comparaion
print(mi_bool23)

frase = "Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
palabra1 = "éxito"
palabra2 = "tecnología"

mi_bool = not palabra1 in frase and not palabra2 in frase
print(mi_bool)
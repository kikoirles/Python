# conversiones
num1 = 20
num2 = 30.5

num1 = num1 + num2

print(num1)
print(num2)

print(type(num1))
print(type(num2))


# conversiones de tipo float a int
num1 = 7.5
num2 = int(num1)
print(num2)


# conversiones
num3 = 20.5
print(num3)         # 20,5
print(type(num3))   # <class 'float'>

num4 = int(num3)    # 20,5 --> 20 (elimina el decimal no redondea)
print(num4)         # 20
print(type(num4))   # <class 'int'>


x = 10
y = 12

print("Mis numeros son " + str(x) + " y " + str(y))    # conversion muy costosa

# conversion mas simple format al final saber que existe esta forma

x = 10.5
y = 12

print(f"Mis numeros son {x} y {y} y su suma es {x + y}".format(y,x,y+x))

# conversion mas simple con format
color = "rojo"
matricula = 123456J
print(f"El coche es de color {color} y su matricula es {matricula}")




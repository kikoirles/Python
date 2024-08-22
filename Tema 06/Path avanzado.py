from pathlib import Path

base = Path.home() # Path devuelve el director de del usuario principal
print(base)

ruta = Path(Path.home(),"Curso Python","Día 6","practicas_path.py")
print(ruta)

guia = Path("Barcelona","Sagrada_familia") # Path ruta relativa
print(guia)

guia2 = Path(base, "Barcelona","Sagrada_familia") # base + ruta relativa
print(guia2)

guia3 = Path(base, "Barcelona","Sagrada_familia", Path ("Barcelona2","Sagrada_familia2"))
print(guia3) # base + ruta relativa + otro Path

guia4 = Path(base, "Barcelona","Sagrada_familia", Path ("Barcelona2","Sagrada_familia2.txt"))
print(guia4) # base + ruta relativa + otro Path
guia5 = guia4.with_name("Sagrada_nueva.txt")
print(guia5) # cambio del nombre final de guia 4
print(guia5.parent) # Directorio antecesor
print(guia5.parent.parent)

pruebas = Path(Path.home(),"Desktop","Python","Tema1","Tema 6")

for txt in Path(pruebas).glob("*.txt"):
    print(txt) # devuelve todos los txt

# Extraer relativas de Python1 y Tema 1
pruebas2 = Path("Desktop","Python","Tema1","Tema 6")
Python1 = pruebas2.relative_to(Path("Desktop","Python"))
Tema1 = pruebas2.relative_to(Path("Desktop","Python","Tema1"))
print(Python1)
print(Tema1)




import datetime

#horas
mi_hora = datetime.time(17, 35, 58, 1500)
print(type(mi_hora))

print(mi_hora.hour)
print(mi_hora)

#dias
mi_dia = datetime.date(2025, 10 ,17)
print(mi_dia.ctime())
print(mi_dia)
print(mi_dia.year)

print(mi_dia.today())

# cambiar mes de abril por noviembre

mi_fecha = datetime.datetime(2025, 4, 15, 22, 18, 16, 2500)
mi_fecha = mi_fecha.replace(month = 11)
print(mi_fecha)

# calculos con fecha dias del fallecimiento de una persona
from datetime import date
nacimiento = date(1993, 2, 3)
defuncion = date(2026, 2, 2)

vida = defuncion - nacimiento
print(vida.days)
print(int(vida.days/365)) # años

# calculo de cuanto tiempo esta despierta una persona
from datetime import datetime

depierta = datetime(2026, 2, 3, 7, 3)
duerme = datetime(2026, 2, 3, 23, 4)

vigilia = duerme - depierta
print(vigilia)
print(vigilia.seconds)

# obtener los minutos de la hora actual
from datetime import datetime

minutos = datetime.now().minute


import datetime

hoy = datetime.date.today()
fecha_nacimiento = datetime.date(2005, 7, 30)
dias_vida = (hoy - fecha_nacimiento).days

print(dias_vida)
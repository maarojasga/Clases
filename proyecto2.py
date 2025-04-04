import datetime

def calcular_edad(year, month, day):
    hoy = datetime.date.today()
    nacimiento = datetime.date(year, month, day)
    edad = hoy.year - nacimiento.year
    
    return edad

try:
    year = int(input("Año de nacimiento: "))
    month = int(input("Mes de nacimiento (1-12): "))
    day = int(input("Día de nacimiento: "))
    edad = calcular_edad(year, month, day)
    print(f"Tienes {edad} años.")
except ValueError:
    print("¡Por favor ingresa valores válidos!")
except Exception as e:
    print(f"Ocurrió un error: {e}")
    
    
    
# Crear una nueva función para calcular los días de vida, y permitir al usuario elegir si quiere calcular los días o la edad.
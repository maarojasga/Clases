import datetime

def calcular_edad(year, month, day):
    hoy = datetime.date.today()
    nacimiento = datetime.date(year, month, day)
    edad = hoy.year - nacimiento.year
    
    return edad
def calcular_dias_de_vida(year, month, day):
    hoy = datetime.date.today()
    nacimiento = datetime.date(year, month, day)
    dias = (hoy - nacimiento).days

    return dias
while True:
    opcion = input(" Elige una opcion (Calcular años de vida-a/Calcular dias de vida-d/Salir-s): ")
    if opcion.lower()== "a":
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
    elif opcion.lower()== "d":
        try:
            year = int(input("Año de nacimiento: "))
            month = int(input("Mes de nacimiento (1-12): "))
            day = int(input("Día de nacimiento: "))
            dias = calcular_dias_de_vida(year, month, day)
            print(f"Tienes {dias} dias de vida.")
        except ValueError:
            print("¡Por favor ingresa valores válidos!")
        except Exception as e:
            print(f"Ocurrió un error: {e}")
    else:
        print("Hasta pronto")
        break

    
# Crear una nueva función para calcular los días de vida, y permitir al usuario elegir si quiere calcular los días o la edad.
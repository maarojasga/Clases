try:
    numero = int(input("Ingresa un número: "))
    resultado = 10 / numero
    print("El resultado es:", resultado)
except ZeroDivisionError:
    print("¡No puedes dividir entre cero!")
except ValueError:
    print("¡Eso no es un número!")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")

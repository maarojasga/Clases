agenda = {}

def agregar_contacto(nombre, telefono):
    agenda[nombre] = telefono

def mostrar_agenda():
    for nombre, telefono in agenda.items():
        print(f"{nombre}: {telefono}")

def buscar_contacto(nombre):
    if nombre in agenda:
        print(f"{nombre}: {agenda[nombre]}")
    else:
        print("Nombre no encontrado")

def ver_agenda_completa(agenda):
    for nombre, telefono in agenda.items():
        print(f"{nombre}:{telefono}")
# Programa principal
while True:
    opcion = input(" Elige una opcion (agregar-a/buscar-b/mostrar-c/salir-d): ")
    if opcion.lower() == "a":
        nombre = input("Nombre del contacto: ")
        telefono = input("Teléfono: ")
        agregar_contacto(nombre, telefono)
    elif opcion.lower() == "b":
        nombre = input("Ingresa el nombre que quieras encontrar: ")
        buscar_contacto(nombre)
    elif opcion.lower() == "c":
        ver_agenda_completa(agenda)
    else:
        print("Hasta luego")
        break


#tarea añadir opcion mostrar agenda antes de salir 
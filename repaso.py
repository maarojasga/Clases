# Variables

nombre = "Alejandra"


# Tipos de variables

# string
nombre = "Alejandra"

# booleanos
es_estudiante = True

# Enteros (int)
edad = 13

# Decimales (float)
temperatura = 12.5



# Listas
frutas = ["pera", "manzana", "banana"]

# Acceder a un valor dentro de una lista
print(frutas[0])


# Condicionales

# if, elif, else

edad = 18
if edad >= 18:
    print("Mayor de edad")
    
elif edad > 13:
    print("Adolescente")
    
else:
    print("Niño")

# Ciclos
 
# For
cocina = ["plato", "vaso", "cuchara", "tenedor", "plato"]
contador_platos =  0
contador_tenedores =  0

for elemento in cocina:
    
    if elemento == "plato":
        print("soy un plato")
        contador_platos += 1
        
        
    elif elemento == "tenedor":
        print("soy un tenedor")
        contador_tenedores += 1
    
    
print(contador_platos)
print(contador_tenedores)


# Funciones

def diametro_circulo(r):
    return 2*r

print(diametro_circulo(4))


# Diccionarios 
persona = {
    "nombre": "Vale",
    "edad": 19,
    "carrera": "ingeniera"
}

# Acceder a un valor usando una llave
print(persona["nombre"])
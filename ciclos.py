# Ciclo for

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
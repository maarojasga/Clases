import requests 

def obtener_pokemon(nombre_de_pokemon):
    url =f"https://pokeapi.co/api/v2/pokemon/{nombre_de_pokemon.lower()}"
    respuesta = requests.get(url)
    if respuesta.status_code==200:
        datos = respuesta.json()
#     print(datos)
        nombre = datos["name"]
        print(nombre)
        tipo = datos["height"]
        print(tipo)
        id_pk = datos["id"]
        print(id_pk)
        order_pk = datos["order"]
        print(order_pk)
        weight_pk = datos["weight"]
        print(weight_pk)
        base_experience_pk = datos["base_experience"]
        print(base_experience_pk)
        location_area_encounters_pk = datos["location_area_encounters"]
        print(location_area_encounters_pk)
    return respuesta

print(obtener_pokemon("charmander"))
#tarea hacer la base de datos
#elegir traer id order weight base_experience location_area_encounters
# API DATA fetching using python

import requests

base_url = "https://pokeapi.co/api/v2/"

def get_info_pokemon(name):
    url = f"{base_url}/pokemon/{name}"

    request1 = requests.get(url)

    if request1.status_code == 200 :
        pokemon_data = request1.json()
        return pokemon_data
    else:
        print("data not retrieved")


pokemonName = input("enter the name of pokemon u want the data :")

result = get_info_pokemon(pokemonName)

print(result["name"])
print(result["id"])
print(result["weight"])
print(result["height"])



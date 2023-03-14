"""Termdex displays information about pokemon"""
import json

import requests


def show_pokemon(pokemon_id):
    """Read pokemon sprites from json file"""
    with open("pokemon.json", encoding="utf-8") as pokemon_data:
        data = json.load(pokemon_data)
    print(data[str(pokemon_id)])


def search_pokemon(pokemon_id):
    """Search for information regarding pokemon"""
    res = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")
    body = res.json()
    pokemon_types = []
    for ptype in body["types"]:
        pokemon_types.append(ptype["type"]["name"])
    show_pokemon(pokemon_id)
    print(body["name"])


def main():
    """Run Termdex app"""
    print("Welcome to TermDex")
    print("Input a pokemon ID")
    pokemon_id = input()
    pokemon_id = int(pokemon_id)
    search_pokemon(pokemon_id)


if __name__ == "__main__":
    main()

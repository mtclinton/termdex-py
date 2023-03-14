"""Termdex displays information about pokemon"""
import json

import requests


def show_sprite(sprite, ptype):
    """Show the pokemon sprite in color"""
    poke_colors = {
        "normal": (168, 167, 122),
        "fire": (238, 129, 48),
        "water": (99, 144, 240),
        "electric": (247, 208, 44),
        "grass": (122, 199, 76),
        "ice": (150, 217, 214),
        "fighting": (194, 46, 40),
        "poison": (163, 62, 161),
        "ground": (226, 191, 101),
        "flying": (169, 143, 243),
        "psychic": (249, 85, 135),
        "bug": (166, 185, 26),
        "rock": (182, 161, 54),
        "ghost": (115, 87, 151),
        "dragon": (111, 53, 252),
        "dark": (112, 87, 70),
        "steel": (183, 183, 206),
        "fairy": (214, 133, 173),
    }
    r, g, b = poke_colors[ptype]
    print(f"\x1b[38;2;{r};{g};{b}m" + sprite + "\x1b[0m")


def show_pokemon(pokemon_id):
    """Read pokemon sprites from json file"""
    with open("pokemon.json", encoding="utf-8") as pokemon_data:
        data = json.load(pokemon_data)
    return data[str(pokemon_id)]


def search_pokemon(pokemon_id):
    """Search for information regarding pokemon"""
    res = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")
    body = res.json()
    pokemon_types = []
    for ptype in body["types"]:
        pokemon_types.append(ptype["type"]["name"])
    show_sprite(show_pokemon(pokemon_id), pokemon_types[0])
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

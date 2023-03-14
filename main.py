"""Termdex displays information about pokemon"""
import requests


def search_pokemon(pokemon_id):
    """Search for information regarding pokemon"""
    res = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")
    body = res.json()
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

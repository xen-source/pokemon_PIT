import json
import random
import os
import time

# MAIN MENU

def menu():
    print("---[POKEMON]---\n")
    print("1. Start game.")
    print("2. View pokemons.")
    print("3. Exit\n")

    try:
        user_choice = int(input("Go to(1-4): "))

        if user_choice == 1:
            battle()
        elif user_choice == 2:
            os.system("cls" if os.name == "nt" else "clear")
            view_pokemons()
        else:
            print("Exiting...\n")
    except ValueError:
        print("Invalid input! Please enter a number.")
        menu()
    finally:
        print("Thank you for playing pokemon!")

def battle():
    turn = []

    try:
        with open("pokemon_team.json", "r") as f:
            pokemon_team = json.load(f)

            turn.append(pokemon_team[0]["name"])

        with open("enemy_team.json", "r") as f:
            enemy_team = json.load(f)

        my_pkmn = pokemon_team[0]
        enemy_pkmn = enemy_team[1]
        turn = [my_pkmn, enemy_pkmn]

        while my_pkmn["hp"] > 0 and enemy_pkmn["hp"] > 0:
            os.system("cls" if os.name == "nt" else "clear")

            attacker = turn.pop(0)

            if my_pkmn["hp"] > 89:
                my_bar = "■■■■■■■■■■■■■"
            elif my_pkmn["hp"] > 69:
                my_bar = "■■■■■■■■■■"
            elif my_pkmn["hp"] > 49:
                my_bar = "■■■■■■■"
            elif my_pkmn["hp"] > 29:
                my_bar = "■■■■"
            elif my_pkmn["hp"] > 9:
                my_bar = "■"
            else:
                my_bar = ""

            if enemy_pkmn["hp"] > 89:
                enemy_bar = "■■■■■■■■■■■■■"
            elif enemy_pkmn["hp"] > 69:
                enemy_bar = "■■■■■■■■■■"
            elif enemy_pkmn["hp"] > 49:
                enemy_bar = "■■■■■■■"
            elif enemy_pkmn["hp"] > 29:
                enemy_bar = "■■■■"
            elif enemy_pkmn["hp"] > 9:
                enemy_bar = "■"
            else:
                enemy_bar = ""
            
            print("                    ---[POKEMON BATTLE]---\n") 

            print(f"\n                                 {enemy_pkmn['name']}[{enemy_bar}]\n")
            print(f"{my_pkmn['name']}[{my_bar}]")

            if attacker == my_pkmn:
                target = enemy_pkmn  

                print(f"1. {my_pkmn['moves'][0]['name']}    2. {my_pkmn['moves'][1]['name']}    3. Heal")
                
                while True:
                    try:
                        user_choice = int(input("Choose[1-3]: "))
                    except ValueError:
                        print("Error! Try again.")
                        time.sleep(0.6)
                    else:
                        break
                    os.system("cls" if os.name == "nt" else "clear")
                    print(f"\n                                 {enemy_pkmn['name']}[{enemy_bar}]\n")
                    print(f"{my_pkmn['name']}[{my_bar}]")
                    print(f"1. {my_pkmn['moves'][0]['name']}    2. {my_pkmn['moves'][1]['name']}    3. Heal")

                if user_choice == 1:
                    attack = my_pkmn["moves"][0]["damage"]
                    print(f"\n{target['name']} took {attack} damage!")
                    time.sleep(0.6)
                elif user_choice == 2:
                    attack = my_pkmn["moves"][1]["damage"]
                    print(f"\n{target['name']} took {attack} damage!")
                    time.sleep(0.6)

                elif user_choice == 3:
                    heal = random.randint(6,10)
                    attack = 0
                    my_pkmn["hp"] += heal
                    print(f"\n{attacker['name']} took {heal} heal!")
                    time.sleep(0.6)
                else:
                    print("Invalid choice, missing your turn!")
                    attack = 0

            else:
                target = my_pkmn
                num = random.randint(1,2)

                if enemy_pkmn["hp"] < 30:
                    heal = random.randint(7,12)
                    attack = 0
                    enemy_pkmn["hp"] += heal
                    print(f"\n{attacker['name']} took {heal} heal!")
                    time.sleep(0.6)
                elif num == 1:
                    attack = enemy_pkmn["moves"][0]["damage"]
                    print(f"\n{target['name']} took {attack} damage!")
                    time.sleep(0.6)
                elif num == 2:
                    attack = enemy_pkmn["moves"][1]["damage"]
                    print(f"\n{target['name']} took {attack} damage!")
                    time.sleep(0.6)

            target["hp"] -= attack

            turn.append(attacker)

        if my_pkmn["hp"] <= 0:
            print(f"\n{enemy_pkmn['name']} won!")
            back = int(input("Back to menu[y/n]: "))
            if back.lower() == 'y':
                os.system("cls" if os.name == "nt" else "clear")
                menu()
            else:
                return
        else:
            print(f"\n{my_pkmn['name']} won!")
            back = input("Back to menu[y/n]: ")
            if back.lower() == 'y':
                os.system("cls" if os.name == "nt" else "clear")
                menu()
            else:
                return 0

    except FileNotFoundError as e:
        print(f"FILE ERROR: I couldn't find the file: {e.filename}")

    except Exception as e:
        print(f"SYSTEM ERROR: {e}")
# SEARCH FUNCTION

def search(pokemons):

    while True:
        print("---[POKEMON SEARCH]---\n")
        try:
            user_input = input("Enter pokemon name: ").strip().lower()
        except ValueError:
            print("Error! Try again.")
            time.sleep(0.6)

        with open("pokemon_team.json", "r") as f:
            pokedex = json.load(f)

        for pokemon in pokedex:
            if pokemon["name"].lower() == user_input:
                print(f"\nName: {pokemon['name']}")
                print(f"Hp: {pokemon['hp']}")
                print("Moves:")
                print(f"    Move 1: {pokemon['moves'][0]['name']}")
                print(f"    Damage: {pokemon['moves'][0]['damage']}")
                print(f"    Move 2: {pokemon['moves'][1]['name']}")
                print(f"    Damage: {pokemon['moves'][1]['damage']}")
                
                back = input("Back to view pokemons[y/n]: ")
                if back.lower() == 'y':
                    os.system("cls" if os.name == "nt" else "clear")
                    view_pokemons()
                else:
                    return 0
            elif pokemon["name"].lower() != user_input:
                print("Pokemon is not in your pokedex!")
                back = input("Back to view pokemons[y/n]: ")
                if back.lower() == 'y':
                    os.system("cls" if os.name == "nt" else "clear")
                    view_pokemons()
                else:
                    return 0

# VIEWING POKEMON DECK

def view_pokemons():
    print("---[POKEMONS]---\n")
    with open("pokemons.txt", "r") as f:
        pokemons = f.read()
        print(pokemons)
    print("\n1. Search pokemon.")
    print("2. Back to menu.")
    print("3. Exit.")

    user_choice = int(input("Go to(1-3): "))

    if user_choice == 1:
        os.system("cls" if os.name == "nt" else "clear")
        search(pokemons)
    elif user_choice == 2:
        os.system("cls" if os.name == "nt" else "clear")
        menu()
    else: 
        return 0

menu()
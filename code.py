def menu():
    print("---[POKEMON]---\n")
    print("1. Start game.")
    print("2. View pokemons.")
    print("3. Shop")
    print("4. Exit\n")
    
    try:
        user_choice = int(input("Go to(1-4): "))

        if user_choice == 1:
            pass
        elif user_choice == 2:
            view_pokemons()
        elif user_choice == 3:
            pass
        else:
            print("Exiting...\n")
    except:
        pass
    finally:
        print("Thank you for playing pokemon!")

def search(pokemons):
    pokemon = input("Enter pokemon name: ")
    if pokemon in pokemons:
        print("found")
    else:
        print("not found")

def view_pokemons():
    print("---[POKEMONS]---\n")
    with open("pokemons.txt", "r") as f:
        pokemons = f.read()
        print(pokemons)
    print("1. Search pokemon.")
    print("2. Back to menu.")
    print("3. Exit.")

    user_choice = int(input("Go to(1-3): "))

    if user_choice == 1:
        search(pokemons)
    elif user_choice == 2:
        menu()
    else:
        pass

menu()
def menu():
    print("---[POKEMON]---\n")
    print("1. Start game.")
    print("2. View pokemons.")
    print("3. Shop")
    print("4. Exit\n")
    user_choice = int(input("Go to(1-4): "))
    return user_choice

def view_pokemons():
    with open("pokemons.txt", "w") as f:
        pokemons = f.read()
        print(pokemons)

user_choice = menu()

try:
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

import sys
import os

# Adds the parent directory to sys.path to allow imports from other directories
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import functions from each module
from CREATE.create import create_custom_table
from INSERT.insert import add_pokemon
from READ.read import listar_pokedex, buscar_pokemon
from UPDATE.update import atualizar_pokemon
from DELETE.delete import remove_pokemon
from DELETE.drop import remove_table
from READ.tabela import listar_tabelas
from INNERJOIN.inner import unir_tabelas

# Main menu function
def menu():
    while True:
        print("\n📌 POKEDEX MENU")
        print("1️ - Create a new Pokédex")
        print("2️ - Delete a Pokédex")
        print("3️ - Add a Pokémon")
        print("4️ - List all Pokémon in the Pokédex")
        print("5️ - Search for a Pokémon by name")
        print("6️ - Update Pokémon information")
        print("7️ - Remove a Pokémon")
        print("8️ - List all Pokédexes")
        print("9️ - Merge Pokédexes")
        print("0️ - Exit")
        
        # User input for menu selection
        choice = input("Choose an option: ")
        
        if choice == "1":
            create_custom_table()  # Create a new custom Pokédex table
        elif choice == "2":
            remove_table()  # Remove a Pokédex table
        elif choice == "3":
            add_pokemon()  # Add a new Pokémon to the Pokédex
        elif choice == "4":
            listar_pokedex()  # List all Pokémon in the Pokédex
        elif choice == "5":   
            table_name = input("Enter the name of the table you want to list: ") 
            pokemon_id = input("Enter the Pokémon ID you want to search for: ")
            buscar_pokemon(table_name, pokemon_id)  # Search for a Pokémon by ID
        elif choice == "6":
            name = input("Enter the name of the Pokémon you want to update: ")
            new_type = input("Enter the new type: ")
            atualizar_pokemon(name, new_type)  # Update the Pokémon information
        elif choice == "7":
            remove_pokemon()  # Remove a Pokémon from the Pokédex
        elif choice == "8":
            listar_tabelas()  # List all available Pokédex tables
        elif choice == "9":
            unir_tabelas()  # Merge multiple Pokédex tables
        elif choice == "0":
            print("Exiting the Pokédex...")
            break  # Exit the program
        else:
            print("Invalid option! Please try again.")

# Run the menu if the script is executed directly
if __name__ == "__main__":
    menu()

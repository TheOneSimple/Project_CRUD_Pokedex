import sqlite3

# Function to check if a table exists in the database
def verificar_tabela_existente(nome_tabela):
    conn = sqlite3.connect("data/pokedex.db")  # Connect to the SQLite database
    cursor = conn.cursor()  # Create a cursor object to interact with the database
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (nome_tabela,))  # Query to check if table exists
    tabela = cursor.fetchone()  # Fetch the result of the query
    conn.close()  # Close the connection to the database
    return tabela is not None  # Return True if the table exists, False otherwise

# Function to list all Pokémon in a specified table from the Pokedex
def listar_pokedex():
    nome_tabela = input("Enter the name of the table you want to list: ")

    # Check if the table exists in the Pokedex database
    if not verificar_tabela_existente(nome_tabela):
        print(f"❌ The table '{nome_tabela}' does not exist. Please try again.")
        return  # Exit the function if the table doesn't exist
    
    conn = sqlite3.connect("data/pokedex.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {nome_tabela}")  # Query to get all Pokémon from the table
    pokemons = cursor.fetchall()  # Fetch all results
    conn.close()  # Close the connection to the database
    
    # If there are Pokémon, print them; otherwise, notify that the Pokedex is empty
    if pokemons:
        print("\n📖 POKEDEX:")
        for p in pokemons:
            print(f"ID: {p[0]} | Name: {p[1]} | Type: {p[2]}")
    else:
        print("Pokédex is empty!")

# Function to search for a specific Pokémon by ID in a specified table
def buscar_pokemon(nome_tabela, id):
    
    # Check if the table exists in the Pokedex database
    if not verificar_tabela_existente(nome_tabela):
        print(f"❌ The table '{nome_tabela}' does not exist. Please try again.")
        return  # Exit the function if the table doesn't exist
    
    conn = sqlite3.connect("data/pokedex.db")
    cursor = conn.cursor()
    # Modifying the query to search by ID
    cursor.execute(f"SELECT * FROM {nome_tabela} WHERE id=?", (id,))
    pokemon = cursor.fetchone()  # Fetch the result of the query
    conn.close()  # Close the connection to the database

    # If the Pokémon is found, print its details; otherwise, notify that the Pokémon was not found
    if pokemon:
        print(f"🔍 Pokémon found: ID: {pokemon[0]} | Name: {pokemon[1]} | Type: {pokemon[2]}")
    else:
        print("❌ Pokémon not found!")

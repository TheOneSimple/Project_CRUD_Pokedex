import sqlite3

# Function to check if a table exists in the database
def verificar_tabela_existente(nome_tabela):
    conn = sqlite3.connect("data/pokedex.db")  # Connect to the SQLite database
    cursor = conn.cursor()  # Create a cursor object to interact with the database
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (nome_tabela,))  # Query to check if the table exists
    tabela = cursor.fetchone()  # Fetch the result of the query
    conn.close()  # Close the connection to the database
    return tabela is not None  # Return True if the table exists, False otherwise

# Function to update Pokémon details (name, type, or both)
def atualizar_pokemon():
    nome_tabela = input("Enter the table name: ")

    # Check if the table exists
    if not verificar_tabela_existente(nome_tabela):
        print(f"❌ The table '{nome_tabela}' does not exist. Please try again.")
        return
    
    # Ask for the Pokémon's ID
    id_pokemon = input("Enter the ID of the Pokémon you want to update: ")

    # Ask the user if they want to change the name, type, or both
    print("\nWhat would you like to update?")
    print("1 - Name")
    print("2 - Type")
    print("3 - Name and Type")
    escolha = input("Choose an option: ")

    conn = sqlite3.connect("data/pokedex.db")  # Connect to the database
    cursor = conn.cursor()  # Create a cursor object to interact with the database

    # Depending on the user's choice, update the corresponding fields
    if escolha == "1":
        novo_nome = input("Enter the new name: ")
        cursor.execute(f"UPDATE {nome_tabela} SET nome=? WHERE id=?", (novo_nome, id_pokemon))  # Update the name
        print(f" The name of the Pokémon with ID {id_pokemon} has been changed to {novo_nome}!")
    
    elif escolha == "2":
        novo_tipo = input("Enter the new type: ")
        cursor.execute(f"UPDATE {nome_tabela} SET tipo=? WHERE id=?", (novo_tipo, id_pokemon))  # Update the type
        print(f" The Pokémon with ID {id_pokemon} is now of type {novo_tipo}!")
    
    elif escolha == "3":
        novo_nome = input("Enter the new name: ")
        novo_tipo = input("Enter the new type: ")
        cursor.execute(f"UPDATE {nome_tabela} SET nome=?, tipo=? WHERE id=?", (novo_nome, novo_tipo, id_pokemon))  # Update both name and type
        print(f" The Pokémon with ID {id_pokemon} now has the name {novo_nome} and type {novo_tipo}!")

    else:
        print("❌ Invalid option!")
        conn.close()  # Close the connection if an invalid option was chosen
        return

    conn.commit()  # Commit the changes to the database
    conn.close()  # Close the connection to the database

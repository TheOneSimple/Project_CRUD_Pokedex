import sqlite3

# Function to check if a table exists in the database
def verificar_tabela_existente(nome_tabela):
    conn = sqlite3.connect("data/pokedex.db")  # Connect to the SQLite database
    cursor = conn.cursor()  # Create a cursor object to interact with the database
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (nome_tabela,))  # Query to check if table exists
    tabela = cursor.fetchone()  # Fetch the result of the query
    conn.close()  # Close the connection to the database
    return tabela is not None  # Return True if the table exists, False otherwise

# Function to list all tables in the database
def listar_tabelas():
    # Connect to the database
    conn = sqlite3.connect("data/pokedex.db")
    cursor = conn.cursor()

    # Query to get all tables from the database
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tabelas = cursor.fetchall()  # Fetch all results
    conn.close()  # Close the connection to the database

    # Check if there are any tables in the database
    if tabelas:
        print("\n📜 Existing tables in the database:")
        for tabela in tabelas:
            print(f"- {tabela[0]}")
    else:
        print("❌ No tables found in the database!")

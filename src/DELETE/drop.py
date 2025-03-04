import sqlite3  # Importing the SQLite3 library

# Function to check if the table exists
def verificar_tabela_existente(nome_tabela):
    conn = sqlite3.connect("data/pokedex.db")  # Connecting to the database
    cursor = conn.cursor()
    
    # Query to check if the table exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (nome_tabela,))
    tabela = cursor.fetchone()
    
    conn.close()  # Closing the connection
    return tabela is not None  # Returns True if the table exists, False otherwise

def remove_table():
    # Asking the user for the table name to remove
    table_name = input("Enter the name of the table you want to remove: ")

    # Checking if the table exists
    if not verificar_tabela_existente(table_name):
        print(f"❌ The table '{table_name}' does not exist. Please try again.")  # Error message if the table doesn't exist
        return
    
    # Connecting to the database to remove the table
    conn = sqlite3.connect("data/pokedex.db")
    cursor = conn.cursor()
    
    # Dropping the table if it exists
    cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
    conn.commit()  # Committing the changes
    conn.close()  # Closing the connection
    
    print(f"🗑️ Table '{table_name}' has been successfully removed!")  # Success message

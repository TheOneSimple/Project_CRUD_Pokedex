import sqlite3  # Importing the SQLite3 library

# Function to check if the table exists
def check_table_exists(table_name):
    conn = sqlite3.connect("data/pokedex.db")  # Connecting to the database
    cursor = conn.cursor()
    
    # Query to check if the table exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
    table = cursor.fetchone()
    
    conn.close()  # Closing the connection
    return table is not None  # Returns True if the table exists, False otherwise

def remove_pokemon():
    # Asking the user for the table name
    table_name = input("Enter the table name: ")

    # Checking if the table exists
    if not check_table_exists(table_name):
        print(f"❌ The table '{table_name}' does not exist. Please try again.")  # Error message if table doesn't exist
        return
    
    id = input("Enter the ID of the Pokémon you want to remove: ")  # Asking for the Pokémon ID

    # Checking if the ID is a valid number
    if not id.isdigit():
        print("⚠️ Invalid ID! Please make sure to enter a number.")  # Warning message for invalid input
        return
    
    id = int(id)  # Converting the ID to an integer
    
    # Connecting to the database and checking if the Pokémon exists
    conn = sqlite3.connect("data/pokedex.db")
    cursor = conn.cursor()
    
    # Query to find the Pokémon by ID
    cursor.execute(f"SELECT * FROM {table_name} WHERE id=?", (id,))
    pokemon = cursor.fetchone()
    
    # If the Pokémon does not exist, show an error message and exit
    if pokemon is None:
        print(f"❌ Pokémon with ID {id} not found in the table '{table_name}'.")
        conn.close()
        return
    
    # If the Pokémon exists, proceed with deletion
    cursor.execute(f"DELETE FROM {table_name} WHERE id=?", (id,))
    conn.commit()  # Committing the changes
    conn.close()  # Closing the connection
    
    print(f"🗑️ Pokémon with ID {id} has been removed from the table '{table_name}'!")  # Success message

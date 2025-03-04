import sqlite3

# Function to check if a table exists in a specific database
def check_table_exists(table_name, db):
    conn = sqlite3.connect(db)  # Connect to the SQLite database
    cursor = conn.cursor()  # Create a cursor object to interact with the database
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))  # Query to check if table exists
    table = cursor.fetchone()  # Fetch the result of the query
    conn.close()  # Close the connection to the database
    return table is not None  # Return True if the table exists, False otherwise

# Function to manually remove accents from a string
def remove_accents(text):
    # Dictionary mapping accented characters to their non-accented equivalents
    mapping = {
        'á': 'a', 'à': 'a', 'â': 'a', 'ã': 'a', 'ä': 'a',
        'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e',
        'í': 'i', 'ì': 'i', 'î': 'i', 'ï': 'i',
        'ó': 'o', 'ò': 'o', 'ô': 'o', 'õ': 'o', 'ö': 'o',
        'ú': 'u', 'ù': 'u', 'û': 'u', 'ü': 'u',
        'ç': 'c'
    }
    # Iterate over each character in the text and replace it with its non-accented counterpart, if it exists
    return ''.join(mapping.get(c, c) for c in text)

# List of all valid Pokémon types (in lowercase and without accents)
VALID_TYPES = [
    "normal", "fire", "water", "electric", "grass", "ice", "fighting", "poison",
    "ground", "flying", "psychic", "bug", "rock", "ghost", "dragon",
    "dark", "steel", "fairy"
]

# Function to add a Pokémon to the Pokedex
def add_pokemon():
    # Prompt the user to enter the name of the table where the Pokémon will be added
    table_name = input("Enter the name of the table where you want to add the Pokémon: ")

    # Check if the table exists in the Pokémon database
    if not check_table_exists(table_name, "data/pokedex.db"):
        print(f"❌ The table '{table_name}' does not exist. Please try again.")
        return  # Exit the function if the table does not exist
    
    # Prompt the user to enter the Pokémon's details
    name = input("Pokémon name: ")
    type_ = input("Pokémon type: ")
    
    # Remove accents from the Pokémon type and convert it to lowercase
    normalized_type = remove_accents(type_.lower())
    
    # Check if the provided type is valid
    if normalized_type not in VALID_TYPES:
        print(f"❌ Invalid type '{type_}'! Choose one of the following: {', '.join(VALID_TYPES)}")
        return  # Exit the function if the type is invalid
    
    # Format the type to capitalize the first letter
    formatted_type = normalized_type.capitalize()
    
    # Connect to the Pokémon database and add the Pokémon to the table
    conn = sqlite3.connect("data/pokedex.db")
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO {table_name} (name, type) VALUES (?, ?)", (name, formatted_type))
    conn.commit()  # Commit the changes to the database
    conn.close()  # Close the connection to the database
    
    # Notify the user that the Pokémon was successfully added
    print(f"✅ Pokémon '{name}' successfully added to the table '{table_name}'!")

# Function to add a Trainer to the Trainers table
def add_trainer():
    # Prompt the user to enter the name of the table where the Trainer will be added
    table_name = input("Enter the name of the table where you want to add the Trainer: ")

    # Check if the table exists in the Trainer database
    if not check_table_exists(table_name, "data/trainers.db"):
        print(f"❌ The table '{table_name}' does not exist. Please try again.")
        return  # Exit the function if the table does not exist
    
    # Prompt the user to enter the Trainer's details
    name = input("Trainer name: ")
    age = input("Trainer age: ")
    city = input("Trainer's city of origin: ")
    
    # Connect to the Trainer database and add the Trainer to the table
    conn = sqlite3.connect("data/trainers.db")
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO {table_name} (name, age, city) VALUES (?, ?, ?)", (name, age, city))
    conn.commit()  # Commit the changes to the database
    conn.close()  # Close the connection to the database
    
    # Notify the user that the Trainer was successfully added
    print(f"✅ Trainer '{name}' successfully added to the table '{table_name}'!")

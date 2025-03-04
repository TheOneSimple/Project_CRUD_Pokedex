import sqlite3  # Importing the SQLite3 library

def create_custom_table():
    # Asking the user for the name of the new table
    table_name = input("Enter the name of the new table: ")

    # Connecting to the SQLite database (or creating it if it doesn't exist)
    conn = sqlite3.connect("data/pokedex.db")
    cursor = conn.cursor()

    # Creating the table if it does not already exist
    try:
        cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,  # Auto-incrementing primary key
                name TEXT UNIQUE NOT NULL,  # Unique and non-null name field
                type TEXT NOT NULL  # Non-null type field
            )
        """)
        conn.commit()  # Committing the changes
        print(f"✅ Table '{table_name}' created successfully!")  # Success message
    except sqlite3.Error as e:
        print(f"❌ Error creating the table: {e}")  # Error handling in case of an issue
    finally:
        conn.close()  # Closing the database connection

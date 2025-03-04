import sqlite3

def verificar_tabela_existente(nome_tabela):
    """Checks if the table exists in the database"""
    conn = sqlite3.connect("data/pokedex.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (nome_tabela,))
    tabela = cursor.fetchone()  # Fetch the result of the query
    conn.close()  # Close the connection to the database
    return tabela is not None  # Return True if the table exists, False otherwise

def unir_tabelas():
    """Allows the user to choose two tables and combine their data"""
    
    # Ask for the table names
    tabela1 = input("Enter the name of the first table: ")
    tabela2 = input("Enter the name of the second table: ")

    # Check if both tables exist
    if not verificar_tabela_existente(tabela1):
        print(f"❌ The table '{tabela1}' does not exist. Please try again.")
        return
    
    if not verificar_tabela_existente(tabela2):
        print(f"❌ The table '{tabela2}' does not exist. Please try again.")
        return
    
    # Connect to the database and perform the UNION query
    conn = sqlite3.connect("data/pokedex.db")
    cursor = conn.cursor()
    
    try:
        query = f"""
        SELECT * FROM {tabela1}
        UNION ALL
        SELECT * FROM {tabela2}
        """  # Combine the data from both tables
        cursor.execute(query)
        resultados = cursor.fetchall()  # Fetch all the results
        
        # Display the results
        if resultados:
            print("\n📊 RESULTS OF THE TABLE UNION:")
            for linha in resultados:
                print(linha)
        else:
            print("📭 No results found in the union of the tables.")

    except sqlite3.Error as e:
        print(f"❌ Error while merging the tables: {e}")

    conn.close()  # Close the connection to the database

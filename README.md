## Introduction

This project is an application for managing Pokémon-related information, in a virtual version inspired by the POKÉDEX. Users can choose the table name to store the data.

## Project Structure

- **POKÉDEX/**
  - Main project directory

### Subdirectories and Files

#### 1. **src/**
Contains the project's source code, divided by functionality:

- **app/**
  - Main entry point of the application.
  - Script responsible for merging data from two tables.

- **CREATE/**
  - Scripts responsible for creating new database records.
    - Creating custom tables.

- **READ/**
  - Scripts responsible for reading database data.
    - Reading Pokémon data.
    - Listing existing tables.

- **UPDATE/**
  - Scripts responsible for updating existing records.
    - Updating Pokémon data.

- **DELETE/**
  - Scripts responsible for deleting records.
    - Deleting Pokémon data.
    - Deleting tables.

- **INSERT/**
  - Scripts responsible for inserting new records into the database.
    - Inserting Pokémon and Trainer data.

- **utils.py**
  - Utility functions used throughout the project.

#### 2. **data/**
Contains the SQLite database:
- Main database.

#### 3. **README.md**
This file describes the project structure and provides general information.

## Technologies Used

- **Python**: Main programming language of the project.
- **SQLite**: Database used.
- **Modular Structure**: Code organized by modules and functionalities.

## How to Use

1. Make sure you have Python installed on your machine.
2. Navigate to the `src/app/` directory and run the `main.py` file:

   ```bash
   python main.py

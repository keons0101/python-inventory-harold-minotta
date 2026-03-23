# Python Inventory Management - Harold Minotta

A simple command-line inventory management system for products, supporting both perishable and non-perishable items. Allows adding, viewing, updating, removing, and saving products to a file.

## How to Run

1. Make sure you have Python 3 installed.
2. Open a terminal in this project folder.
3. Run the program with:

	python harold_coursework1.py

## Features Implemented

- Add new products (perishable and non-perishable)
- View current inventory
- Update product details (including expiration date for perishables)
- Remove products from inventory
- Save inventory to a text file (`inventory.txt`)
- Simple menu-driven interface

## Limitations / Known Issues

- No persistent loading: Inventory is not loaded from file on startup, only saved.
- No input validation for incorrect data types (e.g., entering text where a number is expected may cause errors).
- Expiration date is not validated for format or logic.
- Only supports running in a terminal/console (no GUI).
inventory = {
    101: {
        "name": "Laptop",
        "category": "Electronics",
        "brand": ("Dell",),
        "quantity": 5,
        "price": 799.99
    },
    102: {
        "name": "Mouse",
        "category": "Electronics",
        "brand": ("Logitech",),
        "quantity": 10,
        "price": 25.50
    },
    103: {
        "name": "Keyboard",
        "category": "Office",
        "brand": ("HP",),
        "quantity": 8,
        "price": 20.15
    }
}

categories = ["Electronics", "Home", "Office"]
product_ids = set(inventory.keys())

# ===========================================================================================================

def add_product(inventory, product_ids, categories):
    print("Available categories:", ", ".join(categories))
    
    new_id = int(input("Enter product ID: "))
    
    if new_id in product_ids:
        print("This ID already exists. Try another one.")
        return 
    
    new_name = input("Enter product name: ").strip().capitalize()
    new_category = input("Enter category: ").strip().capitalize()
    new_brand = input("Enter brand name: ").strip().capitalize()
    new_quantity = int(input("Enter quantity: "))
    new_price = float(input("Enter product price: "))

    inventory[new_id] = {
        "name": new_name,
        "category": new_category,
        "brand": (new_brand,),
        "quantity": new_quantity,
        "price": new_price
    }

    product_ids.add(new_id)

    print("Item added successfully!!!")
    print(f"ID: {new_id} | Name: {new_name} | Category: {new_category} | Brand: {new_brand} | Quantity: {new_quantity} | Price: ${new_price:.2f}")

# ===========================================================================================================

def show_inventory(inventory):
    print("-------------------------------------------------------------------------------------------")
    for product_id, product_data in inventory.items():
        print(f"ID: {product_id} | Name: {product_data['name']} | "
            f"Category: {product_data['category']} | "
            f"Brand: {product_data['brand'][0]} | "
            f"Quantity: {product_data['quantity']} | "
            f"Price: ${product_data['price']:.2f}")

# ===========================================================================================================

def update_product(inventory):
    product_id = int(input("Enter product ID to update: "))
    
    if product_id not in inventory:
        print("Product not found.")
        return

    print("Leave blank if you don't want to change something.")

    new_name = input("New name: ")
    new_quantity = input("New quantity: ")
    new_price = input("New price: ")

    if new_name != "":
        inventory[product_id]["name"] = new_name.capitalize()

    if new_quantity != "":
        inventory[product_id]["quantity"] = int(new_quantity)

    if new_price != "":
        inventory[product_id]["price"] = float(new_price)

# ===========================================================================================================

menuRunning = True

while menuRunning:
    print("\n--- MENU ---")
    print("1. Add product")
    print("2. View inventory")
    print("3. Exit")

    option = input("Choose an option: ")

    if option == "1":
        add_product(inventory, product_ids, categories)

    elif option == "2":
        show_inventory(inventory)

    elif option == "3":
        update_product(inventory)

    elif option == "4":
        print("Exiting...")
        menuRunning = False

    else:
        print("Invalid option")
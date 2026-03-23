class Product:
    def __init__(self, name, category, brand, quantity, price):
        self.name = name
        self.category = category
        self.brand = brand 
        self.quantity = quantity
        self.price = price

    def display(self):
        return f"{self.name} | {self.category} | {self.brand} | {self.quantity} | ${self.price:.2f}"

    def update(self, name="", quantity="", price=""):
        if name != "":
            self.name = name.capitalize()
        if quantity != "":
            self.quantity = int(quantity)
        if price != "":
            self.price = float(price)

inventory = {
    101: Product("Laptop", "Electronics", "Dell", 5, 799.99),
    102: Product("Mouse", "Electronics", "Logitech", 10, 25.50),
    103: Product("Keyboard", "Office", "HP", 8, 20.15)
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

    inventory[new_id] = Product(new_name, new_category, new_brand, new_quantity, new_price)

    product_ids.add(new_id)

    print("Item added successfully!!!")
    print(f"ID: {new_id} | Name: {new_name} | Category: {new_category} | Brand: {new_brand} | Quantity: {new_quantity} | Price: ${new_price:.2f}")

# ===========================================================================================================

def show_inventory(inventory):
    print("-------------------------------------------------------------------------------------------")
    for product_id, product_data in inventory.items():
        print(f"ID: {product_id} | {product_data.display()}")

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

    inventory[product_id].update(new_name, new_quantity, new_price)

    print("Product updated successfully!")

# ===========================================================================================================

def remove_product(inventory, product_ids):
    product_id = int(input("Enter product ID to remove: "))

    if product_id not in inventory:
        print("Product not found!!!")
        return

    del inventory[product_id]
    product_ids.remove(product_id)

    print("Product removed successfully!!!")

# ===========================================================================================================

def save_inventory_to_file(inventory):
    file = open("inventory.txt", "w")
    for product_id, product_data in inventory.items():
        line = f"{product_id},{product_data.name},{product_data.category},{product_data.brand},{product_data.quantity},{product_data.price}\n"
        file.write(line)
    file.close()
    print("Inventory saved to file!")

# ===========================================================================================================

menuRunning = True

while menuRunning:
    print("1. Add product")
    print("2. View inventory")
    print("3. Update product")
    print("4. Remove product")
    print("5. Save inventory to file")
    print("6. Exit")

    option = input("Choose an option: ")

    if option == "1":
        add_product(inventory, product_ids, categories)

    elif option == "2":
        show_inventory(inventory)

    elif option == "3":
        update_product(inventory)

    elif option == "4":
        remove_product(inventory, product_ids)

    elif option == "5":
        save_inventory_to_file(inventory)

    elif option == "6":
        print("Exiting...")
        menuRunning = False

    else:
        print("Invalid option")
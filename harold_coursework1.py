inventory = {
    101: {
        "name": "Laptop",
        "quantity": 5,
        "price": 799.99
    },
    102: {
        "name": "Mouse",
        "quantity": 10,
        "price": 25.50
    },
    103: {
        "name": "Keyboard",
        "quantity": 8,
        "price": 20.15
    }
}
print("Welcome to Bigstore----------------------------------------")

new_id = int(input("Enter product ID: "))
new_name = input("Enter product name: ").strip().title()
new_quantity = int(input("Enter quantity: "))
new_price = float(input("Enter product price: "))

inventory[new_id] = {
    "name": new_name,
    "quantity": new_quantity,
    "price": new_price
}

print("Item added successfully!!!")
print(f"ID: {new_id} | Name: {new_name} | Quantity: {new_quantity} | Price: ${new_price:.2f}")
print("-------------------------------------------------------------------------------------------")
for product_id, product_data in inventory.items():
    print(f"ID: {product_id} | Name: {product_data['name']} | Quantity: {product_data['quantity']} | Price: ${product_data['price']:.2f}")
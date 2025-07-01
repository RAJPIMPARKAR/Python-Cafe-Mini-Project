# Cafe Menu Mini Project

# Define the menu as a dictionary
menu = {
    "Chai": 12,
    "Coffee": 20,
    "Pizza": 100,
    "Burger": 50,
    "Salad": 40
}

# Display the welcome message and menu
print("Welcome to our Cafe")
print("Menu:")
for item, price in menu.items():
    print(f"{item}: Rs{price}")

# Initialize order total
order_total = 0

# First item order
item_1 = input("Enter the name of the item you want to order: ")

if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item '{item_1}' has been added to your order.")
else:
    print(f"Ordered item '{item_1}' is not available!")

# Ask if the user wants to order another item
another_order = input("Do you want to add another item? (Yes/No): ")

if another_order.lower() == "yes":
    item_2 = input("Enter the name of the second item: ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item '{item_2}' has been added to your order.")
    else:
        print(f"Ordered item '{item_2}' is not available!")

# Final total
print(f"The total amount of your order is: Rs{order_total}")
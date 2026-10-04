"""
main.py - Entry point for CampusCart.

Imports and combines inventory, cart, and logger modules
into one working CLI application.

Author: Nahim
"""

import inventory
import cart
import logger

shopping_cart = cart.Cart()


@logger.log_transaction
def add_item_to_cart(item_id, qty):
    product = inventory.get_product(item_id)
    if product is None:
        print("Product not found.")
        return
    shopping_cart.add_item(product["name"], product["price"], qty)
    print(f"Added {qty} x {product['name']} to cart.")


if __name__ == "__main__":
    while True:
        print("\n=== CampusCart ===")
        print("1. View Inventory")
        print("2. Add Item to Cart")
        print("3. View Cart / Checkout")
        print("4. View Transaction Summary")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            print("\n--- In Stock ---")
            for item in inventory.filter_in_stock(inventory.inventory):
                print(item)

        elif choice == "2":
            item_id = input("Enter product ID: ").strip()
            qty_input = input("Enter quantity: ").strip()
            if not qty_input.isdigit():
                print("Invalid quantity.")
                continue
            add_item_to_cart(item_id, int(qty_input))

        elif choice == "3":
            print("\n--- Receipt ---")
            for line in shopping_cart.receipt_lines():
                print(line)

        elif choice == "4":
            logger.summary()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option, try again.")
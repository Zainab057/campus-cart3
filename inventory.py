"""
inventory.py - Product inventory management for CampusCart.
Store product data(name, price, stock) and provides functions
to view filter, and sort inventory using lamda functions.

Author: Nahim
"""

inventory = {
    "101": {"name": "Bread", "price": 1500, "stock": 10},
    "102":{"name": "Drink", "price": 800, "stock": 20},
    "103":{"name": "Biscuit", "price": 500, "stock": 15}
}
def get_product(item_id):
    return inventory.get(item_id)
def filter_in_stock(data):
    return list(filter(lambda item:item[1]["stock"] > 0, data.items()))
def sort_by_price(data):
    return sorted(data.items(), key = lambda item: item[1]["price"])

if __name__ == "__main__":
    print("In-stock items:", filter_in_stock(inventory))
    print("Sorted by price:", sort_by_price(inventory))
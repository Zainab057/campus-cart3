"""
cart.py

Handles shopping cart management for the Campus Cart CLI.

Program scope:
- Add products to the cart.
- Store selected quantities.
- Calculate the subtotal.
- Generate receipt lines using a generator.
"""
class Cart:
    """Manage products selected by a customer."""

    def __init__(self):
        self.items = []
    def add_item(self, name, price, quantity):
        item = {
            "name": name,
            "price": price,
            "quantity": quantity
            }

        self.items.append(item)
    def calculate_subtotal(self):
        """Calculate the total cost of all items in the cart."""
        subtotal = 0

        for item in self.items:
            subtotal += item["price"] * item["quantity"]

        return subtotal
    def receipt_lines(self):
        """Generate receipt lines one at a time."""
        for item in self.items:
            total = item["price"] * item["quantity"]

            yield f"{item["name"]} x{item["quantity"]} = ₦{total:,.2f}"

        yield f"Subtotal = ₦{self.calculate_subtotal():,.2f}"
if __name__ == "__main__":
    cart = Cart()

    cart.add_item("Bread", 1500, 2)
    cart.add_item("Drink", 800, 1)

    for line in cart.receipt_lines():
        print(line)
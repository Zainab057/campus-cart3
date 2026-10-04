# campus-cart project

A CLI solution for campus vendors to streamline stock tracking, cart totals, and receipt generation.

# Campus Vendor CLI

A simple command-line interface (CLI) solution designed to help campus vendors efficiently manage their daily sales and inventory operations.

## Overview

Campus vendors often need to keep track of available stock, calculate customer purchases, and provide accurate receipts. Doing these tasks manually can be time-consuming and may lead to calculation errors or difficulty monitoring inventory.

**Campus Vendor CLI** provides a straightforward command-line solution that simplifies these processes. The application allows vendors to manage their stock, add products to a customer's cart, automatically calculate totals, and generate receipts for completed purchases.

## Features

* **Stock Tracking**
  Keep track of products available in the vendor's inventory and monitor stock levels.

* **Product Management**
  Add and manage products, including product names, prices, and quantities.

* **Shopping Cart**
  Add products to a customer's cart and keep track of selected items and quantities.

* **Automatic Cart Totals**
  Calculate the total cost of items in the cart automatically, reducing manual calculation errors.

* **Receipt Generation**
  Generate a clear receipt showing purchased items, quantities, prices, and the total amount.

* **Simple CLI Interface**
  Perform common vendor tasks directly from the terminal using an easy-to-use command-line interface.

## How It Works

The application follows a simple workflow:

1. The vendor adds or manages products in the inventory.
2. A customer selects the products they want to purchase.
3. The selected products are added to the shopping cart.
4. The system calculates the total cost automatically.
5. Stock quantities are updated after a successful purchase.
6. A receipt is generated showing the details of the transaction.

## Example

A typical transaction might look like:

```text
Campus Vendor CLI

Available Products:
1. Bread       ₦1,500
2. Soft Drink  ₦800
3. Biscuit     ₦500

Select a product: 1
Enter quantity: 2

Select a product: 2
Enter quantity: 1

-----------------------------
Receipt
-----------------------------
Bread        x2     ₦3,000
Soft Drink   x1       ₦800
-----------------------------
Total:              ₦3,800
-----------------------------

Thank you for your purchase!
```

## Technologies

* Python
* Command Line Interface (CLI)
* Git & GitHub

## Project Goals

The main goal of this project is to provide campus vendors with a simple and efficient tool for managing basic inventory and sales activities while also demonstrating practical Python programming concepts.This project helps campus vendors manage stock and sales.
## Future Improvements

Possible future improvements include:

* Saving inventory data permanently using a database or file.
* Adding user authentication for vendors.
* Supporting discounts and promotional pricing.
* Adding daily and monthly sales reports.
* Providing low-stock alerts.
* Adding a graphical user interface (GUI).
* Supporting multiple vendors and product categories.

## Author

**zainab kudayisi**

## License

This project is licensed under the MIT License.


# customer.py
class Customer:
    def __init__(self, name, contact_info, account_details):
        # Initialize a customer with their name, contact info, and account details (like loyalty membership)
        self.__name = name
        self.__contact_info = contact_info
        self.__loyalty_member = loyalty_member
        # Set loyalty discount to 10% if the customer is part of the loyalty program, else 0%
        self.__loyalty_discount = 0.10 if account_details == "Loyalty" else 0

    def get_name(self):
        # Get the customer's name
        return self.__name

    def get_loyalty_discount(self):
        # Return the loyalty discount percentage (if applicable)
        return self.__loyalty_discount

    def __str__(self):
        # String representation of the customer (for easy printing)
        return f"Customer: {self.__name}, Contact: {self.__contact_info}"

# ebook.py
class EBook:
    def __init__(self, title, author, publication_date, genre, price):
        # Initialize an eBook with title, author, publication date, genre, and price
        self.__title = title
        self.__author = author
        self.__publication_date = publication_date
        self.__genre = genre
        self.__price = price

    def get_price(self):
        # Get the price of the eBook
        return self.__price

    def __str__(self):
        # String representation of the eBook (for easy printing)
        return f"EBook: {self.__title}, Author: {self.__author}, Price: {self.__price}"

# shopping_cart.py
class ShoppingCart:
    def __init__(self):
        # Initialize an empty shopping cart
        self.__items = []

    def add_ebook(self, ebook):
        # Add an eBook to the shopping cart
        self.__items.append(ebook)

    def remove_ebook(self, ebook):
        # Remove an eBook from the shopping cart if it exists in the cart
        if ebook in self.__items:
            self.__items.remove(ebook)

    def get_total_price(self):
        # Calculate the total price of all eBooks in the cart
        total_price = sum(ebook.get_price() for ebook in self.__items)
        return total_price

    def get_items_count(self):
        # Return the number of items (eBooks) in the cart
        return len(self.__items)

    def __str__(self):
        # String representation of the shopping cart (for easy printing)
        return f"Cart: {len(self.__items)} items, Total Price: {self.get_total_price()}"

# order.py
class Order:
    def __init__(self, customer, shopping_cart, order_date):
        # Initialize an order with a customer, their shopping cart, and the order date
        self.__customer = customer
        self.__shopping_cart = shopping_cart
        self.__order_date = order_date
        self.__invoice = None

    def generate_invoice(self):
        # Generate an invoice based on the customer's order
        self.__invoice = Invoice(self.__customer, self.__shopping_cart)
        return self.__invoice

    def __str__(self):
        # String representation of the order (for easy printing)
        return f"Order Date: {self.__order_date}, Total: {self.__shopping_cart.get_total_price()}"

# invoice.py
class Invoice:
    VAT_RATE = 0.08  # A fixed VAT rate of 8%

    def __init__(self, customer, shopping_cart):
        # Initialize an invoice with customer and shopping cart details
        self.__customer = customer
        self.__shopping_cart = shopping_cart
        self.__discounts = []  # List of discounts to apply
        self.__final_amount = self.calculate_final_amount()  # Calculate the final amount right away

    def apply_loyalty_discount(self):
        # Calculate and apply loyalty discount (if applicable) to the total price
        loyalty_discount = self.__shopping_cart.get_total_price() * self.__customer.get_loyalty_discount()
        self.__discounts.append(loyalty_discount)

    def apply_bulk_discount(self):
        # Apply a bulk discount of 20% if the customer buys 5 or more eBooks
        if self.__shopping_cart.get_items_count() >= 5:
            bulk_discount = self.__shopping_cart.get_total_price() * 0.20
            self.__discounts.append(bulk_discount)

    def calculate_final_amount(self):
        # Calculate the final amount after applying all discounts and VAT
        total_amount = self.__shopping_cart.get_total_price()  # Start with total price
        self.apply_loyalty_discount()  # Apply loyalty discount if eligible
        self.apply_bulk_discount()  # Apply bulk discount if eligible
        discount_total = sum(self.__discounts)  # Sum all discounts
        total_after_discount = total_amount - discount_total  # Apply discounts to total amount
        vat = total_after_discount * Invoice.VAT_RATE  # Calculate VAT on the discounted total
        return total_after_discount + vat  # Return the total price with VAT included

    def __str__(self):
        # String representation of the invoice (for easy printing)
        return f"Invoice for {self.__customer.get_name()} - Final Amount: {self.__final_amount:.2f}"

# Example usage
customer1 = Customer("Mariam Almansoori", "Mariamm09@icloud.com", "Loyalty")

# Create a few eBooks
ebook1 = EBook("Atomic Habits", "James Clear", "2018", "self help book", 20.0)
ebook2 = EBook("The Poppy War", "R.F. Kuang", "2018", "historical military fantasy", 15.0)


# Add eBooks to the shopping cart
cart = ShoppingCart()
cart.add_ebook(ebook1)
cart.add_ebook(ebook2)


# Create an order with the customer and shopping cart
order = Order(customer1, cart, "2024-10-30")

# Generate an invoice for the order
invoice = order.generate_invoice()

# Display the invoice with loyalty and bulk discounts applied
print(invoice)

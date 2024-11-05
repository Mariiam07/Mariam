class Customer:
    def __init__(self, name, contact_info, loyalty_member):
        self.__name = name  # Customer's name
        self.__contact_info = contact_info  # Customer's contact information
        self.__loyalty_member = loyalty_member  # Boolean indicating loyalty membership status
        self.__loyalty_discount = 0.10 if loyalty_member else 0  # Loyalty discount

    def get_name(self):
        return self.__name  # Method to return the customer's name

    def apply_loyalty_discount(self, total):
        # Method to apply loyalty discount to a given total
        if self.__loyalty_member:
            return total * self.__loyalty_discount
        return 0


class EBook:
    def __init__(self, title, author, publication_date, genre, price):
        self.__title = title  # Title of the eBook
        self.__author = author  # Author of the eBook
        self.__publication_date = publication_date  # Publication date of the eBook
        self.__genre = genre  # Genre of the eBook
        self.__price = price  # Price of the eBook

    def get_price(self):
        return self.__price  # Method to return the price of the eBook


class ShoppingCart:
    def __init__(self):
        self.__items = []  # A collection (list) of EBook objects

    def add_ebook(self, ebook):
        self.__items.append(ebook)  # Method to add an eBook to the cart

    def remove_ebook(self, ebook):
        if ebook in self.__items:
            self.__items.remove(ebook)  # Method to remove an eBook from the cart

    def get_total_price(self):
        return sum(ebook.get_price() for ebook in self.__items)  # Method to get the total price of all eBooks

    def apply_bulk_discount(self):
        # Logic for applying a bulk discount could be implemented here
        pass

    def get_items_count(self):
        return len(self.__items)  # Method to return the number of items in the cart


class Order:
    def __init__(self, customer, shopping_cart, order_date):
        self.__customer = customer  # Composition: An order cannot exist without a customer
        self.__shopping_cart = shopping_cart  # Composition: An order is tightly coupled with its shopping cart
        self.__order_date = order_date  # Date of the order

    def generate_invoice(self):
        # Method to generate an invoice based on the customer's order
        return Invoice(self.__customer, self.__shopping_cart)  # Create and return an invoice


class Invoice:
    VAT_RATE = 0.08  # A fixed VAT rate of 8%

    def __init__(self, customer, shopping_cart):
        self.__customer = customer  # Customer for whom the invoice is generated
        self.__shopping_cart = shopping_cart  # Shopping cart associated with the invoice
        self.__discounts = []  # Discounts applied to the invoice
        self.__final_amount = self.calculate_final_amount()  # Total amount after discounts and VAT

    def calculate_final_amount(self):
        # Method to calculate the final amount after applying discounts and VAT
        total_amount = self.__shopping_cart.get_total_price()  # Get total price from shopping cart
        loyalty_discount = self.__customer.apply_loyalty_discount(total_amount)  # Apply loyalty discount
        self.__discounts.append(loyalty_discount)  # Add loyalty discount to discounts
        bulk_discount = self.apply_bulk_discount()  # Apply bulk discount
        self.__discounts.append(bulk_discount)  # Add bulk discount to discounts

        discount_total = sum(self.__discounts)  # Sum all discounts
        total_after_discount = total_amount - discount_total  # Apply discounts to total amount
        vat = total_after_discount * Invoice.VAT_RATE  # Calculate VAT on the discounted total
        return total_after_discount + vat  # Return the total price with VAT included

    def apply_bulk_discount(self):
        # Apply a bulk discount of 20% if the customer buys 5 or more eBooks
        if self.__shopping_cart.get_items_count() >= 5:
            return self.__shopping_cart.get_total_price() * 0.20
        return 0  # No bulk discount


# Customer Me :)
customer1 = Customer("Mariam Almansoori", "Mariamm09@icloud.com", True)

# My favourite eBooks
ebook1 = EBook("Atomic Habits", "James Clear", "2018", "Self-help", 20.0)
ebook2 = EBook("The Poppy War", "R.F. Kuang", "2018", "Historical Military Fantasy", 15.0)

# Add eBooks to the shopping cart
cart = ShoppingCart()
cart.add_ebook(ebook1)
cart.add_ebook(ebook2)

# Create an order with the customer and shopping cart
order = Order(customer1, cart, "2024-10-30")

# Generate an invoice for the order
invoice = order.generate_invoice()

# Display the final amount on the invoice
print(f"Invoice for {invoice._Invoice__customer.get_name()} - Final Amount: {invoice.calculate_final_amount():.2f}")

# customer.py
class Customer:
    def __init__(self, name, contact_info, account_details):
        self.__name = name
        self.__contact_info = contact_info
        self.__account_details = account_details
        self.__loyalty_discount = None

    def get_name(self):
        return self.__name

    def apply_loyalty_discount(self, discount):
        self.__loyalty_discount = discount

    def get_discount(self):
        return self.__loyalty_discount

    def __str__(self):
        return f"Customer: {self.__name}, Contact: {self.__contact_info}"

# order.py
class Order:
    def __init__(self, order_date, invoice_details, total_amount):
        self.__order_date = order_date
        self.__invoice_details = invoice_details
        self.__total_amount = total_amount

    def generate_invoice(self):
        return Invoice(self.__invoice_details, self.__total_amount)

    def __str__(self):
        return f"Order Date: {self.__order_date}, Total: {self.__total_amount}"

# invoice.py
class Invoice:
    def __init__(self, invoice_details, total_amount):
        self.__invoice_details = invoice_details
        self.__total_amount = total_amount
        self.__discounts = []

    def add_discount(self, discount):
        self.__discounts.append(discount)

    def calculate_final_amount(self):
        final_amount = self.__total_amount
        for discount in self.__discounts:
            final_amount -= discount
        return final_amount

    def __str__(self):
        return f"Invoice: {self.__invoice_details}, Final Amount: {self.calculate_final_amount()}"

# ebook.py
class EBook:
    def __init__(self, title, author, publication_date, genre, price):
        self.__title = title
        self.__author = author
        self.__publication_date = publication_date
        self.__genre = genre
        self.__price = price

    def get_price(self):
        return self.__price

    def __str__(self):
        return f"EBook: {self.__title}, Author: {self.__author}, Price: {self.__price}"

# shopping_cart.py
class ShoppingCart:
    def __init__(self):
        self.__items = []
        self.__total_price = 0

    def add_ebook(self, ebook):
        self.__items.append(ebook)
        self.__total_price += ebook.get_price()

    def remove_ebook(self, ebook):
        if ebook in self.__items:
            self.__items.remove(ebook)
            self.__total_price -= ebook.get_price()

    def get_total_price(self):
        return self.__total_price

    def __str__(self):
        return f"Cart: {len(self.__items)} items, Total Price: {self.__total_price}"

# loyalty_discount.py
class LoyaltyDiscount:
    def __init__(self, discount_type, amount):
        self.__discount_type = discount_type
        self.__amount = amount

    def apply_discount(self, total):
        return total - self.__amount

    def __str__(self):
        return f"Loyalty Discount: {self.__discount_type}, Amount: {self.__amount}"


# Create a customer
customer1 = Customer("Mariam Almansoori", "Mariamm09@icloud.com", "Loyalty")
print(customer1)

# Create eBooks
ebook1 = EBook("Atomic Habits", "James Clear", "2018", "self help book", 20.0)
ebook2 = EBook("The Poppy War", "R.F. KUANG", "2018", "historical military fantasy", 15.0)

# Add eBooks to shopping cart
cart = ShoppingCart()
cart.add_ebook(ebook1)
cart.add_ebook(ebook2)
print(cart)

# Place an order
order = Order("2024-10-30", "Order for Mariam", cart.get_total_price())
invoice = order.generate_invoice()

# Apply a loyalty discount
discount = LoyaltyDiscount("Loyalty Member", 5.0)
customer1.apply_loyalty_discount(discount)
invoice.add_discount(customer1.get_discount().apply_discount(invoice.calculate_final_amount()))

# Display the invoice with the discount applied
print(invoice)

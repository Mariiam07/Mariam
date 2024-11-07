# Customer Class
class Customer:
    def __init__(self, name, contact_info, loyalty_member):
        self.__name = name  # Customer's name
        self.__contact_info = contact_info  # Customer's contact info
        self.__loyalty_member = loyalty_member  # Boolean indicating loyalty membership status
        self.__loyalty_discount = 0.10 if loyalty_member else 0  # Discount rate for loyalty members

    def get_name(self):
        return self.__name  # Method to return the customer's name

    def apply_loyalty_discount(self, total):
        if self.__loyalty_member:
            return total * self.__loyalty_discount
        return 0  # No discount if not a loyalty member


# EBook Class
class EBook:
    def __init__(self, title, author, publication_date, genre, price):
        self.__title = title  # Title of the eBook
        self.__author = author  # Author of the eBook
        self.__publication_date = publication_date  # Publication date of the eBook
        self.__genre = genre  # Genre of the eBook
        self.__price = price  # Price of the eBook

    def get_price(self):
        return self.__price  # Method to return the price of the eBook


# Aggregation: ShoppingCart contains multiple EBooks, but the eBooks exist independently
class ShoppingCart:
    def __init__(self):
        self.__items = []  # A list of EBook objects (aggregation relationship)

    def add_ebook(self, ebook):
        self.__items.append(ebook)  # Method to add an EBook to the cart

    def remove_ebook(self, ebook):
        if ebook in self.__items:
            self.__items.remove(ebook)  # Method to remove an EBook from the cart

    def get_total_price(self):
        return sum(ebook.get_price() for ebook in self.__items)  # Total price of all eBooks in the cart

    def get_items_count(self):
        return len(self.__items)  # Number of items in the shopping cart


# Composition: An order cannot exist without a customer
class Order:
    def __init__(self, customer, shopping_cart, order_date):
        self.__customer = customer  # Composition: Order needs a Customer to exist
        self.__shopping_cart = shopping_cart  # Aggregation: An order has a shopping cart, but the cart can exist independently
        self.__order_date = order_date  # Order date

    def generate_invoice(self):
        return Invoice(self.__customer, self.__shopping_cart)  # Composition: An order creates an invoice


# Invoice Class
class Invoice:
    VAT_RATE = 0.08  # A fixed VAT rate of 8%

    # Composition: An invoice cannot exist without an order
    def __init__(self, customer, shopping_cart):
        self.__customer = customer  # Customer associated with the invoice
        self.__shopping_cart = shopping_cart  # Shopping cart associated with the invoice
        self.__discounts = []  # Discounts applied to the invoice
        self.__final_amount = self.calculate_final_amount()  # Final amount after discounts and VAT

    def calculate_final_amount(self):
        total_amount = self.__shopping_cart.get_total_price()  # Total price from the shopping cart
        loyalty_discount = self.__customer.apply_loyalty_discount(total_amount)  # Apply loyalty discount
        self.__discounts.append(loyalty_discount)  # Add loyalty discount to the discounts
        bulk_discount = self.apply_bulk_discount()  # Apply bulk discount
        self.__discounts.append(bulk_discount)  # Add bulk discount to discounts

        discount_total = sum(self.__discounts)  # Total amount of discounts
        total_after_discount = total_amount - discount_total  # Total after applying discounts
        vat = total_after_discount * Invoice.VAT_RATE  # Calculate VAT
        return total_after_discount + vat  # Final amount after VAT

    def apply_bulk_discount(self):
        # Apply bulk discount if there are 5 or more eBooks
        if self.__shopping_cart.get_items_count() >= 5:
            return self.__shopping_cart.get_total_price() * 0.20
        return 0  # No discount if less than 5 eBooks


# Association: A customer may have a loyalty discount applied, but it's not permanent
class LoyaltyDiscount:
    def __init__(self, discount_type, amount):
        self.__discount_type = discount_type  # Type of the discount (e.g., loyalty, bulk)
        self.__amount = amount  # Discount amount

    def apply_discount(self, total):
        # Method to apply the discount to the total
        return total - self.__amount


# Example usage to demonstrate relationships

# Customer with loyalty membership
customer1 = Customer("Mariam Almansoori", "Mariamm09@icloud.com", True)

# Favorite eBooks
ebook1 = EBook("Atomic Habits", "James Clear", "2018", "Self-help", 20.0)
ebook2 = EBook("The Poppy War", "R.F. Kuang", "2018", "Historical Military Fantasy", 15.0)

# Add eBooks to the shopping cart (Aggregation: ShoppingCart has EBooks)
cart = ShoppingCart()
cart.add_ebook(ebook1)
cart.add_ebook(ebook2)

# Create an order (Composition: Order requires a Customer)
order = Order(customer1, cart, "2024-10-30")

# Generate an invoice for the order (Composition: Invoice created by an order)
invoice = order.generate_invoice()

# Display the final amount on the invoice
print(f"Invoice for {invoice._Invoice__customer.get_name()} - Final Amount: {invoice.calculate_final_amount():.2f}")

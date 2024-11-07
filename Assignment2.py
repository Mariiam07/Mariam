# Customer Class
class Customer:
    def __init__(self, name, contact_info, loyalty_member):
        self._name = name  # Protected attribute: Customer's name
        self._contact_info = contact_info  # Protected attribute: Customer's contact info
        self._loyalty_member = loyalty_member  # Boolean indicating loyalty membership status
        self._loyalty_discount = 0.10 if loyalty_member else 0  # Discount rate for loyalty members

    # Getter for name
    def get_name(self):
        return self._name

    # Setter for name
    def set_name(self, name):
        self._name = name

    # Getter for contact info
    def get_contact_info(self):
        return self._contact_info

    # Setter for contact info
    def set_contact_info(self, contact_info):
        self._contact_info = contact_info

    # Getter for loyalty member status
    def get_loyalty_member(self):
        return self._loyalty_member

    # Setter for loyalty member status
    def set_loyalty_member(self, loyalty_member):
        self._loyalty_member = loyalty_member
        self._loyalty_discount = 0.10 if loyalty_member else 0  # Update discount based on loyalty status

    def apply_loyalty_discount(self, total):
        if self._loyalty_member:
            return total * self._loyalty_discount
        return 0  # No discount if not a loyalty member


# EBook Class
class EBook:
    def __init__(self, title, author, publication_date, genre, price):
        self._title = title  # Protected attribute: Title of the eBook
        self._author = author  # Protected attribute: Author of the eBook
        self._publication_date = publication_date  # Protected attribute: Publication date
        self._genre = genre  # Protected attribute: Genre of the eBook
        self._price = price  # Protected attribute: Price of the eBook

    # Getter for title
    def get_title(self):
        return self._title

    # Setter for title
    def set_title(self, title):
        self._title = title

    # Getter for author
    def get_author(self):
        return self._author

    # Setter for author
    def set_author(self, author):
        self._author = author

    # Getter for publication date
    def get_publication_date(self):
        return self._publication_date

    # Setter for publication date
    def set_publication_date(self, publication_date):
        self._publication_date = publication_date

    # Getter for genre
    def get_genre(self):
        return self._genre

    # Setter for genre
    def set_genre(self, genre):
        self._genre = genre

    # Getter for price
    def get_price(self):
        return self._price

    # Setter for price
    def set_price(self, price):
        self._price = price


# ShoppingCart Class
class ShoppingCart:
    def __init__(self):
        self._items = []  # A list of EBook objects (aggregation relationship)

    def add_ebook(self, ebook):
        self._items.append(ebook)  # Method to add an EBook to the cart

    def remove_ebook(self, ebook):
        if ebook in self._items:
            self._items.remove(ebook)  # Method to remove an EBook from the cart

    def get_total_price(self):
        return sum(ebook.get_price() for ebook in self._items)  # Total price of all eBooks in the cart

    def get_items_count(self):
        return len(self._items)  # Number of items in the shopping cart

    # Getter for items
    def get_items(self):
        return self._items


# Order Class
class Order:
    def __init__(self, customer, shopping_cart, order_date):
        self._customer = customer  # Composition: Order needs a Customer to exist
        self._shopping_cart = shopping_cart  # Aggregation: An order has a shopping cart, but the cart can exist independently
        self._order_date = order_date  # Order date

    # Getter for customer
    def get_customer(self):
        return self._customer

    # Setter for customer
    def set_customer(self, customer):
        self._customer = customer

    # Getter for shopping cart
    def get_shopping_cart(self):
        return self._shopping_cart

    # Setter for shopping cart
    def set_shopping_cart(self, shopping_cart):
        self._shopping_cart = shopping_cart

    # Getter for order date
    def get_order_date(self):
        return self._order_date

    # Setter for order date
    def set_order_date(self, order_date):
        self._order_date = order_date

    def generate_invoice(self):
        return Invoice(self._customer, self._shopping_cart)  # Composition: An order creates an invoice


# Invoice Class
class Invoice:
    VAT_RATE = 0.08  # A fixed VAT rate of 8%

    def __init__(self, customer, shopping_cart):
        self._customer = customer  # Customer associated with the invoice
        self._shopping_cart = shopping_cart  # Shopping cart associated with the invoice
        self._discounts = []  # Discounts applied to the invoice
        self._final_amount = self.calculate_final_amount()  # Final amount after discounts and VAT

    # Getter for customer
    def get_customer(self):
        return self._customer

    # Setter for customer
    def set_customer(self, customer):
        self._customer = customer

    # Getter for shopping cart
    def get_shopping_cart(self):
        return self._shopping_cart

    # Setter for shopping cart
    def set_shopping_cart(self, shopping_cart):
        self._shopping_cart = shopping_cart

    def calculate_final_amount(self):
        total_amount = self._shopping_cart.get_total_price()  # Total price from the shopping cart
        loyalty_discount = self._customer.apply_loyalty_discount(total_amount)  # Apply loyalty discount
        self._discounts.append(loyalty_discount)  # Add loyalty discount to the discounts
        bulk_discount = self.apply_bulk_discount()  # Apply bulk discount
        self._discounts.append(bulk_discount)  # Add bulk discount to discounts

        discount_total = sum(self._discounts)  # Total amount of discounts
        total_after_discount = total_amount - discount_total  # Total after applying discounts
        vat = total_after_discount * Invoice.VAT_RATE  # Calculate VAT
        return total_after_discount + vat  # Final amount after VAT

    def apply_bulk_discount(self):
        # Apply bulk discount if there are 5 or more eBooks
        if self._shopping_cart.get_items_count() >= 5:
            return self._shopping_cart.get_total_price() * 0.20
        return 0  # No discount if less than 5 eBooks


# Example 

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
print(f"Invoice for {invoice.get_customer().get_name()} - Final Amount: {invoice.calculate_final_amount():.2f}")

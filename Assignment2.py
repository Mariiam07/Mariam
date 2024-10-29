class EBook:
    """Class to represent an e-book."""
    
    def __init__(self, title, author, publication_date, genre, price):
        self.__title = title
        self.__author = author
        self.__publication_date = publication_date
        self.__genre = genre
        self.__price = price

    # Getter methods
    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_price(self):
        return self.__price

    # __str__ 
    def __str__(self):
        return f"{self.__title} by {self.__author}, Price: ${self.__price:.2f}"

    
class Customer:
    """Class to represent a customer."""
    
    def __init__(self, name, contact_info):
        self.__name = name
        self.__contact_info = contact_info

    # Getter method
    def get_name(self):
        return self.__name

    # __str__ 
    def __str__(self):
        return f"Customer: {self.__name}, Contact: {self.__contact_info}"

    
class ShoppingCart:
    """Class to represent a shopping cart."""
    
    def __init__(self):
        self.__items = []

    # Add item to cart
    def add_item(self, ebook):
        self.__items.append(ebook)

    # Remove item from cart
    def remove_item(self, ebook):
        self.__items.remove(ebook)

    # Get all items in cart
    def get_items(self):
        return self.__items

    # __str__ 
    def __str__(self):
        return "Shopping Cart: " + ", ".join(str(item) for item in self.__items)

    
class Order:
    """Class to represent an order."""
    
    def __init__(self, customer, items):
        self.__customer = customer
        self.__items = items

    # Get customer
    def get_customer(self):
        return self.__customer

    # Get items
    def get_items(self):
        return self.__items

    # __str__ 
    def __str__(self):
        return f"Order for {self.__customer.get_name()}: {', '.join(str(item) for item in self.__items)}"


class Invoice:
    """Class to represent an invoice."""
    
    def __init__(self, order, discount=0):
        self.__order = order
        self.__discounts = discount  # Discounts applied
        self.__vat_rate = 0.08  # VAT fixed rate of 8%

    # Calculate total price including VAT and discount
    def calculate_total(self):
        total = sum(item.get_price() for item in self.__order.get_items())
        total -= self.__discounts
        total += total * self.__vat_rate
        return total

    # __str__ 
    def __str__(self):
        return (f"Invoice:\nCustomer: {self.__order.get_customer().get_name()}\n"
                f"Items: {', '.join(item.get_title() for item in self.__order.get_items())}\n"
                f"Discounts Applied: ${self.__discounts:.2f}\n"
                f"Total Amount (with VAT): ${self.calculate_total():.2f}")


# OUTPUT
if __name__ == "__main__":
    # Create e-books
    ebook1 = EBook("Python Programming", "Mariam Mubarak", "2022-11-21", "Programming", 29.99)
    ebook2 = EBook("Data Science Essentials", "Reem Munthir", "2022-12-15", "Data Science", 39.99)

    # Create a customer
    customer = Customer("Maitha", "Maithaaa090@icloud.com")

    # Create a shopping cart and add e-books
    cart = ShoppingCart()
    cart.add_item(ebook1)
    cart.add_item(ebook2)

    # Create an order
    order = Order(customer, cart.get_items())

    # Generate an invoice with a $5 discount
    invoice = Invoice(order, discount=5.00)
    print(invoice)

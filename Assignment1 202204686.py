# This class represents a customer at the hotel, since tt stores the customer's personal info like name, email, contact details, reservation, and payment info.
class Customer:
    def __init__(self, name, email, contact, reservation_id, payment_details):
        self.name = name  # Customer's name
        self.email = email  # Customer's email address
        self.contact = contact  # Phone number or other contact details
        self.reservation_id = reservation_id  # ID of the reservation the customer has made
        self.payment_details = payment_details  # Info about how the customer paid (credit card, etc.)

    # This method allows the customer to create a reservation by providing a reservation object, by updates the reservation ID and confirms the reservation was created.
    def create_reservation(self, reservation):
        self.reservation_id = reservation.reservation_id
        return f"Reservation {reservation.reservation_id} created."

    # Allows the customer to cancel their reservation. The reservation ID is cleared.
    def cancel_reservation(self):
        self.reservation_id = None
        return "Reservation canceled."

    # Lets the customer check the reservation details by showing the current reservation ID.
    def view_reservation(self):
        return f"Current Reservation ID: {self.reservation_id}"

    # This retrieves the customer's name, in case it's needed elsewhere in the system.
    def get_name(self):
        return self.name

    # Allows the customer's name to be updated, maybe if it was entered incorrectly or legally changed.
    def set_name(self, name):
        self.name = name


# This class manages reservations, it holds details like the reservation ID, the room info, check-in and check-out dates, and the total cost.
class Reservation:
    def __init__(self, reservation_id, room_details, check_in_date, check_out_date, total_cost):
        self.reservation_id = reservation_id  # Unique ID for the reservation
        self.room_details = room_details  # Description of the room the customer reserved
        self.check_in_date = check_in_date  # When the customer plans to check in
        self.check_out_date = check_out_date  # When the customer plans to check out
        self.total_cost = total_cost  # The overall cost of the stay

    # Confirms that the reservation has been successfully made.
    def confirm_reservation(self):
        return f"Reservation {self.reservation_id} confirmed."

    # Allows the customer to cancel their reservation.
    def cancel_reservation(self):
        return f"Reservation {self.reservation_id} canceled."

    # Gives the full details of the reservation, so the customer or hotel staff can review it.
    def view_details(self):
        return (f"Reservation ID: {self.reservation_id}, Room Details: {self.room_details}, "
                f"Check-in: {self.check_in_date}, Check-out: {self.check_out_date}, Total Cost: ${self.total_cost}")


# This class represents a hotel room and includes information like the room's ID, type, availability, and price.
class Hotel:
    def __init__(self, room_id, room_type, availability_status, price):
        self.room_id = room_id  # A unique identifier for the specific room
        self.room_type = room_type  # What kind of room it is
        self.availability_status = availability_status  # Whether the room is available for booking or not
        self.price = price  # The price per night for the room

    # This method updates whether the room is available or occupied, it's useful for managing bookings in real time.
    def update_availability(self, status):
        self.availability_status = status  # Update the room's availability status
        return f"Room {self.room_id} availability updated to {status}."

    # This returns the details of the room, such as its type, availability, and price.
    def view_room_details(self):
        return f"Room ID: {self.room_id}, Type: {self.room_type}, Status: {self.availability_status}, Price: ${self.price}"


# The Payment class handles everything to do with payments, it stores payment info like how much was paid, the method (credit card, cash), and whether the payment was processed.
class Payment:
    def __init__(self, payment_id, reservation_id, amount, payment_method, payment_status):
        self.payment_id = payment_id  # Unique ID for the payment transaction
        self.reservation_id = reservation_id  # Links this payment to a specific reservation
        self.amount = amount  # The total amount of the payment
        self.payment_method = payment_method  # How the customer paid (credit card, cash)
        self.payment_status = payment_status  # the payment has been processed or not

    # Processes the payment by marking the status as "Processed." This would be used when the payment goes through.
    def process_payment(self):
        self.payment_status = "Processed"  # Update the payment status to show it's complete
        return f"Payment of ${self.amount} processed."

    # Allows for a refund by changing the status to "Refunded." Useful if the customer cancels or has an issue.
    def issue_refund(self):
        self.payment_status = "Refunded"  # Update the payment status to show the money has been returned
        return f"Refund of ${self.amount} issued."


# Creating a customer with basic details like name, email, contact info, and payment details.
customer = Customer("Ted Vera", "tedvera@mac.com", "555-1234", "15549850358", "Mastercard 9904")

# Setting up a reservation for the customer. Includes details about the room, dates, and total cost.
reservation = Reservation("15549850358", "2 Queen Beds, Non-smoking", "Aug 22, 2010", "Aug 24, 2010", 201.48)

# Defining a hotel room with details like room ID, type of room, availability, and price.
hotel_room = Hotel("52523687", "2 Queen Beds", "Available", 89.95)

# Creating a payment instance for the customer's reservation, showing how they paid and the amount.
payment = Payment("P9904", "15549850358", 201.48, "Mastercard", "Processed")

# Printing out some customer details.
print(f"Customer Name: {customer.get_name()}")

# Showing the reservation ID linked to this booking.
print(f"Reservation ID: {reservation.reservation_id}")

# Displaying what kind of room was reserved.
print(f"Room Details: {reservation.room_details}")

# Showing when the customer plans to check in.
print(f"Check-in Date: {reservation.check_in_date}")

# Displaying the total cost of the reservation.
print(f"Total Cost: ${reservation.total_cost}")

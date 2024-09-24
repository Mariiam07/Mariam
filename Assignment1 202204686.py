class Customer:
    def __init__(self, name, email, contact, reservation_id, payment_details):
        self.name = name
        self.email = email
        self.contact = contact
        self.reservation_id = reservation_id
        self.payment_details = payment_details

    def create_reservation(self, reservation):
        self.reservation_id = reservation.reservation_id
        return f"Reservation {reservation.reservation_id} created."

    def cancel_reservation(self):
        self.reservation_id = None
        return "Reservation canceled."

    def view_reservation(self):
        return f"Current Reservation ID: {self.reservation_id}"

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name


class Reservation:
    def __init__(self, reservation_id, room_details, check_in_date, check_out_date, total_cost):
        self.reservation_id = reservation_id
        self.room_details = room_details
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.total_cost = total_cost

    def confirm_reservation(self):
        return f"Reservation {self.reservation_id} confirmed."

    def cancel_reservation(self):
        return f"Reservation {self.reservation_id} canceled."

    def view_details(self):
        return f"Reservation ID: {self.reservation_id}, Room Details: {self.room_details}, Check-in: {self.check_in_date}, Check-out: {self.check_out_date}, Total Cost: ${self.total_cost}"


class Hotel:
    def __init__(self, room_id, room_type, availability_status, price):
        self.room_id = room_id
        self.room_type = room_type
        self.availability_status = availability_status
        self.price = price

    def update_availability(self, status):
        self.availability_status = status
        return f"Room {self.room_id} availability updated to {status}."

    def view_room_details(self):
        return f"Room ID: {self.room_id}, Type: {self.room_type}, Status: {self.availability_status}, Price: ${self.price}"


class Payment:
    def __init__(self, payment_id, reservation_id, amount, payment_method, payment_status):
        self.payment_id = payment_id
        self.reservation_id = reservation_id
        self.amount = amount
        self.payment_method = payment_method
        self.payment_status = payment_status

    def process_payment(self):
        self.payment_status = "Processed"
        return f"Payment of ${self.amount} processed."

    def issue_refund(self):
        self.payment_status = "Refunded"
        return f"Refund of ${self.amount} issued."


customer = Customer("Ted Vera", "tedvera@mac.com", "555-1234", "15549850358", "Mastercard 9904")

reservation = Reservation("15549850358", "2 Queen Beds, Non-smoking", "Aug 22, 2010", "Aug 24, 2010", 201.48)

hotel_room = Hotel("52523687", "2 Queen Beds", "Available", 89.95)

payment = Payment("P9904", "15549850358", 201.48, "Mastercard", "Processed")

print(f"Customer Name: {customer.get_name()}")
print(f"Reservation ID: {reservation.reservation_id}")
print(f"Room Details: {reservation.room_details}")
print(f"Check-in Date: {reservation.check_in_date}")
print(f"Total Cost: ${reservation.total_cost}")
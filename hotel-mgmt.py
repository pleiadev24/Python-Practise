class Hotel:
    def __init__(self,room_number,capacity,is_occcupied=False):
        self.rooms=room_number
        self.capcity=capacity
        self.is_occupied=is_occcupied

    def __str__(self):
        return f"Room {self.room_number} ({'occupied' if self.is_occupied else 'vacant'})"

class Guest:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"{self.name} ({self.email})"
    
class Reservation:
    def __init__(self, guest, room, check_in_date, check_out_date):
        self.guest = guest
        self.room = room
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
    
    def __str__(self):
        return -f"Reservation for{self.guest}in {self.room}from {self.check_in_date} to {self.check_out_date}"

    def add_room(self, room):
        self.rooms.append(room)

    def display_rooms(self):
        print(f"Rooms in {self.name}:")
        for room in self.rooms:
            print(room)
    

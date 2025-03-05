import tkinter as tk
from tkinter import messagebox

class Room:
    def __init__(self, room_number, room_type, price, amenities):
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.amenities = amenities

    def __repr__(self):
        return f"Room {self.room_number}: {self.room_type}, Price: ${self.price}, Amenities: {', '.join(self.amenities)}"

class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def get_available_rooms(self):
        return self.rooms

class Customer:
    def __init__(self, budget, preferred_room_type, required_amenities):
        self.budget = budget
        self.preferred_room_type = preferred_room_type
        self.required_amenities = required_amenities

    def filter_rooms(self, rooms):
        return [
            room for room in rooms
            if room.price <= self.budget
            and (self.preferred_room_type.lower() in room.room_type.lower() or self.preferred_room_type == "")
            and all(amenity in room.amenities for amenity in self.required_amenities)
        ]

def search_rooms():
    try:
        budget = float(budget_entry.get())
        preferred_room_type = room_type_entry.get()
        required_amenities = [a.strip() for a in amenities_entry.get().split(',') if a.strip()]
        
        customer = Customer(budget, preferred_room_type, required_amenities)
        matched_rooms = customer.filter_rooms(hotel.get_available_rooms())
        
        result_text.delete(1.0, tk.END)
        if matched_rooms:
            for room in matched_rooms:
                result_text.insert(tk.END, str(room) + "\n")
        else:
            result_text.insert(tk.END, "No rooms match your criteria. Please adjust your preferences.")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number for budget.")

# Create hotel and add rooms
hotel = Hotel("Ocean View Hotel")
hotel.add_room(Room(101, "Single", 100, ["Wi-Fi", "Air Conditioning", "TV"]))
hotel.add_room(Room(102, "Double", 150, ["Wi-Fi", "Air Conditioning", "TV", "Minibar"]))
hotel.add_room(Room(103, "Suite", 250, ["Wi-Fi", "Air Conditioning", "TV", "Minibar", "Ocean View"]))
hotel.add_room(Room(104, "Single", 90, ["Wi-Fi", "TV"]))
hotel.add_room(Room(105, "Double", 200, ["Wi-Fi", "Air Conditioning", "TV", "Minibar", "Balcony"]))

# Create GUI
root = tk.Tk()
root.title("Hotel Room Search")

tk.Label(root, text="Budget (USD):").grid(row=0, column=0)
budget_entry = tk.Entry(root)
budget_entry.grid(row=0, column=1)

tk.Label(root, text="Preferred Room Type:").grid(row=1, column=0)
room_type_entry = tk.Entry(root)
room_type_entry.grid(row=1, column=1)

tk.Label(root, text="Required Amenities (comma separated):").grid(row=2, column=0)
amenities_entry = tk.Entry(root)
amenities_entry.grid(row=2, column=1)

search_button = tk.Button(root, text="Search", command=search_rooms)
search_button.grid(row=3, columnspan=2)

result_text = tk.Text(root, height=10, width=50)
result_text.grid(row=4, columnspan=2)

root.mainloop()

import tkinter as tk
from tkinter import messagebox

class Car:
    def __init__(self, model, price, fuel_efficiency, brand, horsepower, safety_rating, color):
        self.model = model
        self.price = price
        self.fuel_efficiency = fuel_efficiency
        self.brand = brand
        self.horsepower = horsepower
        self.safety_rating = safety_rating
        self.color = color
    
    def __repr__(self):
        return f"{self.model} ({self.brand}): ${self.price}, {self.fuel_efficiency} MPG, Safety: {self.safety_rating} Stars"

class CarShop:
    def __init__(self):
        self.cars = []
    
    def add_car(self, car):
        self.cars.append(car)
    
    def get_available_cars(self):
        return self.cars

class CarBuyer:
    def __init__(self, budget, min_fuel_efficiency, brand_preference, min_safety_rating):
        self.budget = budget
        self.min_fuel_efficiency = min_fuel_efficiency
        self.brand_preference = brand_preference
        self.min_safety_rating = min_safety_rating
    
    def filter_cars(self, cars):
        return [
            car for car in cars
            if car.price <= self.budget
            and car.fuel_efficiency >= self.min_fuel_efficiency
            and (self.brand_preference.lower() in car.brand.lower() or self.brand_preference == "")
            and car.safety_rating >= self.min_safety_rating
        ]

def search_cars():
    try:
        budget = float(budget_entry.get())
        min_fuel_efficiency = float(fuel_efficiency_entry.get())
        brand_preference = brand_entry.get()
        min_safety_rating = float(safety_entry.get())
        
        buyer = CarBuyer(budget, min_fuel_efficiency, brand_preference, min_safety_rating)
        matched_cars = buyer.filter_cars(car_shop.get_available_cars())
        
        result_text.delete(1.0, tk.END)
        if matched_cars:
            for car in matched_cars:
                result_text.insert(tk.END, str(car) + "\n")
        else:
            result_text.insert(tk.END, "No cars match your criteria. Please adjust your preferences.")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for budget, fuel efficiency, and safety rating.")

# Create CarShop and add cars
car_shop = CarShop()
car_shop.add_car(Car('Honda Civic', 22000, 30, 'Honda', 158, 4.5, 'Red'))
car_shop.add_car(Car('Toyota Corolla', 21000, 32, 'Toyota', 139, 4.7, 'Blue'))
car_shop.add_car(Car('BMW 3 Series', 35000, 25, 'BMW', 255, 4.2, 'Black'))
car_shop.add_car(Car('Ford Focus', 20000, 28, 'Ford', 160, 4.3, 'White'))
car_shop.add_car(Car('Chevrolet Malibu', 23000, 26, 'Chevrolet', 160, 4.4, 'Silver'))

# Create GUI
root = tk.Tk()
root.title("Car Shop")

tk.Label(root, text="Budget (USD):").grid(row=0, column=0)
budget_entry = tk.Entry(root)
budget_entry.grid(row=0, column=1)

tk.Label(root, text="Min Fuel Efficiency (MPG):").grid(row=1, column=0)
fuel_efficiency_entry = tk.Entry(root)
fuel_efficiency_entry.grid(row=1, column=1)

tk.Label(root, text="Preferred Brand:").grid(row=2, column=0)
brand_entry = tk.Entry(root)
brand_entry.grid(row=2, column=1)

tk.Label(root, text="Min Safety Rating (out of 5):").grid(row=3, column=0)
safety_entry = tk.Entry(root)
safety_entry.grid(row=3, column=1)

search_button = tk.Button(root, text="Search", command=search_cars)
search_button.grid(row=4, columnspan=2)

result_text = tk.Text(root, height=10, width=50)
result_text.grid(row=5, columnspan=2)

root.mainloop()

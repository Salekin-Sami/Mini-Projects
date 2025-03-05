import tkinter as tk
from tkinter import messagebox

class RestaurantGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Management System")
        
        self.menu = {}  # Dictionary to store menu items and prices
        self.order = {}  # Dictionary to store orders
        
        self.create_widgets()
    
    def create_widgets(self):
        # Menu Management Frame
        menu_frame = tk.LabelFrame(self.root, text="Menu Management")
        menu_frame.pack(padx=10, pady=5, fill="both")
        
        tk.Label(menu_frame, text="Item Name:").grid(row=0, column=0)
        self.item_name_entry = tk.Entry(menu_frame)
        self.item_name_entry.grid(row=0, column=1)
        
        tk.Label(menu_frame, text="Price:").grid(row=1, column=0)
        self.item_price_entry = tk.Entry(menu_frame)
        self.item_price_entry.grid(row=1, column=1)
        
        tk.Button(menu_frame, text="Add Item", command=self.add_item).grid(row=2, column=0, columnspan=2, pady=5)
        
        # Order Management Frame
        order_frame = tk.LabelFrame(self.root, text="Take Order")
        order_frame.pack(padx=10, pady=5, fill="both")
        
        self.menu_listbox = tk.Listbox(order_frame)
        self.menu_listbox.pack(padx=5, pady=5, fill="both")
        
        tk.Label(order_frame, text="Quantity:").pack()
        self.quantity_entry = tk.Entry(order_frame)
        self.quantity_entry.pack()
        
        tk.Button(order_frame, text="Add to Order", command=self.add_to_order).pack(pady=5)
        
        # Bill Calculation Frame
        bill_frame = tk.LabelFrame(self.root, text="Bill Summary")
        bill_frame.pack(padx=10, pady=5, fill="both")
        
        self.bill_text = tk.Text(bill_frame, height=8, width=40)
        self.bill_text.pack(padx=5, pady=5)
        
        tk.Button(bill_frame, text="Calculate Bill", command=self.calculate_bill).pack(pady=5)
    
    def add_item(self):
        item = self.item_name_entry.get().strip().title()
        try:
            price = float(self.item_price_entry.get())
            if item and item not in self.menu:
                self.menu[item] = price
                self.menu_listbox.insert(tk.END, f"{item}: ${price:.2f}")
                self.item_name_entry.delete(0, tk.END)
                self.item_price_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "Item already exists or invalid input.")
        except ValueError:
            messagebox.showerror("Error", "Invalid price entered.")
    
    def add_to_order(self):
        selected = self.menu_listbox.curselection()
        if not selected:
            messagebox.showwarning("Warning", "Please select an item from the menu.")
            return
        
        item_text = self.menu_listbox.get(selected[0])
        item_name = item_text.split(":")[0]
        try:
            quantity = int(self.quantity_entry.get())
            if quantity > 0:
                self.order[item_name] = self.order.get(item_name, 0) + quantity
                self.quantity_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "Quantity must be greater than 0.")
        except ValueError:
            messagebox.showerror("Error", "Invalid quantity entered.")
    
    def calculate_bill(self):
        if not self.order:
            messagebox.showinfo("Info", "No items in order.")
            return
        
        subtotal = sum(self.menu[item] * qty for item, qty in self.order.items())
        tax = subtotal * 0.05
        service_charge = subtotal * 0.10
        total = subtotal + tax + service_charge
        
        bill_summary = "\n".join([f"{item} x {qty} = ${self.menu[item] * qty:.2f}" for item, qty in self.order.items()])
        bill_summary += f"\n\nSubtotal: ${subtotal:.2f}\nTax (5%): ${tax:.2f}\nService Charge (10%): ${service_charge:.2f}\nTotal: ${total:.2f}"
        
        self.bill_text.delete("1.0", tk.END)
        self.bill_text.insert(tk.END, bill_summary)
        self.order.clear()

if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantGUI(root)
    root.mainloop()

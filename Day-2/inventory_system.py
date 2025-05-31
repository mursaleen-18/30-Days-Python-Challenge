import json
import os
from datetime import datetime

class InventorySystem:
    def __init__(self):
        self.inventory = {}
        self.history = []  # Track inventory changes
        self.load_inventory()  # Load existing inventory on startup

    def add_item(self, item_name, quantity):
        """Add an item to the inventory or update its quantity if it exists."""
        if quantity <= 0:
            print("Error: Quantity must be greater than 0")
            return False
        
        if item_name in self.inventory:
            self.inventory[item_name] += quantity
            self.log_change("ADD", item_name, quantity, self.inventory[item_name])
            print(f"Updated {item_name} quantity. New quantity: {self.inventory[item_name]}")
        else:
            self.inventory[item_name] = quantity
            self.log_change("ADD", item_name, quantity, quantity)
            print(f"Added {item_name} to inventory with quantity: {quantity}")
        self.save_inventory()
        return True

    def remove_item(self, item_name, quantity):
        """Remove a specified quantity of an item from the inventory."""
        if item_name not in self.inventory:
            print(f"Error: {item_name} not found in inventory")
            return False
        
        if quantity <= 0:
            print("Error: Quantity must be greater than 0")
            return False
        
        if self.inventory[item_name] < quantity:
            print(f"Error: Not enough {item_name} in inventory")
            return False
        
        self.inventory[item_name] -= quantity
        self.log_change("REMOVE", item_name, quantity, self.inventory[item_name])
        print(f"Removed {quantity} {item_name}. Remaining quantity: {self.inventory[item_name]}")
        
        if self.inventory[item_name] == 0:
            del self.inventory[item_name]
            print(f"{item_name} removed from inventory")
        
        self.save_inventory()
        return True

    def update_quantity(self, item_name, new_quantity):
        """Update the quantity of an existing item."""
        if item_name not in self.inventory:
            print(f"Error: {item_name} not found in inventory")
            return False
        
        if new_quantity < 0:
            print("Error: Quantity cannot be negative")
            return False
        
        old_quantity = self.inventory[item_name]
        self.inventory[item_name] = new_quantity
        self.log_change("UPDATE", item_name, new_quantity - old_quantity, new_quantity)
        print(f"Updated {item_name} quantity to: {new_quantity}")
        self.save_inventory()
        return True

    def display_inventory(self):
        """Display all items in the inventory."""
        if not self.inventory:
            print("Inventory is empty")
            return
        
        print("\nCurrent Inventory:")
        print("-" * 50)
        print(f"{'Item Name':<20} {'Quantity':<10} {'Last Updated':<20}")
        print("-" * 50)
        for item, quantity in self.inventory.items():
            last_update = self.get_last_update(item)
            print(f"{item:<20} {quantity:<10} {last_update:<20}")
        print("-" * 50)

    def log_change(self, action, item_name, quantity_change, new_quantity):
        """Log inventory changes with timestamp."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.history.append({
            "timestamp": timestamp,
            "action": action,
            "item": item_name,
            "quantity_change": quantity_change,
            "new_quantity": new_quantity
        })

    def get_last_update(self, item_name):
        """Get the last update time for an item."""
        for entry in reversed(self.history):
            if entry["item"] == item_name:
                return entry["timestamp"]
        return "Never"

    def save_inventory(self):
        """Save inventory data to a JSON file."""
        data = {
            "inventory": self.inventory,
            "history": self.history
        }
        with open("inventory_data.json", "w") as f:
            json.dump(data, f, indent=4)

    def load_inventory(self):
        """Load inventory data from JSON file if it exists."""
        if os.path.exists("inventory_data.json"):
            try:
                with open("inventory_data.json", "r") as f:
                    data = json.load(f)
                    self.inventory = data.get("inventory", {})
                    self.history = data.get("history", [])
                print("Inventory data loaded successfully.")
            except Exception as e:
                print(f"Error loading inventory data: {e}")
                self.inventory = {}
                self.history = []

    def search_item(self, search_term):
        """Search for items in the inventory."""
        found_items = {}
        search_term = search_term.lower()
        for item, quantity in self.inventory.items():
            if search_term in item.lower():
                found_items[item] = quantity
        
        if found_items:
            print("\nSearch Results:")
            print("-" * 30)
            for item, quantity in found_items.items():
                print(f"{item}: {quantity}")
            print("-" * 30)
        else:
            print(f"No items found matching '{search_term}'")

    def display_history(self, limit=10):
        """Display recent inventory changes."""
        if not self.history:
            print("No history available")
            return
        
        print("\nRecent Inventory Changes:")
        print("-" * 70)
        print(f"{'Timestamp':<20} {'Action':<10} {'Item':<15} {'Change':<10} {'New Qty':<10}")
        print("-" * 70)
        
        for entry in self.history[-limit:]:
            print(f"{entry['timestamp']:<20} {entry['action']:<10} {entry['item']:<15} "
                  f"{entry['quantity_change']:<10} {entry['new_quantity']:<10}")
        print("-" * 70)

def main_menu():
    """Display the main menu and handle user input."""
    inventory = InventorySystem()
    
    while True:
        print("\n=== Inventory Management System ===")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Update Quantity")
        print("4. Display Inventory")
        print("5. Search Items")
        print("6. View History")
        print("7. Exit")
        
        choice = input("\nEnter your choice (1-7): ")
        
        if choice == "1":
            item = input("Enter item name: ")
            try:
                quantity = int(input("Enter quantity: "))
                inventory.add_item(item, quantity)
            except ValueError:
                print("Error: Please enter a valid number for quantity")
        
        elif choice == "2":
            item = input("Enter item name: ")
            try:
                quantity = int(input("Enter quantity to remove: "))
                inventory.remove_item(item, quantity)
            except ValueError:
                print("Error: Please enter a valid number for quantity")
        
        elif choice == "3":
            item = input("Enter item name: ")
            try:
                quantity = int(input("Enter new quantity: "))
                inventory.update_quantity(item, quantity)
            except ValueError:
                print("Error: Please enter a valid number for quantity")
        
        elif choice == "4":
            inventory.display_inventory()
        
        elif choice == "5":
            search_term = input("Enter search term: ")
            inventory.search_item(search_term)
        
        elif choice == "6":
            try:
                limit = int(input("Enter number of recent changes to display (default 10): ") or "10")
                inventory.display_history(limit)
            except ValueError:
                print("Error: Please enter a valid number")
                inventory.display_history()
        
        elif choice == "7":
            print("Thank you for using the Inventory Management System!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu() 
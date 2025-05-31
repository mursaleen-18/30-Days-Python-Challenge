class InventorySystem:
    def __init__(self):
        self.inventory = {}  # Dictionary to store items and their quantities

    def add_item(self, item_name, quantity):
        """Add an item to the inventory or update its quantity if it exists."""
        if quantity <= 0:
            print("Error: Quantity must be greater than 0")
            return
        
        if item_name in self.inventory:
            self.inventory[item_name] += quantity
            print(f"Updated {item_name} quantity. New quantity: {self.inventory[item_name]}")
        else:
            self.inventory[item_name] = quantity
            print(f"Added {item_name} to inventory with quantity: {quantity}")

    def remove_item(self, item_name, quantity):
        """Remove a specified quantity of an item from the inventory."""
        if item_name not in self.inventory:
            print(f"Error: {item_name} not found in inventory")
            return
        
        if quantity <= 0:
            print("Error: Quantity must be greater than 0")
            return
        
        if self.inventory[item_name] < quantity:
            print(f"Error: Not enough {item_name} in inventory")
            return
        
        self.inventory[item_name] -= quantity
        print(f"Removed {quantity} {item_name}. Remaining quantity: {self.inventory[item_name]}")
        
        if self.inventory[item_name] == 0:
            del self.inventory[item_name]
            print(f"{item_name} removed from inventory")

    def update_quantity(self, item_name, new_quantity):
        """Update the quantity of an existing item."""
        if item_name not in self.inventory:
            print(f"Error: {item_name} not found in inventory")
            return
        
        if new_quantity < 0:
            print("Error: Quantity cannot be negative")
            return
        
        self.inventory[item_name] = new_quantity
        print(f"Updated {item_name} quantity to: {new_quantity}")

    def display_inventory(self):
        """Display all items in the inventory."""
        if not self.inventory:
            print("Inventory is empty")
            return
        
        print("\nCurrent Inventory:")
        print("-" * 30)
        for item, quantity in self.inventory.items():
            print(f"{item}: {quantity}")
        print("-" * 30)

# Example usage
if __name__ == "__main__":
    # Create an instance of the inventory system
    inventory = InventorySystem()
    
    # Add some items
    inventory.add_item("Laptop", 5)
    inventory.add_item("Mouse", 10)
    inventory.add_item("Keyboard", 8)
    
    # Display the inventory
    inventory.display_inventory()
    
    # Update quantities
    inventory.update_quantity("Laptop", 3)
    inventory.add_item("Mouse", 5)  # Add more mice
    
    # Remove some items
    inventory.remove_item("Keyboard", 3)
    
    # Display the final inventory
    inventory.display_inventory() 
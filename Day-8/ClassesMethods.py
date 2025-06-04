class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Information: {self.year} {self.brand} {self.model}")


# Creating objects
car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Tesla", "Model 3", 2024)

# Displaying car information
car1.display_info()
car2.display_info()

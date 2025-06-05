# Base class
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def drive(self):
        return f"Driving a {self.make} {self.model}"

# Subclass
class ElectricCar(Car):
    def __init__(self, make, model, battery_capacity):
        super().__init__(make, model)
        self.battery_capacity = battery_capacity  # in kWh

    # Polymorphic method override
    def drive(self):
        return f"Driving an electric {self.make} {self.model} with {self.battery_capacity}kWh battery"

# Example usage
car = Car("Toyota", "Corolla")
electric_car = ElectricCar("Tesla", "Model 3", 75)

print(car.drive())           # Output: Driving a Toyota Corolla
print(electric_car.drive())  # Output: Driving an electric Tesla Model 3 with 75kWh battery

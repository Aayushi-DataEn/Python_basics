class Car:

    total_car = 0

    def __init__(self, brand, model):
        self._brand = brand
        self.model = model 
    

# 4 encapsulation = "" make situation private . in class everyone get access unlike outside class
    def get_brand(self):
        return self._brand + " !"

    def full_name(self):
        return f"{self.brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"

# 3 solution inheritance
class Electric_Car(Car):
    def __init__(self, brand, model, battery_size):
        # self.brand = brand
        # self modell = model
        # super().__init__ it inherits access from above 
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Petrol or Diesel"
    

my_tesla = Electric_Car("Tesla", "Model S", "85kwh")
# print(my_tesla.get_brand)
print(my_tesla.fuel_type())

safari = Car("Tata", "Safari")
print(safari.fuel_type)

print(Car.total_car
)

# class name always start from Capital letter.
# __init__ aka constructor 


# my_car = Car("Toyota", "Corolla")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())

# my_new_car = Car("Tata", "Safari")
# print(my_new_car.brand)
# print(my_new_car.model)
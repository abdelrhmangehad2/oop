
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

   
    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}")

   
    def start_engine(self):
        print(f"The {self.model} engine is now running!")


my_car = Car("honda", "Civic", 2023)


my_car.display_info()
my_car.start_engine()

another_car = Car("bmw", "Model c", 2021)
another_car.display_info()
another_car.start_engine()

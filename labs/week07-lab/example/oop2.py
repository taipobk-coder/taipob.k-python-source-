class Vehicle:
    def __init__(self,make,model):
        self.make = make
        self.model = model

    def detail(self):
        print(f"make:{self.make}")
        print(f"model:{self.model}")

class Car(Vehicle):
    def __init__(self,make,model,year):
        super().__init__(make,model)
        self.year = year

    def detail(self):
        print(f"make:{self.make}")
        print(f"model:{self.model}")
        print(f"year:{self.year}")


car1 = Car("Honda","civic",2025)
print(car1.detail())

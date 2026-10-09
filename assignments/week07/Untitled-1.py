class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.pi = 3.14159

    # Method to get the area
    def get_area(self):
        return self.pi * (self.radius**2)

    # Method to get the perimeter
    def get_perimeter(self):
        return 2 * self.pi * self.radius

myCircle = Circle (10)
print(myCircle.get_area())       
print(myCircle.get_perimeter()) 
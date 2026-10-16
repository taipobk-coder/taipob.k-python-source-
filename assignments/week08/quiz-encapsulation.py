"""
Write a Python class Rectangle with:

Private attributes for length and width
Methods to calculate area (getArea()) and perimeter getPerimeter())
A method to check if it's a square (isSquare())

"""

class rectangle:
    def __init__(self,length,width):
        self.__length = length
        self.__width = width

    def getArea(self):
        return f"Area of {self.__width} width and {self.__length} length = {self.__width * self.__length}"

    def getParimeter(self):
       return f"Perimeter of width {self.__width} and length {self.__length} = {2 * (self.__width + self.__length)}"

    def isSquare(self):
        return self.__width == self.__length

myrectangle = rectangle(5,10)

print(myrectangle.getArea())

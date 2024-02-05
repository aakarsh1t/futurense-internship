class Rectangle:
    def __init__(self, length, width):

        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
rectangle = Rectangle(length,width)

# Print the area and perimeter of the rectangle
print("Area of the rectangle:", rectangle.area())
print("Perimeter of the rectangle:", rectangle.perimeter())
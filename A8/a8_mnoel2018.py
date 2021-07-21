'''Makenson Noel 
   A8: 2D shapes'''

import math

#variables 
PI = 3.14
def error():
    print("ERROR")

class Shape:
    pass
        
class Circle(Shape):
    def __init__(self, r):
        self.radius = r

    def area(self):
        return (PI * (self.radius ** 2))
  
    def perimeter(self):
        return (2 * PI * self.radius)

class Polygon(Circle):
    pass

class Triangle(Polygon):

    def __init__(self, a, b, c):
        self.side_one = a
        self.side_two = b
        self.side_three = c

    def area(self):
        s = (self.side_one + self.side_two + self.side_three) / 2

        if  self.side_one + self.side_two <= self.side_three or self.side_one + self.side_three <= self.side_two or self.side_two + self.side_three <= self.side_one:
            return error()

        else:
            return ((s*(s-self.side_one)*(s-self.side_two)*(s-self.side_three)) **0.5)

    def perimeter(self):
        if  self.side_one + self.side_two <= self.side_three or self.side_one + self.side_three <= self.side_two or self.side_two + self.side_three <= self.side_one:
            return error()
    
        else:
            return (self.side_one + self.side_two + self.side_three)

class Rectangle(Polygon):
    def __init__(self, w, h):
        self.weight = w
        self.height = h

    def area(self):
        if self.weight < 0 and self.height < 0:
            return error()
        return (self.weight + self.height)

    def perimeter(self):
        if self.weight < 0 and self.height < 0:
            return error()
        return (2 * (self.weight + self.height))
      
class Pentagon(Polygon):
    def __init__(self, r):
        self.radius = r

    def area(self):
        return (math.sqrt(5 * (5 + 2 * (math.sqrt(5)))) * self.radius * self.radius) / 4 

    def perimeter(self):
        return ((math.sqrt(5 * (5 + 2 * (math.sqrt(5)))) * self.radius * self.radius) / 4 ) * 5

class Hexagon(Polygon):
    def __init__(self, r):
        self.radius = r

    def area(self):
        return (( 3 * math.sqrt(3) * (self.radius * self.radius)) / 2)

    def perimeter(self):
        return ((( 3 * math.sqrt(3) * (self.radius * self.radius)) / 2) * 6)
        
# created a circle of radius = 2    
my_circle = Circle(2) 

# attempted to create a triangle with "incorrect" values
# should produce error message
my_triangle = Triangle(3, 1.7, 4.9) 

# created a triangle passing the length of each side
my_triangle = Triangle(3, 7, 4.6) 

# created a rectangle of sides 3 and 4.5
my_rectangle = Rectangle(3, 4.5)

# created a pentagon with sides of equal length
my_pentagon = Pentagon(3) 

# creates a hexagon with sides of equal length
my_hexagon = Hexagon(3) 

############################################

## Print area and perimeter for each variable
print("\n\nResults: \n\n")

print("Area of circle:",my_circle.area())
print("Perimeter of circle:", my_circle.perimeter(), "\n")

print("Area of triangle: ", my_triangle.area())
print("Perimeter of triangle: ", my_triangle.perimeter(), "\n")

print("Area of rectangle:", my_rectangle.area())
print("Perimeter of rectangle: ", my_rectangle.perimeter(), "\n")

print("Area of pentagon:", my_pentagon.area())
print("Perimeter of pentagon: ", my_pentagon.perimeter(), "\n")

print("Area of hexagon:", my_hexagon.area())
print("Perimeter of hexagon:", my_hexagon.perimeter(), "\n")
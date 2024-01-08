'''Makenson Noel
   A7: Color addition and subtraction
   '''
colors = { "red" : (1,0,0), 
            "green" : (0,1,0),
            "blue" : (0,0,1),
            "cyan" : (0, 1, 1),
            "magenta" : (1,0,1),
            "yellow" : (1,1,0),
            "black" : (0,0,0),
            "white" : (1,1,1) }

class Color(object):
  def __init__(self, r, g, b):
      self.r = self.checkRange(r)
      self.g = self.checkRange(g)
      self.b = self.checkRange(b)

  def checkRange(self,color_component):
    if color_component < 0:
      return 0

    elif color_component > 1:
      return 1

    else:
      return color_component

  def __add__(self, x):
    return Color(self.r + x.r, self.g + x.g, self.b + x.b)

  def __sub__(self, x):
    return Color(self.r - x.r, self.g - x.g ,self.b - x.b)

  def __str__(self):
    return "({}, {}, {})".format(self.r , self.g , self.b)

  def __repr__(self):
    return self.__str__()
    
# Test Code
red = Color(1,0,0)
green = Color (0,1,0)
blue = Color (0,0,1)
cyan = Color (0, 1, 1)
magenta = Color (1,0,1)
yellow = Color (1,1,0)
black = Color (0,0,0)
white = Color (1,1,1)

print("\n\na simple program for performing addition and subtraction using colors.\n\n")

print("Enter two colors by name or (r,g,b) values\n")

print("\nValid names are: \nred (1, 0, 0) \ngreen (0, 1, 0) \nblue (0, 0, 1) \ncyan (0, 1, 1) \nmagenta (1, 0, 1) \nyellow (1, 1, 0) \nblack (0, 0, 0) \nwhite (1, 1, 1)\n\n")

color_one = input("Enter Color 1: ")
#cases for first input

if color_one  == "red": color_one = red
elif color_one == "green": color_one = green
elif color_one == "blue": color_one = blue
elif color_one == "cyan": color_one = cyan
elif color_one  == "magenta": color_one = magenta
elif color_one == "yellow": color_one = yellow
elif color_one == "black": color_one = black
elif color_one  == "white": color_one = white
else : print("Error")

color_two = input("Enter Color 2: ")

#cases for second input
if color_two == "red": color_two = red
elif color_two == "green": color_two = green
elif color_two == "blue": color_two = blue
elif color_two == "cyan": color_two = cyan
elif color_two == "magenta": color_two = magenta
elif color_two == "yellow": color_two = yellow
elif color_two == "black": color_two = black
elif color_two == "white": color_two = white
else : print("Error")

c1 = color_one + color_two
c2 = color_one - color_two

print("Color 1 + Color 2 =", c1)
print("Color 1 - Color 2 =", c2)
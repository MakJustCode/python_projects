x = 50
y = 30

def swapper(x, z):
  #Takes in two values and temporarily swaps them.
  print("(Local) Before: x ", x, "and z =", z)
  t = x
  x = z
  z = t
  print("(Local) After: x =", x, "and z =", z) 
print("(Global) before call:", x, y)
swapper(x, y)
print("(Global) after call:", x, y)
#print("This won't work: ", z) #uncomment to see error 
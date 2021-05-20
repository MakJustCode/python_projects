"""Makenson I. Noel
   Develop With Mak
   PyGraphs"""

import math
from turtle import*


#Formula for a sphere
pi = 3.1415926535897931
r= 6.0
V= 4.0/3.0*pi* r**3

#function for the py graph 
def graph():
  
  color('blue')
  begin_fill()
  forward(300)
  right(V)
  end_fill() 

  color('red')
  begin_fill()
  forward(120)
  right(V)
  end_fill() 

  color('green')
  begin_fill()
  forward(120)
  right(V)
  end_fill() 

  color('yellow')
  begin_fill()
  forward(120)
  right(V)
  end_fill() 

#for the variable I in the range of 500, the program will lopp 500 times, by the sphere shall be complete 
for i in range(500):
  graph()


"""Makenson I. Noel
Develop With Mak
May 18 2021 

Created a program to generate the structure of a Haitian Flag"""

from turtle import *


def message():
  for i in range(1):

    #White part of Hatitian Flag
    color('white')
    begin_fill()
    forward(90)
    right(90)
    forward(90)
    right(90)
    forward(90)
    right(90)
    end_fill()

    #Red part of Hatitian Flag
    color('red')
    begin_fill()
    forward(45)
    left(90)
    forward(90)
    left(90)
    forward(90)
    left(90)
    forward(90)
    left(90)
    forward(45)
    right(90)
    forward(90)
    right(90)
    forward(45)
    right(90)
    forward(90)
    right(180)
    end_fill()

    color('red')
    forward(180)
    begin_fill()
    left(90)
    forward(90)
    left(90)
    forward(90)
    left(90)
    forward(90)
    end_fill()

    right(180)
    forward(90)

    #Blue part of Hatitian Flag
    color('blue')

    begin_fill()
    right(90)
    forward(90)
    left(90)
    forward(90)
    left(90)
    forward(270)

    left(90)
    forward(90)
    left(90)
    forward(90)
    left(90)
    forward(45)
    right(90)
    forward(90)
    right(90)
    end_fill()

    #Displaying function
message()

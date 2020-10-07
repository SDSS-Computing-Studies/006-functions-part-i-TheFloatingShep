#!python3
""" 
Create a function called hypotenuse()
Input is 2 float numbers and a boolean
If the boolean is True, then find the hypotenuse
If the boolean is False, then the larger number is the hypotenuse
Return the missing side
(2 points)
"""
import math
def hypotenuse(x,y,z):
    if z == True:
        return math.sqrt((x**2) + (y**2))
    else:
        if x >= y:
            X = x
            Y = y
        else:
            X = y
            Y = x
        return math.sqrt((X**2) - (Y**2))
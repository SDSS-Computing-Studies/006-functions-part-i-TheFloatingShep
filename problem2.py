#!python3

"""
Create a function called distance()
Input is 2 tuples, that each contain an (x,y) coordinate.
Return value is the distance between the (x,y) coordinates.
Note that the coordinates should be signed (positive or negative) floats
(2 points)
"""
import math
"""
The less confusing version:
def distance(t1,t2):
    x = t1[0] - t2[0]
    y = t1[1] - t2[1]
    z = math.sqrt((x**2) + (y**2))
    return z
"""
def distance(t1,t2):
    return math.sqrt(((t1[0] - t2[0])**2) + ((t1[1] - t2[1])**2))
'''
15. Write a Python program to get the volume of a sphere with radius 6.
'''

# volume of sphere 4/3 * pi * r^3
from math import pi

radius = float(input('Radius of sphere : '))

print('Volume : ', (4/3)* pi * (radius**3))

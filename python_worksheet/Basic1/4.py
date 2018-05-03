'''
4. Write a Python program which accepts the radius of a circle from the user and compute the area.
'''
# Formula for circle = pi*(r^2)

import math
r = float( input('r = ') )
print('Area = {}'.format(math.pi * r**2 ))

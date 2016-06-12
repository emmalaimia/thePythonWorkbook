# Take a radius r as the input
# Caluclate the area of a circle with radius r and the volume of a sphere with radius r

import math

radius = input("The radius is: ")

area = math.pi * math.pow(radius,2)

volume = (4/3) * math.pi * math.pow(radius,3)

print("The radius of a circle with radius %r is %r and the voume of a sphere with radius %r is %r" % (radius, area, radius, volume))



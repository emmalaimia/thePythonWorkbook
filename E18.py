
# Calculate the area of a cylinder

import math

radius = input("What is the radius of the cylinder in centimeters: ")

height = input("What is the height of the cylinder in centimeters: ")

volume = radius * math.pi * math.pow(radius, 2) * height

print("The volume of the cylinnder is %r" % (round(volume,1)))


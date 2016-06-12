
# Calculate and display the area of a polygon with length of side is s and number of sides is n

from math import tan, pi

n = int(input("How many sides does the polygon have?: "))

s = float(input("What is the length of each side in centimeters?: "))

area = round(((n*s**2)/(4*tan(pi/n))),2)

print("The area of the polygon is %r square centimeters" % (area))

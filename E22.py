
# Caluclate the area of a triangle with sides s1, s2 and s3

import math

s1 = input("Enter the length of the first side of the triangle in centimeters: ")

s2 = input("And the second side: ")

s3 = input("And the third side: ")

s = (s1 +s2 + s3)/2

area = math.sqrt(s*(s-s1)*(s - s2)*(s - s3))

print("The area of the triangle is %r square centimeters" % (area))

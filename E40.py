

# Classify a triangle

side1 = float(input("Enter length of first side of the triangle: "))

side2 = float(input("Second side: "))

side3 = float(input("Third side: "))

if side1==side2 and side2==side3:
	classification = 'equilateral'

elif side1==side2 or side2==side3:
	classification = 'isosceles'

else:
	classification = 'scalene'

print("The triangle is %r" % classification)

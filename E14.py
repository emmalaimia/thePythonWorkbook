
# Read in the number of feet and inches and return number of centimetres

# One foot is 12 inches. One inch is 2.54 centimetres

print("Please enter your height in feet and inches")

feet = int(input("Feet:"))

inches = int(input("Inches:"))

centimetres = feet * 12 * 2.54 + inches * 2.54

print ("Your height is %r centimetres" % centimetres)


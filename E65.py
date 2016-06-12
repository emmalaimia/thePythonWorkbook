# Compute the Perimeter of a Polygon

# Let the user read in x and y coordinates and add up the distances

from math import sqrt, pow

# Function that tests if a string can be converted to a float
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


#First input the first two coordinates
x = input("Enter the x part of the coordinate: ")

# Output an error and ask for new inputs if the user only inputs a y or an x coordinate or if they are not numbers
while str(x) == '' or is_number(x)==False:
	print("Warning: you have not input a numerate x coordinate. Input a number.")
	x = input("Enter the x part of the coordinate: ")

y = input("Enter the y part of the coordinate: ")

# Output an error and ask for new inputs if the user only inputs a y or an x coordinate or if they are not numbers
while str(y) == '' or is_number(y)==False:
	print("Warning: you have not input a numerate y coordinate. Input a number.")
	y = input("Enter the y part of the coordinate: ")

# Convert to numbers

x,y = float(x),float(y)

# Set initial distance to zero

total_distance = 0

# Save these coordinates as the starting point

start_x, start_y = x,y

#Cumulatively add up the distances of the remaining coordinates
while str(x) != '' and str(y) != '':
	new_x = input("Enter the x part of the coordinate: (blank to quit): ")
	if str(new_x) == '':
		break
	elif is_number(new_x)==False:
		print("Warning: you have not input a numerate x coordinate. Input a number.")
		new_x = input("Enter the x part of the coordinate: (blank to quit): ")

	new_y = input("Enter the y part of the coordinate: ")
	if is_number(new_y)==False:
		print("Warning: you have not input a numerate y coordinate. Input a number.")
		new_y = input("Enter the y part of the coordinate: ")

	new_x,new_y = float(new_x),float(new_y)	

	distance = sqrt(pow(x-new_x,2) + pow(y-new_y,2))

	total_distance = total_distance + distance

	x,y = new_x,new_y

# Calculate the distance to the last provided point and the starting point

return_distance = sqrt(pow(x-start_x,2) + pow(y-start_y,2))

# Add it to the total

total_distance = total_distance + return_distance

print("The perimiter of the polygon is %r" % total_distance)


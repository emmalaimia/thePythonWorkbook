 
 # Ask the user to enter the widrh and length of a room
 # Compute and display the area of the room 
 # The length and width will be entered as floating point numbers
 # Include units in your prompt

print("Please enter the width and length of the room so I can calculate the area")

width = float(input("Width in metres:"))

length = float(input("Length in metres:"))

area = width * length

print("The area of the room is %r square metres" % area)
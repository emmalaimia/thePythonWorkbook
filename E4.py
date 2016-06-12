#Create a program that reads the length and width of a farmers field from the user
#in feet. Display the area of the field in acres
#There are 43560 square feet in an acres

print("What is the length and width of the field?")

length = float(input("Length in feet: "))

width = float(input("Width in feet: "))

acre_area = (length * width) / 43560

print("The field is ", acre_area, " acres big!")




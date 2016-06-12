

#Let the user enter prices and then a blank line to finish the total
#Display the total and the total due if paying with cash, rounded to the nearest 5 cents

print("Enter the price of all products followed by a blank line")

value = input()

total = 0

while str(value) != '':
	
	total = total + float(value)

	value = input()

print("The total is %r" % (total))	

total_pennies = total * 100

remainder_nickels = total_pennies % 5

if remainder_nickels < 2.5:

	integer_pennies = total_pennies - remainder_nickels

else:

	integer_pennies = total_pennies + 5 - remainder_nickels

integer_dollars = int(integer_pennies/100)






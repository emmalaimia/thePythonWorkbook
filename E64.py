

#Let the user enter prices and then a blank line to finish the total
#Display the total and the total due if paying with cash, rounded to the nearest 5 cents

print("Enter the price of all products followed by a blank line")

value = input()

total = 0

while str(value) != '':
	
	total = total + float(value)

	value = input()

print("The total is $%r" % (total))	

total_pennies = total * 100

#print("Total Pennies: %r" % (total_pennies))

remainder_pennies = total_pennies % 5

#print("Remainder Nickels: %r" % (remainder_nickels))

if remainder_pennies < 2.5:

	integer_pennies = total_pennies - remainder_pennies

else:

	integer_pennies = total_pennies + 5 - remainder_pennies

integer_dollars = int(integer_pennies/100)

integer_nickels = int((integer_pennies -100*integer_dollars)/5)

total_cash = integer_dollars + integer_nickels*5/100

print("In cash that is $%.02f" % (total_cash))




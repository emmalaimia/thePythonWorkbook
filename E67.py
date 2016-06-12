
# Calculate the total admission cost for a group of people of differnt ages to the zoo

# Dictionary with prices for different groups
prices = {'Babies': 0, 'Children':14, 'Adults':23, 'Seniors':18}

count = 1

age = input("Input the age of person %r: " % count)

total_cost = 0

while str(age)!='':

	age = int(age)

	if age <=2:
		category = 'Babies'

	elif age<=12:
		category = 'Children'

	elif age<65:
		category = 'Adults'

	else:
		category = 'Seniors'

	cost = prices[category]

	total_cost = total_cost + cost

	count = count + 1

	age = input("Input the age of person %r (blank to quit): " % count)

print("The total admission will be $%.2f" % total_cost)
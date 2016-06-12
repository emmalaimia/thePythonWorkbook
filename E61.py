

# Let the user input as many values as they want and then calculate the average

print("Input all your values one by one. When you have entered all your values enter 0. Then the average will be calculated")

total = 0

count = 0 

value = -1

while value != 0:

	value = float(input("Input a value:"))

	if value !=0:

		total = total + value

		count = count + 1

if total == 0:

	average = 0

else: 

	average = total / count

print("The average of those numbers is %r" % (average))


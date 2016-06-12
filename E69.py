
# Approximate pi to 15 approximations


iterations = int(input("How many iterations should we use to approximate pi? "))

pi = 3

count=1

print(pi)

sign = 1

evenNumbers = 2

while count<iterations:

	pi = pi + 4 * sign / (evenNumbers * (evenNumbers+1) * (evenNumbers+2)) 

	print(pi)

	sign = sign*-1

	count = count+1

	evenNumbers = evenNumbers + 2



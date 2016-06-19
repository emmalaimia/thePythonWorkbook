# Write a program that implements Newton's method to compute and display the square root of a number

number = float(input("Input a number that you want the squre root of: "))

guess = number / 2

guess_squared = guess * guess

difference = abs(guess_squared - number)

while difference > 10E-12:

	guess = (guess + number/guess) / 2

	guess_squared

	guess_squared = guess * guess

	difference = abs(guess_squared - number)

print("The square root of %r is %r" % (number,guess))
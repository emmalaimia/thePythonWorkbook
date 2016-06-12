

# Write a program that reads a positive integer n from the user
# and then displays the sum of all the integers from 1 to n.
# The sum of the first n positive integers can be computed using the formula:
# sum = (n)(n+1)/2

n = int(input("Give me an integer please: "))

sum_to_n = int((n)*(n+1)/2)

print("The sum from 1 to %r is %r" % (n, sum_to_n))





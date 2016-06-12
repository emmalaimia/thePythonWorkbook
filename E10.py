
# Create a program that reads two integers from the user and displays:
# The sum
# The difference when the second is subtracted from the first
# The product of the two numbers
# The quotient when a is divided by b
# The remainder when a is divided by b
# The result of log10a
# The result of a^b

from math import log10

a = int(input("Give me an integer please: "))

b = int(input("And a second one: "))

print("The sum of %r and %r is %r" % (a,b,a+b))
print("The difference between of %r and %r is %r" % (a,b,a-b))
print("The product of %r and %r is %r" % (a,b,a*b))
print("The quotient of %r and %r is %.0f" % (a,b,a/b))


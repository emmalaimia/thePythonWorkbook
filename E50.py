
# Find the real roots of a quadratic equation

print("A quadratic equation has the form f(x) = ax2 + bx + c, where a, b and c are constants")

print("This program will give you the real roots of your equation")

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

discriminant = b**2 - 4 * a * c

if discriminant < 0:
	roots = 0

elif discriminant == 0:
	roots = 1

else:
	roots = 2


if roots == 0:
	print("There are no real roots to this equation")

elif roots == 1:
	root = - b / (2 * a)
	print("This equation has one real root and it is %r" % (root))

else:
	root1 = (-b + (discriminant**0.5)) / (2 * a)
	root2 = (-b - (discriminant**0.5)) / (2 * a)
	print("This equation has two real roots and they are %r and %r" % (root1,root2))


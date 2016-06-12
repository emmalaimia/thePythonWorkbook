
d = input("Enter a banknote denomination: ")

if d == 1:
	i = "George Washington"

elif d == 2:
	i = "Thomas Jefferson"

elif d == 5:
	i = "Abraham Lincoln"

elif d == 10:
	i = "Alexander Hamilton"

elif d == 20:
	i = "Andrew Jackson"

elif d == 50:
	i = "Ulysses S. Grant"

elif d == 100:
	i = "Benjamin Franklin"

else:
	i = "Unknown"

if i == "Unknown":
	print("There is no %r$ note" % (d))

else:
	print("%r is on the %r$ note" % (i,d))


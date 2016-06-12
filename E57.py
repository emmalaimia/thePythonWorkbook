

# Detrmine if a year is a leap year, it will be if:
# It is divisible by 400
# Of the remaining if it's divisible by 100 it's not a leap year
# Of the remaining years if it's divisible by 4 it is a leap year
# Remaining years are not leap years


year = int(input("Write any year: "))

leap = 'is not'

if year%400 == 0:
	leap = 'is'

else:
	if year%100 == 0:
		leap = 'is not'
	else:
		if year%4 == 0:
			leap = 'is'

print("%d %s a leap year" % (year, leap))
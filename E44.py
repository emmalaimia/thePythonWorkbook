
month = raw_input("Enter a month of the year (the complete name): ")

day = input("Enter the day of the month: ")

holiday = "No holiday"

if month == "January" and day == 1:
	holiday = "New years's day"

if month == "July" and day == 1:
	holiday = "Canada day"

if month == "December" and day == 25:
	holiday = "Christmas day"

if holiday == "No holiday":
	print("%r %r is not holiday" % (month, day))

else:
	print("%r %r is %r" % (month, day, holiday))




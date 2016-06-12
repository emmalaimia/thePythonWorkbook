

# Display the number of days the entered month has

month = raw_input("Enter the full name of a month: ").lower() 

if month=="january" or month=="march" or month=="may" or month=="july" or month=="august" or month=="october" or month=="december":
	print("%r has 31 days" % month)

elif month=="february":
	print("%r has 28 or 29 days depending on if it's a leap year or not" % month)

elif month=="april" or month=="june" or month=="september" or month=="november":
	print("%r has 30 days" % month)

else:
	print("%r is not a month" % month)



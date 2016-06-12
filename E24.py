
# Calculate number of seconds from days, hours, minutes and seconds

days = input("Number of days: ")

hours = input("Number of hours: ")

minutes = input("Number of minutes: ")

seconds = input("Number of seconds: ")

total_seconds = seconds + minutes*60 + hours*60*60 + days*24*60*60

print("That makes the total number of seconds %r" % total_seconds)
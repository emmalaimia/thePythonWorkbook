
# Read in an employees rating and output the preformance description and the raise

rating = float(input("Enter the rating for the employee (0.0, 0.4, 0.6 or more): "))

if rating == 0.0:
	meaning = 'Unacceptable performance'
	r = 2400 * rating

elif rating == 0.4:
	meaning = 'Acceptable performance'
	r = 2400 * rating

elif rating >= 0.6:
	meaning = 'Meritorious performance'
	r = 2400 * rating

else:
	meaning = 'Unavailable'


if meaning == 'Unavailable':
	print("That is not a valid rating")

else:
	print("That corresponds to %s and a raise of $%.2f" % (meaning,r))




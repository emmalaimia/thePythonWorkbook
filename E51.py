
# Take the letter grade and output the grade points

grade = raw_input("Input a valid letter grade: ")

grade = grade.upper()

points = -1

if grade == 'A+':
	points = 4.0

elif grade == 'A':
	points = 4.0

elif grade == 'A-':
	points = 3.7

elif grade == 'B+':
	points = 3.3

elif grade == 'B':
	points = 3.0

elif grade == 'B-':
	points = 2.7

elif grade == 'C+':
	points = 2.3

elif grade == 'C':
	points = 2.0

elif grade == 'C-':
	points = 1.7

elif grade == 'D+':
	points = 1.3

elif grade == 'D':
	points = 1.0

elif grade == 'F':
	points = 0

else:
	print("That is not a valid grade")

if points>=0:
	print("That grade corresponds to %r points" % (points))





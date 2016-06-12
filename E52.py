
# Take the the grade points and output the letter grade

points = float(input("Input number of grade points: "))

a_plus_points = 4.0
a_points = 4.0
a_minus_points = 3.7
b_plus_points = 3.3
b_points = 3.0
b_minus_points = 2.7
c_plus_points = 2.3
c_points = 2.0
c_minus_points = 1.7
d_plus_points = 1.3
d_points = 1.0
f_points = 0

if points < (d_points - ((d_points - f_points)/2)):
	grade = 'F'

elif points < (d_plus_points - ((d_plus_points - d_points)/2)):
	grade = 'D'

elif points < (c_minus_points - ((c_minus_points - d_plus_points)/2)):
	grade = 'D+'

elif points < (c_points - ((c_points - c_minus_points)/2)):
	grade = 'C-'

elif points < (c_plus_points - ((c_plus_points - c_points)/2)):
	grade = 'C'

elif points < (b_minus_points - ((b_minus_points - c_plus_points)/2)):
	grade = 'C+'

elif points < (b_points - ((b_points - b_minus_points)/2)):
	grade = 'B-'

elif points < (b_plus_points - ((b_plus_points - b_points)/2)):
	grade = 'B'

elif points < (a_minus_points - ((a_minus_points - b_plus_points)/2)):
	grade = 'B+'

elif points < (a_points - ((a_points - a_minus_points)/2)):
	grade = 'A-'

elif points < a_points:
	grade = 'A'

else:
	grade = 'A+'


print("The grade is %r" % (grade))






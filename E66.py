
# Create a grade to points dictionary

gradeToPoints = {'A+':4.0, 'A':4.0, 'A-':3.7, 'B+':3.3, 'B':3.0, 'B-':2.7, 
					'C+':2.3, 'C':2.0, 'C-':1.7, 'D+':1.3, 'D':1.0, 'F':0}


print(gradeToPoints['A'])

grade = str(input("Input a valid letter grade: "))

grade = grade.upper()

while grade not in gradeToPoints:
	print("That is not a valid grade. Try again.")
	grade = str(input("Input a valid letter grade: "))
	grade = grade.upper()

sumGrade = 0

count = 0

while grade != '':

	while grade not in gradeToPoints:
		print("That is not a valid grade. Try again or blank to quit")
		grade = str(input("Input a valid letter grade (or blank to quit): "))

	gradePoint = gradeToPoints[grade]

	sumGrade = sumGrade + gradePoint

	count = count + 1

	grade = str(input("Input a valid letter grade (or blank to quit): "))

	grade = grade.upper()

print("The grade point average is ", sumGrade/count)







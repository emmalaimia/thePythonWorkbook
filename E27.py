
# Calculate BMI

height = float(input("What is your height in metres?: "))

weight = float(input("What is your weight in kilograms?: "))

bmi = weight / (height*height)

print("Your BMI is %r" % bmi)

print("A healthy BMI is between 18.5 and 24.9")

if (bmi>=18.5 and bmi<=24.5):
	print("So you are healthy! Congratulations!")

elif bmi<18.5:
	print("So you're underweight.")

else:
	print("So you're overweight.")

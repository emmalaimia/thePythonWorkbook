
# Input the richter magnitude of an earthquake and output its description

m = float(input("Input the magnitude of the earthquake: "))

if m < 2.0:
	description = 'Micro'

elif m < 3.0:
	description = 'Very minor'

elif m < 4.0:
	description = 'Minor'

elif m < 5.0:
	description = 'Light'

elif m < 6.0:
	description = 'Moderate'

elif m < 7.0:
	description = 'Strong'

elif m < 8.0:
	description = 'Major'

elif m < 10.0:
	description = 'Great'

else:
	description = 'Meteroric'

print("That is a %r earthquake" % (description))
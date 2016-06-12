

# Take the wavelength and output the colour. Give error message if light is outside visible spectre

wave = int(input("Enter a wavelength in the visible spectre (between 380 and 750): "))

if wave < 380 or wave > 750:
	print("That is not in the correct range")

else:
	if wave<450:
		colour = 'Violet'
	elif wave <495:
		colour = 'Blue'
	elif wave < 570:
		colour = 'Green'
	elif wave < 590:
		colour = 'Yellow'
	elif wave < 620:
		colour = 'Orange'
	else:
		colour = 'Red'

	print("The colour is %s" % (colour))

	
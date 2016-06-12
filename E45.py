

x = raw_input("Enter a position on the chess board (for example a1): ")

column = x[0]

row = int(x[1:])

if column == 'a' or column == 'c' or column == 'e' or column == 'g':
	first_colour = 'Black'

else:
	first_colour = 'White'

if first_colour == 'Black':
	if row % 2 == 0:
		square_colour = 'White'
	else:
		square_colour = 'Black'

elif first_colour == 'White':
	if row % 2 == 0:
		square_colour = 'Black'
	else:
		square_colour = 'White'

print("The square is %r" % (square_colour))






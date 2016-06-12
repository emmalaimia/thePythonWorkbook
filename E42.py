

# Note to frequency

c4_freq =261.63

d4_freq=293.66

e4_freq=329.63

f4_freq=349.23

g4_freq=392.00

a4_freq=440.00

b4_freq=493.88

limit = 1

a = float(input("Input a frequency and I'll tell you which note it is (between 260.64 and 494.88)"))


if a > c4_freq - limit and a<=c4_freq+limit:
	note = 'C4'

elif a > d4_freq - limit and a<=d4_freq + limit:
	note = 'D4'

elif a > e4_freq - limit and a<=e4_freq + limit:
	note = 'E4'

elif a > f4_freq - limit and a<=f4_freq + limit:
	note = 'F4'

elif a > g4_freq - limit and a<=g4_freq + limit:
	note = 'G4'

elif a > a4_freq - limit and a<=a4_freq + limit:
	note = 'A4'

elif a > b4_freq - limit and a<=b4_freq + limit:
	note = 'B4'	

else:
	note = ''


print(note)





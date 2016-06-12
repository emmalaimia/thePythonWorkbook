

# Note to frequency

c4_freq =261.63

d4_freq=293.66

e4_freq=329.63

f4_freq=349.23

g4_freq=392.00

a4_freq=440.00

b4_freq=493.88

#Read the name of the note from the user
name = raw_input("Input a note: ")

# Store the note and its octave in two seperate variables

note = name[0]

octave = int(name[1])

# Get the frequency of the note assuming it's in the fourth octave

if note=='C':
	freq = c4_freq

elif note=='D':
	freq = f4_freq

elif note=='E':
	freq = e4_freq

elif note=='F':
	freq=f4_freq

elif note=='G':
	freq=g4_freq

elif note=='A':
	freq=a4_freq

elif note=='B':
	freq=b4_freq


# Adjust for different octaves

freq = freq / 2 ** (4 - octave)


print("The frequency of %r is %r" % (name, freq))







# Make a program that implements Ceasars cipher
# Each letter of the message the user puts in should be shifted a specified number of steps forward

#Import the lowercase alphabet
import string

alphabet = string.ascii_lowercase

steps = int(input("How many steps should the message be shifted? "))

message = str(input("Message to be endcoded: "))

message = message.lower()

new_string = ''

for letter in message:

	position = alphabet.index(letter)

	if position+steps<0:

		new_letter = alphabet[position+steps+len(alphabet)]

	elif position+steps<=len(alphabet):

		new_letter = alphabet[position+steps]

	elif position+steps>len(alphabet):

		new_letter = alphabet[position+steps-len(alphabet)]

	new_string = new_string + new_letter

print(new_string)


# Is a string a palindrome?

string = input("Input a string and I will tell you if it's a palindrome or not: ")

string_save = string

string = string.lower()

string = string.replace(" ","")

first_letter = string[0]

last_letter = string[-1]

if first_letter!=last_letter:

	comparison=False

else:

	comparison = True

string = string[1:len(string)-1]

while comparison==True and len(string)>0:

	first_letter = string[0]

	last_letter = string[-1]

	if first_letter!=last_letter:

		comparison=False

	else:

		comparison = True

	string = string[1:len(string)-1]


if comparison==True:

	print("%r is a palindrome!" % (string_save))

else:

	print("%r is not a palindrome!" % (string_save))
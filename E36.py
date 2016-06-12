
# Is a letter a vowel or a consonant

letter = raw_input("Input a letter of the alphabet: ")

if letter=="e" or letter=="i" or letter=="o" or letter=="u":
	print("%r is a vowel" % letter)

elif letter=="y":
	print("%r is sometimes a vowel and sometimes a consonant" % letter)

else:
	print("%r is a consonant" % letter)



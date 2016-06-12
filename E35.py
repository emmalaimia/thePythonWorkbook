
# Convert human years to dog years

human_years = input("Human years: ")

if human_years<2:
	dog_years = human_years*10.5

else:
	dog_years = 21 + (human_years - 2) * 4

print("That is %r dog years" % (dog_years))


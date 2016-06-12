
# Write a program that begins by reading a number of cents from the user as an integer
# Then your program should compute and display the denominations of the coins that
# should be used to give that amount of change to the shopper.
# The change should be given in as few coins as possible
# Use pennies, nickels, dimes, quarters, loonies and toonies

from math import floor

penny_value = 1
nickel_value = 5
dime_value = 10
quarter_value = 25
loonie_value = 100
toonie_value = 200

change = int(input("Please input the required change in cents: "))

whole_toonies = floor(change/toonie_value)

remaining_change = change - whole_toonies*toonie_value

whole_loonies = floor(remaining_change/loonie_value)

remaining_change = remaining_change - whole_loonies*loonie_value

whole_quarters = floor(remaining_change/quarter_value)

remaining_change = remaining_change - whole_quarters*quarter_value

whole_dimes = floor(remaining_change/dime_value)

remaining_change = remaining_change - whole_dimes*dime_value

whole_nickels = floor(remaining_change/nickel_value)

remaining_change = remaining_change - whole_nickels*nickel_value

whole_pennies = floor(remaining_change/penny_value)

if whole_toonies < 0:
	whole_toonies = 0

if whole_loonies < 0:
	whole_loonies = 0

if whole_quarters < 0:
	whole_quarters = 0

if whole_dimes < 0:
	whole_dimes = 0

if whole_nickels < 0:
	whole_nickels = 0

if whole_pennies < 0:
	whole_pennies = 0

print("Your change is %r Toonies, %r Loonies, %r Quarters, %r Dimes, %r Nickels and %r Pennies" % (whole_toonies, whole_loonies, whole_quarters, whole_dimes, whole_nickels, whole_pennies))












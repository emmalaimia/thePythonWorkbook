
# A newly opened savings account earns 4% interest per year
# The interest is paid at the end of the year and added to the balance
# Get the amount of money from the user
# Then calculate and display the amount in the account after 1, 2 and 3 years

amount = float(input("How much money is there in your account now? "))

interest_rate = 0.04

one_year = amount + amount * interest_rate

two_year = one_year + one_year * interest_rate

three_year = two_year + two_year * interest_rate

print("The amount after one year will be $%.2f, after two years it will be $%.2f and after three years it will be $%.2f." % (one_year, two_year, three_year))




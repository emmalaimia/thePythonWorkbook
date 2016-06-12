
# Begin by reading the cost of a meal from the user
# Then cpute the tax and the tip for the meal
# Set tax rate to 15%
# Set tip rate to 18% (before tax)
# The output should include the tax amount, the tip amount and the grand total
# Format the values to dollars with two decimal points

before_tax = float(input("What was the cost of your meal before tax? "))

tax_rate = 0.15
tip_rate = 0.18

tax_amount = before_tax * tax_rate
tip_amount = before_tax * tip_rate
after_tax = before_tax + tax_amount + tip_amount

print("The tax to pay is $%.2f." % tax_amount)
print("The tip to pay is $%.2f." % tip_amount)
print("The total cost of your meal is $%.2f." % after_tax)






# Drink containers holding one litre or less have a 0.1 depost and 
# containers with more have 0.25

# Read number of containers of each size from the user
# Compute and display the refund that will be received for returning them
# Format the output so that it includes a dollar sign and always displays two decimal figures

print("I am going to help you calculate the refund you will get from your containers")

less = float(input("How many containers 1 litres or less do you have? "))

more = float(input("How many containers bigger than 1 litres do you have? "))

refund = 0.1*less + 0.25*more

print("The refund is $%.2f." % refund)

#Another way of doing the same formatting:
print("The refund is", "${:.2f}.".format(refund))
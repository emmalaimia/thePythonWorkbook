

# 50 minutes and 50 texts for $15
# Extra minutes cost $0.25
# Extra texts cost $0.15
# Every bill has a $0.44 extra 911 charge and is subject to a 5% sales tax

# Display base charger, additional minutes and text charge (if any), the fee, tax and total
# Display with two decimal points and dollar signs

fixed_cost = 15

extra_minute_cost = 0.25

extra_text_cost = 0.15

charge_911 = 0.44

sales_tax_rate = 0.05

minute_allowance = 50

text_allowance = 50

minutes = float(input("Write the number of minutes used: "))

texts = float(input("write the number of texts sent: "))

extra_minutes = minutes - minute_allowance

extra_texts = texts - text_allowance

if extra_minutes<0:
	extra_minutes = 0

if extra_texts<0:
	extra_texts = 0

extra_minutes_total = extra_minutes * extra_minute_cost

extra_text_total = extra_texts * extra_text_cost

total_cost = (1+sales_tax_rate)*(fixed_cost + extra_minutes_total + extra_text_total + charge_911)

tax_cost = (sales_tax_rate)*(fixed_cost + extra_minutes_total + extra_text_total + charge_911)

if extra_minutes_total>0 and extra_text_total>0:
	print("The base charge is $%.2f" % fixed_cost)
	print("The charge for %d extra minutes is $%.2f" % (extra_minutes,extra_minutes_total))
	print("The charge for %d extra texts is $%.2f" % (extra_texts,extra_text_total))
	print("There is a $%.2f 911 charge and $%.2f sales tax" % (charge_911,tax_cost))
	print("In total the cost comes to $%.2f" % (total_cost))

elif extra_minutes_total>0:
	print("The base charge is $%.2f" % fixed_cost)
	print("The charge for %d extra minutes is $%.2f" % (extra_minutes,extra_minutes_total))
	print("There is a $%.2f 911 charge and $%.2f sales tax" % (charge_911,tax_cost))
	print("In total the cost comes to $%.2f" % (total_cost))

elif extra_text_total>0:
	print("The base charge is $%.2f" % fixed_cost)
	print("The charge for %d extra texts is $%.2f" % (extra_texts,extra_text_total))
	print("There is a $%.2f 911 charge and $%.2f sales tax" % (charge_911,tax_cost))
	print("In total the cost comes to $%.2f" % (total_cost))

else:
	print("The base charge is $%.2f" % fixed_cost)
	print("There is a $%.2f 911 charge and $%.2f sales tax" % (charge_911,tax_cost))
	print("In total the cost comes to $%.2f" % (total_cost))


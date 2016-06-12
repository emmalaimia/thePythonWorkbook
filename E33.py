

regular_price = 3.49

discounted_price = 3.49 * 0.4

amount = input("How many loaves:")

total_regular = regular_price * amount

total_discounted = discounted_price * amount

difference = total_regular - total_discounted

print("That would have been $%r but with the discount it's just $%r. So you save $%r" \
	% (round(total_regular,2), round(total_discounted,2), round(difference,2)))


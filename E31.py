
# Read four figures from the user and output the sum of the figures

number = str(int(input("Please input a four digit number; so any number between 1000 and 9999: ")))

sum_of_numbers = int(number[0])+int(number[1])+int(number[2])+int(number[3])

print("The sum of those numbers is %r" % sum_of_numbers)

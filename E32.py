

number = str(int(input("Input a number with three digits; any number between 100 and 999:")))

a = int(number[0])

b = int(number[1])

c = int(number[2])

first = min(a,b,c)

third = max(a,b,c)

second = (a+b+c) - (first + third)

print(first, second, third)


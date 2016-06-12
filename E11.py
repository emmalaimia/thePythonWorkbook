#In the United States, fuel efficiency for vehicles is normally expressed in 
#miles-per-Gallon (MPG).
#In Canada, fuel efficiency is normally expressed in 
#litres-per-hundred kilometres (L/100km).
#Use your research skills to determine how to convert from MPG to L/100km.
#Then create a program that reads a value from the user in American units
#and displays the equivalent fuel efficiency in Canadian units

#1 gallon is 3.78541 litres
#1 mile is 1.609344 km
#So 1 mile is 0.01609344 hundreth km

input_efficiency = float(input("Please input the fuel efficiency in MPG: "))

output_efficiency = input_efficiency * 3.78541 / 0.01609344

print("The fuel efficiency is %r L/100km" % output_efficiency)



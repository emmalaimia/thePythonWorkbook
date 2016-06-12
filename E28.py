
# Calculate the wind chill

from math import pow

temp = float(input("What is the temperature in Celcius?: "))

wind_speed = float(input("What is the wind speed in kilometers per hour?: "))

wind_chill = 13.12 + 0.6215*temp - 11.37 * pow(wind_speed, 0.16) + 0.3965 * pow(temp,0.16)

if (temp<=10.0 and wind_speed>=4.8):

	print("The wind chill is %r" % int(wind_chill))

if temp>10:

	print("The wind chill index is not valid for temparetures greater than 10 degrees")

if wind_speed<4.8:

	print("The wind chill index is not valid for wind speeds below 4.8")

	



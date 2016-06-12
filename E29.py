
# Convert a celcius value to a fahrenheit or kelvin

celcius_value = float(input("Input a temperature in Celcius: "))

fahrenheit_value = 1.8 * celcius_value + 32

kelvin_value = celcius_value + 273.15

print("That is equivalent to %r Fahrenhit or %r Kelvin" % (round(fahrenheit_value,1), round(kelvin_value,1)))


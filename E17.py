# Take a mass of water and a number of degrees as input
# Calculate the energy required to heat the water by this many degrees

mass_water = input("Grams of water: ")

number_degrees = input("Number of degrees: ")

energy_required = mass_water * number_degrees * 4.186

print("The energy required to heat %r grams of water by %r degrees is %r joules" % (mass_water, number_degrees, energy_required))

energy_required_kilowatt = energy_required * 0.0000002778

print("Assume that a cup of coffee is 250 ml and that the temperature of tap water is 7 degrees")

print("Also assume that energy costs 8.9 cents per kilowatt-hour")


print("Then it would cost %r cents to boil a cup of coffee" % (250 * 93 * 0.0000002778 * 8.9))

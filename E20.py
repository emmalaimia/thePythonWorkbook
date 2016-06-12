

pressure = input("Pressure: ")

volume = input("Volume: ")

temperature = input("Temperature: ") + 273.15

print("Then number of moles is %r moles" % (round(pressure*volume/(temperature*8.314),0)))




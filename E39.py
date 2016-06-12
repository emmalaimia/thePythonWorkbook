
jackhammer = 130

gas_lawnmower = 106

alarm_clock = 70

quiet_room = 40

decibel = input("What is the decibel level?: ")

if decibel<quiet_room:
	print("That's quieter than a quiet room")

elif decibel==quiet_room:
	print("That's like a quiet room")

elif decibel<alarm_clock:
	print("That's somewhere between a quiet room and an alarm clock")

elif decibel==alarm_clock:
	print("That's like an alarm clock")

elif decibel<gas_lawnmower:
	print("That's somewhere between an alarm clock and a gas lawnmower")

elif decibel==gas_lawnmower:
	print("That's like a gas lawnmover")

elif decibel<jackhammer:
	print("That's somewhere between a gas lawnmover and a jackhammer")

elif decibel==jackhammer:
	print("That's like a jackhammer")

else:
	print("That's louder than a jackhammer!")

	





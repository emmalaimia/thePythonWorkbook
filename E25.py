
#Take a total number of seconds and display D:HH:MM:SS

from math import floor

remaining_seconds = int(input("Total number of seconds: "))

days = int(floor(remaining_seconds/(24*60*60)))

if days>0:

	remaining_seconds = int(remaining_seconds % (days*(24*60*60)))

hours = int(floor(remaining_seconds/(60*60)))

if hours>0:

	remaining_seconds = int(remaining_seconds % (hours*(60*60)))

minutes = int(floor(remaining_seconds/60))

if minutes>0:

	remaining_seconds = int(remaining_seconds % (minutes*60))

seconds = remaining_seconds

print("The equivalent duration is %d:%02d:%02d:%02d." % (days, hours, minutes, seconds))



# Enter a year and output the Chinese Zodiak of that year

year = int(input("Enter a year: "))

year_diff = year - 2000

if (year - 2000) % 12 == 0:
	zodiak = 'Dragon'

if (year - 2001) % 12 == 0:
	zodiak = 'Snake'

if (year - 2002) % 12 == 0:
	zodiak = 'Horse'

if (year - 2003) % 12 == 0:
	zodiak = 'Sheep'

if (year - 2004) % 12 == 0:
	zodiak = 'Monkey'

if (year - 2005) % 12 == 0:
	zodiak = 'Rooster'

if (year - 2006) % 12 == 0:
	zodiak = 'Dog'

if (year - 2007) % 12 == 0:
	zodiak = 'Pig'

if (year - 2008) % 12 == 0:
	zodiak = 'Rat'

if (year - 2009) % 12 == 0:
	zodiak = 'Ox'

if (year - 2010) % 12 == 0:
	zodiak = 'Tiger'

if (year - 2011) % 12 == 0:
	zodiak = 'Hare'

print("The zodiak of that year is %r" % (zodiak))















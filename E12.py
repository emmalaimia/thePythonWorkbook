
#Create a program that allows the user to enter the latitude and longitude 
#of tow points on the Earth in degrees. 
#Your program should display the distance between the points in kilometers

#Let (T1, G1) and (T2, G2) be the latitude and longitude of the two points
#Then
#distance = 6371.01 * arccos(sin(T1) * sin(T2) + cos(T1) * cos(T2) * cos(G1 -G2))

from math import radians, acos, sin, cos

print ("This program will calculate the distance between any two  points specified by their latitude and their longitude")

T1 = radians(float(input("Input the latitude of your first point:")))

G1 = radians(float(input("Input the longitude of your first point:")))

T2 = radians(float(input("Input the latitude of your second point:")))

G2 = radians(float(input("Input the longitude of your second point:")))

#print(T1, G1, T2, G2)

distance = 6371.01 * acos(sin(T1) * sin(T2) + cos(T1) * cos(T2) * cos(G1 -G2))

print("The distance between your two points is %r kilometers" % distance)




import math

distance = input("From what height was the object dropped in metres?: ")

final_velocity = math.sqrt(2*9.8*distance)

print("If you drop an object from %r meters the distance when it hits the ground will be %r meters per seconds" % (distance, round(final_velocity,2)))




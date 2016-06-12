
# A retailer sells widgets and gizmos
# Each widget weighs 75 grams
# Each gizmo weighs 112 grams
# Read the number of widgets and gizmos from the user and calculate the total weight

widgets = int(input("How many widgets would you like? "))
gizmos = int(input("How many gizmos would you like? "))

total_weight = int(75 * widgets + 112 * gizmos)

print("The total weigth is ", total_weight, "grams")
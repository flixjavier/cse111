import math

manufacter_items = int(input("what is the number of manufactured items? "))

items_per_box = int(input("how many items per box? "))

#*need to round up the number of boxes. math.ceil round up to the nearest integer that is greater than or equal to a given number

number_of_boxes = math.ceil(manufacter_items / items_per_box)

print(f"the necessary boxes \n to pack {manufacter_items} items are {number_of_boxes}" )


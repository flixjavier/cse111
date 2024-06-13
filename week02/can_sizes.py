import math

#TODO
#main

#**storage_efficiency = volume / surface_area

#** volume = math.pi * (pow(2,radius)) * height

#** surface_area = 2π radius (radius + height)

#Main 

""" def main():
  can_name = input(f'Enter the name of the can: ')
  can_radius = float(input(f'Enter the radius of the can: '))
  can_height = float(input(f'Enter the height of the can: '))

  #Calculate Volume and Surface Area
  can_volume = compute_volume(can_radius, can_height)
  can_surface_area = compute_surface_area(can_radius, can_height)
  can_store_efficiency = compute_store_efficiency(can_volume, can_surface_area)

  print(f'The Surface efficiency of {can_name} is {can_store_efficiency:.2f}') """

def main():
  count = 0

  while count < 13:
    can_name = input(f'Enter the name of the can: ')
    can_radius = float(input(f'Enter the radius of the can: '))
    can_height = float(input(f'Enter the height of the can: '))

    #Calculate Volume and Surface Area
    """ can_volume = compute_volume(can_radius, can_height)
    can_surface_area = compute_surface_area(can_radius, can_height) """
    """ can_store_efficiency = compute_store_efficiency(can_volume, can_surface_area) """
    can_store_efficiency = compute_store_efficiency(can_radius, can_height)

    print(f'The Surface efficiency of {can_name} is {can_store_efficiency:.2f}')
    count += 1

#compute the volume of a cylinder
def compute_volume(radius,height):
  """ Compute the volumen of a cylinder """
  volume = math.pi * (pow(radius,2)) * height
  return volume

#compute the surface area of a cylinder
def compute_surface_area(radius, height):
  """ compute the surface area of a cylinder """
  surface_area = 2 * math.pi * radius * (radius + height)
  return surface_area

#compute the store efficiency
""" def compute_store_efficiency (volume, surface_area):
  store_efficiency = volume / surface_area
  return store_efficiency """
def compute_store_efficiency (radius, height):
  volume = compute_volume(radius, height)
  surface_area = compute_surface_area(radius, height)
  store_efficiency = volume / surface_area
  return store_efficiency

main()







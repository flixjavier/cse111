import math

#this function is used to calculate the volume of a cylinder
def print_cylinder_volume():
  """Compute and print the volume of a cylinder.
    Parameters: none
    Return: nothing
    """
  # Get the radius and the height from the user. 
  radius = float(input(f'Enter the radius of the cylinder: '))
  height = float(input(f'Enter the height of the cylinder: '))

  #calculate the volume

  volume = math.pi * (pow(2,radius)) * height

  #print the volume
  print(f'The volume of cyliner is {volume:.2f}')

#this function is used to calculate the volume of a cylinder
def print_cylinder_volume2(radius, height):
  """Compute and print the volume of a cylinder.
    Parameters: radius, height
    Return: nothing
    """
  #calculate the volume

  volume = math.pi * (pow(2,radius)) * height

  #return the volume value
  return volume

print(f'The Volume of the cylinder is: {print_cylinder_volume2(2.5, 4.1):.2f}')
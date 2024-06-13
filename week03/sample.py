
def water_column_height (tower_height, tank_height):
  """ Function that calculates and returns the height of a column of water from a tower height and a tank wall height  """

  height = tower_height + (3 * tank_height) / 4

  return height


water_column_height(20, 10); 



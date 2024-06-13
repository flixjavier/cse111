"""#!Exceeds requirements. """

PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)

HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)

WATER_DENSITY = 998.2 #Kilogram/meter**3
EARTH_ACCELERATION_OF_GRAVITY = 9.80665 #Meter/second**2
WATER_DYNAMIC_VISCOSITY = 0.0010016 #Pascal seconds

KPA_CONVERTION_FACTOR = 0.14503773773020923

def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss

    pressure_psi = kPa_to_psi(pressure)
    print(f"Pressure at house: {pressure:.1f} kilopascals\nPressure at house: {pressure_psi:.1f} psi")


def water_column_height (tower_height, tank_height):
  """ Function that calculates and returns the height of a column of water from a tower height and a tank wall height  """
  height = tower_height + ((3 * tank_height) / 4)
  return height

def pressure_gain_from_water_height(height):
  """ calculates and returns the pressure caused by Earth’s EARTH_ACCELERATION_OF_GRAVITY pulling on the water stored in an elevated tank (Kilopascals) """
  pressure = (WATER_DENSITY*EARTH_ACCELERATION_OF_GRAVITY*height) / 1000

  return pressure

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
  """calculates and returns the water pressure lost because of the friction between the water and the walls of a pipe that it flows through (Kilopascals)  """
  pressure = -(friction_factor*pipe_length*WATER_DENSITY*(pow(fluid_velocity, 2))) / (2000*pipe_diameter)

  return pressure

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
  """ calculates the water pressure lost because of fittings such as 45° and 90° bends that are in a pipeline (kilopascals)"""

  pressure = -(0.04*WATER_DENSITY*(pow(fluid_velocity,2))*quantity_fittings) / 2000

  return pressure

def reynolds_number(hydraulic_diameter, fluid_velocity):
  """ calculates and returns the Reynolds number for a pipe with water flowing through it. The Reynolds number is a unitless ratio of the inertial and viscous forces in a fluid that is useful for predicting fluid flow in different situations """

  reynolds = (WATER_DENSITY*hydraulic_diameter*fluid_velocity) / WATER_DYNAMIC_VISCOSITY

  return reynolds

def pressure_loss_from_pipe_reduction(larger_diameter,
        fluid_velocity, reynolds_number, smaller_diameter):
  """  calculates the water pressure lost because of water moving from a pipe with a large diameter into a pipe with a smaller diameter """

  k_constant = (0.1 + (50 / reynolds_number)) * (pow(larger_diameter/smaller_diameter, 4)-1)

  pressure = -(k_constant*WATER_DENSITY*pow(fluid_velocity, 2)) / 2000

  return pressure

def kPa_to_psi(kPa):
  """ calculate the conversion between kPa to psi """
  psi = kPa * KPA_CONVERTION_FACTOR
  return psi

if __name__ == "__main__":
    main()












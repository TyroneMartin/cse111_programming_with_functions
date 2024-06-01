def water_column_height(tower_height: float, tank_height: float) -> float:
    """Calculate and return the water column height of a tower.

    Parameters:
        tower_height (float): The height of the tower above the ground.
        tank_height (float): The height of the tank above the tower.

    Returns:
        float: The height of the water column above the ground.
    """
    h = tower_height + (tank_height * 3) / 4
    return h

# print(" print(water_column_height()")
# print(water_column_height(0, 10))
# print(water_column_height(25, 0))
# print(water_column_height(48.3, 12.8))
# print("-------------------------")


def pressure_gain_from_water_height(height: float) -> float:
    """Compute and return the pressure gain in kilopascals caused by Earth’s gravity.

    Parameters:
        height (float): The height of the water column above the ground.

    Returns:
        float: The pressure in kilopascals.
    """
    pressure = 998.2  # the density of water
    gravity = 9.80665  # the acceleration from Earth's gravity

    p = (pressure * gravity * height) / 1000
    return p
# print(" pressure_gain_from_water_height()")
# print(pressure_gain_from_water_height(0))
# print(pressure_gain_from_water_height(30.2))
# print("-------------------------")

def pressure_loss_from_pipe(pipe_diameter: float, pipe_length: float, friction_factor: float, fluid_velocity: float) -> float:
    """Compute and return the pressure loss in kilopascals from friction.

    Parameters:
        pipe_diameter (float): The diameter of the pipe in meters.
        pipe_length (float): The length of the pipe in meters.
        friction_factor (float): The pipe’s friction factor.
        fluid_velocity (float): The velocity of the water flowing through the pipe in meters / second.

    Returns:
        float: The lost pressure in kilopascals.
    """
    density = 998.2  # the density of water
    p = -friction_factor * pipe_length * density * (fluid_velocity ** 2) / (2000 * pipe_diameter)
    return p

# print(" pressure_loss_from_pipe()")
# print(pressure_loss_from_pipe(0.048692, 0, 0.018, 1.75))
# print(pressure_loss_from_pipe(0.048692, 200, 0, 1.75))
# print("-------------------------")

def pressure_loss_from_fittings(fluid_velocity: float, quantity_fittings: int) -> float:
    """
    Calculate the pressure loss from pipe fittings.

    Args:
        fluid_velocity (float): Velocity of the water flowing through the pipe in meters/second.
        quantity_fittings (int): Quantity of fittings.

    Returns:
        float: The lost pressure in kilopascals.
    """
    pressure_density = 998.2
    lost_pressure = -0.04 * fluid_velocity ** 2 * pressure_density * quantity_fittings / 2000
    return lost_pressure

# print(" pressure_loss_from_fittings()")
# print(pressure_loss_from_fittings(0, 3))
# print(pressure_loss_from_fittings(1.65, 0))
# print(pressure_loss_from_fittings(1.65, 2))
# print("-------------------------")


def reynolds_number(hydraulic_diameter: float, fluid_velocity: float) -> float:
    """
    Calculate the Reynolds number for fluid flow in a pipe.

    Args:
        hydraulic_diameter (float): The hydraulic diameter of the pipe in meters.
        fluid_velocity (float): The velocity of the fluid flowing through the pipe in meters/second.

    Returns:
        float: The Reynolds number for the flow.
    """
    water_density = 998.2
    dynamic_viscosity = 0.0010016
    reynolds = water_density * fluid_velocity * hydraulic_diameter / dynamic_viscosity
    return reynolds

def pressure_loss_from_pipe_reduction(larger_diameter: float, fluid_velocity: float, reynolds_number: float, smaller_diameter: float) -> float:
    """ 
    Calculate the water pressure lost due to water moving from a pipe with a
    larger diameter to a pipe with a smaller diameter.
    
    Parameters:
    larger_diameter (float): Diameter of the larger pipe in meters
    fluid_velocity (float): Velocity of water flowing through the larger diameter pipe in meters/second
    reynolds_number (float): Reynolds number corresponding to the pipe with the larger diameter
    smaller_diameter (float): Diameter of the smaller pipe in meters
    
    Returns:
    float: The lost pressure in kilopascals
    """
    water_density = 998.2
    k = (0.1 + 50 / reynolds_number) * ((larger_diameter / smaller_diameter) ** 4 - 1)
    pressure_loss = -k * water_density * fluid_velocity ** 2 / 2000
    return pressure_loss

def compute_fluid_force(water_density: float, water_dynamic_viscosity: float) -> float:
    """ 
    Calculate the fluid force acting on an object submerged in a fluid.
    
    Parameters:
    water_density (float): Density of the fluid in kg/m^3
    water_dynamic_viscosity (float): Viscosity of the fluid in Pa.s
    
    Returns:
    float: The fluid force in N
    """
    # constant for Earth's gravitational force g = GM/r^2
    gravity = 9.8  
    fluid_force = gravity * water_density * water_dynamic_viscosity 
    return fluid_force



PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)

HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)


def main() -> None:
    """ 
    This function gets user input from the user and calculates the pressure at the house based on various factors
    and prints the result.
    """
    tower_height: float = float(input("Height of water tower (meters): "))
    tank_height: float = float(input("Height of water tank walls (meters): "))
    length1: float = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles: int = int(input("Number of 90° angles in supply pipe: "))
    length2: float = float(input("Length of pipe from supply to house (meters): "))

    water_height: float = water_column_height(tower_height, tank_height)
    pressure: float = pressure_gain_from_water_height(water_height)

    diameter: float = PVC_SCHED80_INNER_DIAMETER
    friction: float = PVC_SCHED80_FRICTION_FACTOR
    velocity: float = SUPPLY_VELOCITY
    reynolds: float = reynolds_number(diameter, velocity)
    loss: float = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    loss = pressure_loss_from_pipe_reduction(diameter, velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss

    # Creativity section: Ask the user for input
    print("\nCreativity Section")
    water_density = float(input("Please enter the water density (kg/m^3): "))
    water_dynamic_viscosity = float(input("Please enter the water dynamic viscosity (Pa·s): "))
    result = compute_fluid_force(water_density, water_dynamic_viscosity)
    print()
    
    print(f"1. Pressure at house: {pressure:.1f} kilopascals")
    print(f"2. The computed fluid force is: {result:.0f} Newtons")



if __name__ == "__main__":
    main()





















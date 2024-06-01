"""
Formulas for water flow


def water_column_height(tower_height, tank_height):

h = t + 3w/4
where
h is height of the water column
t is the height of the tower
w is the height of the walls of the tank that is on top of the tower

# pressure_gain_from_water_height(height)

In your function, use the following formula for calculating pressure caused by Earth’s gravity.

P = ρgh/1000
where
P is the pressure in kilopascals
ρ is the density of water (998.2 kilogram / meter3)
g is the acceleration from Earths gravity (9.80665 meter / second2)
h is the height of the water column in meters


-------------------------
pressure_loss_from_pipe()

In your function, use the following formula for calculating pressure loss from friction within a pipe.

P = -fLpv^2/2000 d
where
P is the lost pressure in kilopascals
f is the pipe’s friction factor
L is the length of the pipe in meters
ρ is the density of water (998.2 kilogram / meter3)
v is the velocity of the water flowing through the pipe in meters / second
d is the diameter of the pipe in meters

"""


def water_column_height(tower_height, tank_height):
    """Compute and return the water column height of a tower with
    tower_height above the ground, and tank_height above the tower. 

    Parameters
        tower_height: a float that is the height of the tower above the ground
        tank_height: a float that is the height of the tank above the tower

    Return: a float that is the height of the water column above the ground
    """
    h = tower_height + (tank_height * 3) / 4
    return h

# print(" print(water_column_height()")
# print(water_column_height(0, 10))
# print(water_column_height(25, 0))
# print(water_column_height(48.3, 12.8))
# print("-------------------------")


def pressure_gain_from_water_height(height):
    """Compute and return the pressure gain in kilopascals caused by 
    Earth’s gravity.

    Parameters
        height: a float that is the height of the water column above the ground

    Return: a float that is the pressure in kilopascals
    """
    pressure  = 998.2 # the density of water
    gravity  = 9.80665 # the acceleration from Earths gravity

    p = (pressure * gravity  * height) / 1000
    return p
# print(" pressure_gain_from_water_height()")
# print(pressure_gain_from_water_height(0))
# print(pressure_gain_from_water_height(30.2))
# print("-------------------------")

def pressure_loss_from_pipe(pipe_diameter,
        pipe_length, friction_factor, fluid_velocity):
    """Compute and return the pressure loss in kilopascals from friction

    Parameters
        pipe_diameter: a float that is the diameter of the pipe in meters
        pipe_length: a float that is the length of the pipe in meters
        friction_factor: a float that is the pipe’s friction factor
        fluid_velocity: a float that is the velocity of the water flowing
            through the pipe in meters / second

    Return: a float that is the lost pressure in kilopascals
    """
    density = 998.2 # the density of water
    p = -friction_factor * pipe_length * density * (fluid_velocity ** 2) / (2000 * pipe_diameter)
    return p

# print(" pressure_loss_from_pipe()")
# print(pressure_loss_from_pipe(0.048692, 0, 0.018, 1.75))
# print(pressure_loss_from_pipe(0.048692, 200, 0, 1.75))
# print("-------------------------")


"""
continued 

In your function, use the following formula for calculating pressure loss from pipe fittings.

pressure_loss_from_fittings
P = -0.04 pv^2 n / 2000 
where
P is the lost pressure in kilopascals
p is the density of water (998.2 kilogram / meter3)
v is the velocity of the water flowing through the pipe in meters / second
n is the quantity of fittings


Reynolds number for a pipe with water flowing through it.
The Reynolds number is a unitless ratio of the inertial and viscous
forces in a fluid that is useful for predicting fluid flow in different situations. 
The function must have this header.

reynolds_number()

R = pdv/μ
where
R is the Reynolds number
p is the density of water (998.2 kilogram / meter3)
d is the hydraulic diameter of a pipe in meters. For a round pipe, the hydraulic diameter is the same as the pipe’s inner diameter.
v is the velocity of the water flowing through the pipe in meters / second
μ is the dynamic viscosity of water (0.0010016 Pascal seconds)

"""

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    pressure_density = 998.2
    lost_pressure = -0.04 * fluid_velocity ** 2 * pressure_density * quantity_fittings / 2000
    return lost_pressure

# print(" pressure_loss_from_fittings()")
# print(pressure_loss_from_fittings(0, 3))
# print(pressure_loss_from_fittings(1.65, 0))
# print(pressure_loss_from_fittings(1.65, 2))
# print("-------------------------")


def reynolds_number(hydraulic_diameter, fluid_velocity):

    water_density = 998.2
    dynamic_viscosity = 0.0010016
    reynolds =  water_density * fluid_velocity * hydraulic_diameter / dynamic_viscosity
    return reynolds


""""
 program write a function named pressure_loss_from_pipe_reduction that calculates the water pressure lost because of water moving from a pipe with a large diameter into a pipe with a smaller diameter. The function must have this header.

 
k = (0.1 + 50 / R) ((D/d)^4 - 1)

P = -k pv^2 / 2000

where
k is a constant computed by the first formula and used in the second formula
R is the Reynolds number that corresponds to the pipe with the larger diameter
D is the diameter of the larger pipe in meters
d is the diameter of the smaller pipe in meters
P is the lost pressure kilopascals
ρ is the density of water (998.2 kilogram / meter3)
v is the velocity of the water flowing through the larger diameter pipe in meters / second

"""

def pressure_loss_from_pipe_reduction(larger_diameter,
        fluid_velocity, reynolds_number, smaller_diameter):
    
    water_density = 998.2
    k = (0.1 + 50 / reynolds_number) * ((larger_diameter / smaller_diameter) ** 4 - 1)
    pressure_loss = -k * water_density * fluid_velocity ** 2 / 2000
    return pressure_loss

"""
Gravity is measured as how fast objects accelerate towards each other. 
The average gravitational pull of the Earth is 9.8 meters 
per second squared (m/s2).
"""
def compute_fluid_force(water_density, water_dynamic_viscosity):
    #  constant  for  earth’s gravitational force g = GM/r^2
    gravity = 9.8  
    fluid_force = gravity * water_density * water_dynamic_viscosity 
    return fluid_force




PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)

HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)


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

    print(f"Pressure at house: {pressure:.1f} kilopascals")


if __name__ == "__main__":
    main()





















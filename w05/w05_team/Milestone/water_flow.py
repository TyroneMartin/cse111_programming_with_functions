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
# print(pressure_gain_from_water_height(50))
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

print(" pressure_loss_from_pipe()")
print(pressure_loss_from_pipe(0.048692, 0, 0.018, 1.75))
print(pressure_loss_from_pipe(0.048692, 200, 0, 1.75))
print(pressure_loss_from_pipe(0.048692, 200, 0.018, 0))
print(pressure_loss_from_pipe(0.048692, 200, 0.018, 1.75))
print(pressure_loss_from_pipe(0.048692, 200, 0.018, 1.65))
print(pressure_loss_from_pipe(0.28687, 1000, 0.013, 1.65))
print(pressure_loss_from_pipe(0.28687, 1800.75, 0.013, 1.65))























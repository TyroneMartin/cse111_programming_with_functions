""""
Problem Statement
In many countries, food is stored in steel cans (also known as tin cans) that are shaped like cylinders. 
There are many different sizes of steel cans. The storage efficiency of a can tells us how much a can stores 
versus how much steel is required to make the can. Some sizes of cans require a lot of steel to store a small 
amount of food. Other sizes of cans require less steel and store more food. A can size with a large storage 
efficiency is considered more friendly to the environment than a can size with a small storage efficiency.

The storage efficiency of a steel can is computed by dividing the volume of a can by its surface area.

storage_efficiency = volume /surface_area

In other words, the storage efficiency of a can is the space inside the can divided by the amount of steel required to make the can. The formulas for the volume and surface area of a cylinder are:

volume = π radius^2 height

surface_area = 2π radius (radius + height)

π is the constant PI, the ratio of the circumference of a circle divided by its diameter (use math.pi)
radius is the radius of the cylinder
height is the height of the cylinder
"""

import math
PI = math.pi

def main():
    names = ["#1 Picnic", "#1 Tall", "#2", "#2.5", "#3 Cylinder", "#5", "#6Z", "#8Z short", "#10", "#211", "#300", "#303"]
    Radii = [6.83, 7.78, 8.73, 10.32, 10.79, 13.02, 5.40, 6.83, 15.72, 6.83, 7.62, 8.10]
    Heights = [10.16, 11.91, 11.59, 11.91, 17.78, 14.29, 8.89, 7.62, 17.78, 12.38, 11.27, 11.11]
    cost_per_can= [0.28, 0.43, 0.45, 0.61, 0.86, 0.83, 0.22, 0.26, 1.53, 0.34, 0.38, 0.42]
    
    for i in range(len(names)):
        name =   names[i]
        height = Heights[i]
        radius = Radii[i]
        cost =   cost_per_can[i]
        print(f"{name} has a storage efficiency of {compute_cost_efficiency(radius, height):.2f}")
        print(f"  surface area is {compute_surface_area(radius, height):.2f}")
        print(f"  cost per can is {compute_cost_efficiency (radius, height):.2f}") 
        print(f"  volume is {compute_volume(radius, height):.2f}")
        print(f"  Cost per can is ${cost:.2f}")

def compute_cost_efficiency (radius, height):
        """Compute and return the cost efficiency of a steel can.
        cost_efficiency = volume /surface_area
        Parameter:
        radius: The radius of the cylinder
        height: The height of the cylinder
        Return: The cost efficiency.    
        """
        cost_efficiency = compute_volume(radius, height) / compute_surface_area(radius, height)
        return cost_efficiency



def compute_volume(radius, height):
        """Compute and return the volume of a cylinder volume = π radius^2 height.
        Parameter:
        radius: The radius of the cylinder
        height: The height of the cylinder
        Return: The volume of the cylinder.
        """
        volume = PI * radius**2 * height
        return volume



def compute_surface_area(radius, height):
        """Compute and return the surface area of a cylinder.
        surface_area = 2π radius (radius + height)
        Parameter:
        radius: The radius of the cylinder
        height: The height of the cylinder
        Return: The surface area of the cylinder.
        """
        surface_area = 2 * PI * radius * (radius + height)
        return surface_area



def storage_efficiency(radius, height):
    """Compute and return the storage efficiency of a steel can.
    storage_efficiency = volume /surface_area
    Parameter:
    radius: The radius of the cylinder
    height: The height of the cylinder
    Return: The storage efficiency.    
    """
    volume = compute_volume(radius, height)
    efficiency = volume / compute_surface_area(radius, height)
    return efficiency


 
if __name__ == "__main__":
    main()
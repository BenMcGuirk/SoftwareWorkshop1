"""
Kinetic energy is given by the formula - KE=(1/2)mv^2, where m is mass and v is velocity. Modify project 5 to print the objects
kinetic enegy as well as its momentum.
"""

mass = float(input("Enter its mass: "))
velocity = float(input("Enter its velocity: "))
momentum = mass * velocity
kineticEnergy = (1/2) * mass * velocity ** 2
print("Momentum = " + str(momentum), "and Kinetic Energy = " + str(kineticEnergy))
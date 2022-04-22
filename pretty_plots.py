import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import sympy as sym

# Matplotlib setting to use LaTeX font for plots
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.sans-serif": ["Computer Modern Roman"]})

# Reading in the pressure data
abs_pressure = pd.read_csv("abs_pressure.csv")

pressure_x = abs_pressure.iloc[:, 0]
pressure_y = abs_pressure.iloc[:, 3]

# Read in the drag coefficient data
c_d = pd.read_csv("c_d.csv")
c_d_x = c_d.iloc[:, 0]
c_d_y = c_d.iloc[:, 1]

# Read in the lift coefficient data
c_L = pd.read_csv("c_L.csv")
c_L_x = c_L.iloc[:, 0]
c_L_y = c_L.iloc[:, 1]

# Read in the velocity magnitude data
vel = pd.read_csv("vel_mag.csv")
vel_x = abs_pressure.iloc[:, 2]
vel_mag = abs_pressure.iloc[:, 3]

dpi_val = 1000
'''
# Plot the pressure data
plt.scatter(pressure_x, pressure_y, color='green', marker='o')
plt.title("Absolute Pressure, NACA 0012 Airfoil")
plt.xlabel("Horizontal position (x)")
plt.ylabel("Absolute Pressure (Pa)")
plt.savefig("abs_pressure.png", dpi=dpi_val)

# Plot the drag coefficient data
plt.plot(c_d_x, c_d_y, color='red')
plt.title("Drag Coefficient for NACA 0012 Airfoil")
plt.xlabel("Iteration")
plt.ylabel("Drag Coefficient")
plt.savefig("drag_coef.png", dpi=dpi_val)

# Plot the lift coefficient data
plt.plot(c_L_x, c_L_y, color='blue')
plt.title("Lift Coefficient for NACA 0012 Airfoil")
plt.xlabel("Iteration")
plt.ylabel("Lift Coefficient")
plt.savefig("lift_coef.png", dpi=dpi_val)
'''

# Plot the velocity data
plt.scatter(vel_x, vel_mag, color='red')
plt.title("Velocity Magnitude for NACA 0012 Airfoil")
plt.xlabel("Horizontal Position (m)")
plt.ylabel("Velocity (m/s)")
plt.savefig("vel_mag_plot.png", dpi=dpi_val)
plt.show()

print("Program executed")

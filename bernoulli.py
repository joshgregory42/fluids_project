import pandas as pd
from matplotlib import pyplot as plt


# Bernoulli Equation calculation given ambient pressure, air density, free-streem velocity, and local velocity
def bernoulli_calc(p_1, rho, v_1, v_2):
    p_2 = (p_1 + (1 / 2) * rho * (v_1 ** 2 - v_2 ** 2)) * -1
    return p_2


p_1_calc = 101325.0  # Reference pressure at sea level, Pa

# Read in pressure data
abs_pressure = pd.read_csv("abs_pressure_edited.csv")

p_x = abs_pressure.iloc[:, 0]
p_y = abs_pressure.iloc[:, 1]
pressure = abs_pressure.iloc[:, 3]


def bernoulli_force(y, p):
    force = []
    for i in range(len(p) - 1):
        p_avg = (p[i] + p[i + 1]) / 2
        delta_y = y[i + 1] - y[i]
        force.append(p_avg * delta_y)

    force_total = sum(force)
    return force_total


# Read in the velocity magnitude data
vel = pd.read_csv("vel_mag.csv")

vel_x = abs_pressure.iloc[:, 2]
vel_mag = abs_pressure.iloc[:, 3]

v_1_calc = 300  # m/s
rho_calc = 1.18425  # density of air, kg/m^3

bernoulli = bernoulli_calc(p_1_calc, rho_calc, v_1_calc, vel_mag)

force_bern = bernoulli_force(p_y, pressure)

print("\nTotal drag force: " + str(force_bern) + " N")

# Matplotlib setting to use LaTeX font for plots
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.sans-serif": ["Computer Modern Roman"]})

# Reading in the pressure data
abs_pressure = pd.read_csv("abs_pressure.csv")

pressure_x = abs_pressure.iloc[:, 0]
pressure_y = abs_pressure.iloc[:, 3]

dpi_val = 1000

# Plot the pressure data
plt.scatter(pressure_x, pressure_y, facecolors='none', edgecolors='g')
plt.title("Absolute Pressure, NACA 0012 Airfoil (CFD)")
plt.xlabel("Horizontal Position (x)")
plt.ylabel("Absolute Pressure (Pa)")
plt.savefig("cfd_pressure.png", dpi=dpi_val)
plt.show()


plt.scatter(p_x, bernoulli, facecolors='none', edgecolors='r', label="Bernoulli")
plt.title("Absolute Pressure, NACA 0012 Airfoil (Bernoulli)")
plt.xlabel("Horizontal Position (x)")
plt.ylabel("Absolute Pressure (Pa)")
plt.savefig("bern_pressure.png", dpi=dpi_val)
plt.show()

print("\nProgram executed")

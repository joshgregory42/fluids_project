# MCEN 3021 (Fluid Mechanics) — Final Project Data Analysis

This repository contains all of the raw data, computational fluid dynamics (CFD) simulations, and data analysis programs that was used to obtain and process our data. The CFD solver that was used was Siemens Star CCM+, which are all of the .sim files.

## Repository Structure

The “laminar” folder corresponds to the CFD simulation that was run in the laminar scheme as well as all of the corresponding data that was pulled from that simulation. The “turbulent” folder is the same as the laminar one, however it was run using a turbulent scheme instead of a laminar one.

“CFD Calcs.ipynb” is a Jupyter notebook that contains all of the code that was used to process our CFD results and output a value for the form drag.

“bernoulli.py” is a Python file that takes the absolute pressure and airfoil data from the turbulent CFD simulation and uses the Bernoulli equation to solve for the resulting pressure, which is then taken and in combination with the airfoil coordinates computes the form drag to be compared to the value outputted by “CFD Calcs”.

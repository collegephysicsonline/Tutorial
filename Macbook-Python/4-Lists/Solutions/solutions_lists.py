
#This script contains solutions to various physics problems using Python lists and basic statistical operations.

import math

from collections import Counter

# Importing the math module to perform mathematical operations such as square root, logarithm, and exponential functions.
# Importing the collections module to use the Counter class for counting elements in a list.

# Problem 1: Average velocity
velocities = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
average_velocity = sum(velocities) / len(velocities)
print("Average Velocity:", average_velocity)

# Problem 2: Total mass
masses = [1, 2, 3, 4, 5]
total_mass = sum(masses)
print("Total Mass:", total_mass)

# Problem 3: Maximum distance
distances = [100, 200, 300, 400, 500]
max_distance = max(distances)
print("Maximum Distance:", max_distance)

# Problem 4: Minimum force
forces = [10, 20, 5, 15, 25]
min_force = min(forces)
print("Minimum Force:", min_force)

# Problem 5: Average temperature
temperatures = [30, 32, 31, 29, 28, 27, 26]
average_temperature = sum(temperatures) / len(temperatures)
print("Average Temperature:", average_temperature)

# Problem 6: Sorted heights
heights = [150, 160, 170, 180, 190, 200, 210, 220, 230, 240]
sorted_heights = sorted(heights)
print("Sorted Heights:", sorted_heights)

# Problem 7: Total kinetic energy
kinetic_energies = [100, 200, 300, 400, 500]
total_kinetic_energy = sum(kinetic_energies)
print("Total Kinetic Energy:", total_kinetic_energy)

# Problem 8: Total potential energy
potential_energies = [50, 100, 150, 200, 250]
total_potential_energy = sum(potential_energies)
print("Total Potential Energy:", total_potential_energy)

# Problem 9: Highest power output
power_outputs = [1000, 2000, 1500, 2500, 3000]
highest_power_output = max(power_outputs)
print("Highest Power Output:", highest_power_output)

# Problem 10: Total work done
work_done = [500, 1000, 1500, 2000, 2500]
total_work_done = sum(work_done)
print("Total Work Done:", total_work_done)

# Problem 11: Highest acceleration
accelerations = [2, 4, 6, 8, 10]
highest_acceleration = max(accelerations)
print("Highest Acceleration:", highest_acceleration)

# Problem 12: Total momentum
momenta = [10, 20, 30, 40, 50]
total_momentum = sum(momenta)
print("Total Momentum:", total_momentum)

# Problem 13: Total charge
charges = [1, -1, 2, -2, 3]
total_charge = sum(charges)
print("Total Charge:", total_charge)

# Problem 14: Shortest wavelength
wavelengths = [400, 500, 600, 700, 800]
shortest_wavelength = min(wavelengths)
print("Shortest Wavelength:", shortest_wavelength)

# Problem 15: Highest frequency
frequencies = [50, 60, 70, 80, 90]
highest_frequency = max(frequencies)
print("Highest Frequency:", highest_frequency)
# Problem 16: Calculate the average speed of a car over a trip
speeds = [60, 70, 80, 90, 100]
average_speed = sum(speeds) / len(speeds)
print("Average Speed:", average_speed)

# Problem 17: Find the median value of a list of resistances
resistances = [10, 20, 30, 40, 50, 60, 70]
sorted_resistances = sorted(resistances)
mid_index = len(sorted_resistances) // 2
if len(sorted_resistances) % 2 == 0:
    median_resistance = (sorted_resistances[mid_index - 1] + sorted_resistances[mid_index]) / 2
else:
    median_resistance = sorted_resistances[mid_index]
print("Median Resistance:", median_resistance)

# Problem 18: Calculate the range of a list of voltages
voltages = [110, 120, 130, 140, 150]
voltage_range = max(voltages) - min(voltages)
print("Voltage Range:", voltage_range)

# Problem 19: Find the mode of a list of frequencies
frequencies = [50, 60, 70, 80, 90, 60, 70, 70]
frequency_counts = Counter(frequencies)
mode_frequency = frequency_counts.most_common(1)[0][0]
print("Mode Frequency:", mode_frequency)

# Problem 20: Calculate the harmonic mean of a list of periods
periods = [1, 2, 3, 4, 5]
harmonic_mean = len(periods) / sum(1 / period for period in periods)
print("Harmonic Mean of Periods:", harmonic_mean)

# Problem 21: Find the second highest value in a list of energies
energies = [100, 200, 300, 400, 500]
unique_energies = list(set(energies))
unique_energies.sort()
second_highest_energy = unique_energies[-2]
print("Second Highest Energy:", second_highest_energy)

# Problem 22: Calculate the root mean square (RMS) of a list of currents
currents = [1, 2, 3, 4, 5]
rms_current = math.sqrt(sum(current ** 2 for current in currents) / len(currents))
print("RMS Current:", rms_current)

# Problem 23: Find the interquartile range (IQR) of a list of pressures
pressures = [100, 110, 120, 130, 140, 150, 160, 170, 180, 190]
sorted_pressures = sorted(pressures)
q1 = sorted_pressures[len(sorted_pressures) // 4]
q3 = sorted_pressures[3 * len(sorted_pressures) // 4]
iqr_pressure = q3 - q1
print("Interquartile Range of Pressures:", iqr_pressure)

# Problem 24: Calculate the geometric mean of a list of densities
densities = [1, 2, 3, 4, 5]
geometric_mean = math.exp(sum(math.log(density) for density in densities) / len(densities))
print("Geometric Mean of Densities:", geometric_mean)

# Problem 25: Find the variance of a list of velocities
velocities = [10, 20, 30, 40, 50]
mean_velocity = sum(velocities) / len(velocities)
variance_velocity = sum((velocity - mean_velocity) ** 2 for velocity in velocities) / len(velocities)
print("Variance of Velocities:", variance_velocity)

# Problem 26: Calculate the standard deviation of a list of forces
forces = [10, 20, 30, 40, 50]
mean_force = sum(forces) / len(forces)
variance_force = sum((force - mean_force) ** 2 for force in forces) / len(forces)
std_deviation_force = math.sqrt(variance_force)
print("Standard Deviation of Forces:", std_deviation_force)

# Problem 27: Find the skewness of a list of temperatures
temperatures = [30, 32, 31, 29, 28, 27, 26]
mean_temperature = sum(temperatures) / len(temperatures)
variance_temperature = sum((temp - mean_temperature) ** 2 for temp in temperatures) / len(temperatures)
std_deviation_temperature = math.sqrt(variance_temperature)
skewness_temperature = (sum((temp - mean_temperature) ** 3 for temp in temperatures) / len(temperatures)) / (std_deviation_temperature ** 3)
print("Skewness of Temperatures:", skewness_temperature)

# Problem 28: Calculate the kurtosis of a list of heights
heights = [150, 160, 170, 180, 190, 200, 210, 220, 230, 240]
mean_height = sum(heights) / len(heights)
variance_height = sum((height - mean_height) ** 2 for height in heights) / len(heights)
std_deviation_height = math.sqrt(variance_height)
kurtosis_height = (sum((height - mean_height) ** 4 for height in heights) / len(heights)) / (std_deviation_height ** 4) - 3
print("Kurtosis of Heights:", kurtosis_height)

# Problem 29: Find the covariance between two lists of values
x_values = [1, 2, 3, 4, 5]
y_values = [2, 4, 6, 8, 10]
mean_x = sum(x_values) / len(x_values)
mean_y = sum(y_values) / len(y_values)
covariance = sum((x - mean_x) * (y - mean_y) for x, y in zip(x_values, y_values)) / len(x_values)
print("Covariance:", covariance)

# Problem 30: Calculate the correlation coefficient between two lists of values
std_deviation_x = math.sqrt(sum((x - mean_x) ** 2 for x in x_values) / len(x_values))
std_deviation_y = math.sqrt(sum((y - mean_y) ** 2 for y in y_values) / len(y_values))
correlation_coefficient = covariance / (std_deviation_x * std_deviation_y)
print("Correlation Coefficient:", correlation_coefficient)
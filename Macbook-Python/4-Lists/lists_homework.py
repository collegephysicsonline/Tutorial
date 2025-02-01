"""
Each problem is designed to help students practice list operations and understand their applications in physics.


Problems:

1. Calculate the average velocity from a list of velocities. (e.g., 10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
2. Compute the total mass from a list of masses. (e.g., 1, 2, 3, 4, 5)
3. Determine the maximum distance from a list of distances. (e.g., 100, 200, 300, 400, 500)
4. Find the minimum force from a list of forces. (e.g., 10, 20, 5, 15, 25)
5. Calculate the average temperature from a list of temperatures. (e.g., 30, 32, 31, 29, 28, 27, 26)
6. Sort a list of heights in ascending order. (e.g., 150, 160, 170, 180, 190, 200, 210, 220, 230, 240)
7. Compute the total kinetic energy from a list of kinetic energies. (e.g., 100, 200, 300, 400, 500)
8. Calculate the total potential energy from a list of potential energies. (e.g., 50, 100, 150, 200, 250)
9. Determine the highest power output from a list of power outputs. (e.g., 1000, 2000, 1500, 2500, 3000)
10. Compute the total work done from a list of work values. (e.g., 500, 1000, 1500, 2000, 2500)
11. Find the highest acceleration from a list of accelerations. (e.g., 2, 4, 6, 8, 10)
12. Calculate the total momentum from a list of momenta. (e.g., 10, 20, 30, 40, 50)
13. Compute the total charge from a list of charges. (e.g., 1, -1, 2, -2, 3)
14. Determine the shortest wavelength from a list of wavelengths. (e.g., 400, 500, 600, 700, 800)
15. Find the highest frequency from a list of frequencies. (e.g., 50, 60, 70, 80, 90)
16. Calculate the average speed of a car over a trip from a list of speeds. (e.g., 60, 70, 80, 90, 100)
17. Find the median value of a list of resistances. (e.g., 10, 20, 30, 40, 50, 60, 70)
18. Calculate the range of a list of voltages. (e.g., 110, 120, 130, 140, 150)
19. Find the mode of a list of frequencies. (e.g., 50, 60, 70, 80, 90, 60, 70, 70)
20. Calculate the harmonic mean of a list of periods. (e.g., 1, 2, 3, 4, 5)
21. Find the second highest value in a list of energies. (e.g., 100, 200, 300, 400, 500)
22. Calculate the root mean square (RMS) of a list of currents. (e.g., 1, 2, 3, 4, 5)
23. Find the interquartile range (IQR) of a list of pressures. (e.g., 100, 110, 120, 130, 140, 150, 160, 170, 180, 190)
24. Calculate the geometric mean of a list of densities. (e.g., 1, 2, 3, 4, 5)
25. Find the variance of a list of velocities. (e.g., 10, 20, 30, 40, 50)
26. Calculate the standard deviation of a list of forces. (e.g., 10, 20, 30, 40, 50)
27. Find the skewness of a list of temperatures. (e.g., 30, 32, 31, 29, 28, 27, 26)
28. Calculate the kurtosis of a list of heights. (e.g., 150, 160, 170, 180, 190, 200, 210, 220, 230, 240)
29. Find the covariance between two lists of values. (e.g., x_values: 1, 2, 3, 4, 5 and y_values: 2, 4, 6, 8, 10)
30. Calculate the correlation coefficient between two lists of values. (e.g., x_values: 1, 2, 3, 4, 5 and y_values: 2, 4, 6, 8, 10)

Hints:

1. Average velocity: Use the formula `average_velocity = sum(velocities) / len(velocities)`.
2. Total mass: Use the function `sum(masses)`.
3. Maximum distance: Use the function `max(distances)`.
4. Minimum force: Use the function `min(forces)`.
5. Average temperature: Use the formula `average_temperature = sum(temperatures) / len(temperatures)`.
6. Sort heights: Use the function `sorted(heights)`.
7. Total kinetic energy: Use the function `sum(kinetic_energies)`.
8. Total potential energy: Use the function `sum(potential_energies)`.
9. Highest power output: Use the function `max(power_outputs)`.
10. Total work done: Use the function `sum(work_values)`.
11. Highest acceleration: Use the function `max(accelerations)`.
12. Total momentum: Use the function `sum(momenta)`.
13. Total charge: Use the function `sum(charges)`.
14. Shortest wavelength: Use the function `min(wavelengths)`.
15. Highest frequency: Use the function `max(frequencies)`.
16. Average speed: Use the formula `average_speed = sum(speeds) / len(speeds)`.
17. Median resistance: Use the function `statistics.median(resistances)`.
18. Range of voltages: Use the formula `range_voltages = max(voltages) - min(voltages)`.
19. Mode of frequencies: Use the function `statistics.mode(frequencies)`.
20. Harmonic mean of periods: Use the function `statistics.harmonic_mean(periods)`.
21. Second highest energy: Use the formula `sorted(energies)[-2]`.
22. RMS of currents: Use the formula `rms = math.sqrt(sum(x**2 for x in currents) / len(currents))`.
23. IQR of pressures: Use the formula `IQR = Q3 - Q1` where `Q1` and `Q3` are the 25th and 75th percentiles.
24. Geometric mean of densities: Use the function `statistics.geometric_mean(densities)`.
25. Variance of velocities: Use the function `statistics.variance(velocities)`.
26. Standard deviation of forces: Use the function `statistics.stdev(forces)`.
27. Skewness of temperatures: Use the formula for skewness.
28. Kurtosis of heights: Use the formula for kurtosis.
29. Covariance between two lists: Use the formula for covariance.
30. Correlation coefficient between two lists: Use the formula for correlation coefficient.

"""

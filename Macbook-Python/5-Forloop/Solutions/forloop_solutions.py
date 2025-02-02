# Solutions

#1. **Calculate the average speed of a car over multiple trips.**
speeds = [60, 70, 80]  # speeds in km/h
total_speed = sum(speeds)
average_speed = total_speed / len(speeds)
print(f"Average Speed: {average_speed} km/h")

#2. **Determine the total distance traveled by a car given a list of speeds and times.**
speeds = [60, 70, 80]  # speeds in km/h
times = [1, 2, 1.5]    # times in hours
total_distance = sum([speed * time for speed, time in zip(speeds, times)])
print(f"Total Distance: {total_distance} km")

#3. **Compute the kinetic energy of multiple objects given their masses and velocities.**
masses = [1000, 1500, 1200]  # masses in kg
velocities = [10, 20, 15]    # velocities in m/s
kinetic_energies = [0.5 * mass * velocity**2 for mass, velocity in zip(masses, velocities)]
print(f"Kinetic Energies: {kinetic_energies} J")

#4. **Find the potential energy of objects at different heights.**
masses = [50, 70, 60]  # masses in kg
heights = [10, 15, 12] # heights in meters
g = 9.81  # acceleration due to gravity in m/s^2
potential_energies = [mass * g * height for mass, height in zip(masses, heights)]
print(f"Potential Energies: {potential_energies} J")

#5. **Calculate the work done by a force over various distances.**
forces = [100, 150, 200]  # forces in N
distances = [5, 10, 8]    # distances in meters
work_done = [force * distance for force, distance in zip(forces, distances)]
print(f"Work Done: {work_done} J")

#6. **Determine the acceleration of a car given its change in velocity over time intervals.**
initial_velocities = [0, 10, 20]  # initial velocities in m/s
final_velocities = [20, 30, 40]   # final velocities in m/s
times = [5, 10, 8]                # time intervals in seconds
accelerations = [(final - initial) / time for initial, final, time in zip(initial_velocities, final_velocities, times)]
print(f"Accelerations: {accelerations} m/s^2")

#7. **Compute the gravitational force between multiple pairs of objects.**
masses1 = [5.97e24, 1.989e30]  # masses in kg (Earth, Sun)
masses2 = [7.35e22, 5.97e24]   # masses in kg (Moon, Earth)
distances = [3.84e8, 1.496e11] # distances in meters
G = 6.67430e-11  # gravitational constant in m^3 kg^-1 s^-2
gravitational_forces = [G * mass1 * mass2 / distance**2 for mass1, mass2, distance in zip(masses1, masses2, distances)]
print(f"Gravitational Forces: {gravitational_forces} N")

#8. **Find the momentum of objects given their masses and velocities.**
masses = [1000, 1500, 1200]  # masses in kg
velocities = [10, 20, 15]    # velocities in m/s
momenta = [mass * velocity for mass, velocity in zip(masses, velocities)]
print(f"Momenta: {momenta} kg·m/s")

#9. **Calculate the pressure exerted by a fluid at different depths.**
depths = [10, 20, 30]  # depths in meters
density = 1000         # density of water in kg/m^3
g = 9.81               # acceleration due to gravity in m/s^2
pressures = [density * g * depth for depth in depths]
print(f"Pressures: {pressures} Pa")

#10. **Determine the frequency of a wave given its speed and wavelength.**
speeds = [340, 300, 1500]  # speeds in m/s
wavelengths = [0.5, 1, 0.75]  # wavelengths in meters
frequencies = [speed / wavelength for speed, wavelength in zip(speeds, wavelengths)]
print(f"Frequencies: {frequencies} Hz")

#11. **Compute the electric potential energy of charges at different positions.**
charges1 = [1e-6, 2e-6]  # charges in C
charges2 = [1e-6, 3e-6]  # charges in C
distances = [0.1, 0.2]   # distances in meters
k = 8.99e9  # Coulomb's constant in N·m^2/C^2
electric_potential_energies = [k * charge1 * charge2 / distance for charge1, charge2, distance in zip(charges1, charges2, distances)]
print(f"Electric Potential Energies: {electric_potential_energies} J")

#12. **Find the magnetic force on a moving charge in different magnetic fields.**
charges = [1e-6, 2e-6]  # charges in C
velocities = [10, 20]   # velocities in m/s
magnetic_fields = [0.1, 0.2]  # magnetic fields in T
magnetic_forces = [charge * velocity * magnetic_field for charge, velocity, magnetic_field in zip(charges, velocities, magnetic_fields)]
print(f"Magnetic Forces: {magnetic_forces} N")

#13. **Calculate the heat transferred in various processes given specific heat capacities and temperature changes.**
masses = [1, 2, 1.5]  # masses in kg
specific_heats = [4200, 3900, 4186]  # specific heat capacities in J/(kg·°C)
temperature_changes = [10, 20, 15]  # temperature changes in °C
heat_transferred = [mass * specific_heat * temp_change for mass, specific_heat, temp_change in zip(masses, specific_heats, temperature_changes)]
print(f"Heat Transferred: {heat_transferred} J")

#14. **Determine the efficiency of different machines given input and output energies.**
input_energies = [1000, 2000, 1500]  # input energies in J
output_energies = [800, 1600, 1200]  # output energies in J
efficiencies = [(output / input) * 100 for input, output in zip(input_energies, output_energies)]
print(f"Efficiencies: {efficiencies} %")

#15. **Compute the power output of engines over time intervals.**
work_done = [1000, 2000, 1500]  # work done in J
times = [10, 20, 15]  # time intervals in seconds
power_output = [work / time for work, time in zip(work_done, times)]
print(f"Power Output: {power_output} W")

#16. **Find the angular momentum of rotating objects given their moments of inertia and angular velocities.**
moments_of_inertia = [10, 20, 15]  # moments of inertia in kg·m^2
angular_velocities = [5, 10, 7]  # angular velocities in rad/s
angular_momenta = [moment * angular_velocity for moment, angular_velocity in zip(moments_of_inertia, angular_velocities)]
print(f"Angular Momenta: {angular_momenta} kg·m^2/s")

#17. **Calculate the torque on objects given forces and lever arms.**
forces = [100, 150, 200]  # forces in N
lever_arms = [0.5, 1, 0.75]  # lever arms in meters
torques = [force * lever_arm for force, lever_arm in zip(forces, lever_arms)]
print(f"Torques: {torques} N·m")

#18. **Determine the centripetal force on objects moving in circular paths.**
masses = [1000, 1500, 1200]  # masses in kg
velocities = [10, 20, 15]  # velocities in m/s
radii = [50, 100, 75]  # radii in meters
centripetal_forces = [mass * velocity**2 / radius for mass, velocity, radius in zip(masses, velocities, radii)]
print(f"Centripetal Forces: {centripetal_forces} N")

#19. **Compute the buoyant force on objects submerged in fluids.**
volumes = [0.1, 0.2, 0.15]  # volumes in m^3
fluid_density = 1000  # density of water in kg/m^3
g = 9.81  # acceleration due to gravity in m/s^2
buoyant_forces = [fluid_density * g * volume for volume in volumes]
print(f"Buoyant Forces: {buoyant_forces} N")

#20. **Find the refractive index of materials given angles of incidence and refraction.**
import math
angles_of_incidence = [30, 45, 60]  # angles in degrees
angles_of_refraction = [20, 30, 40]  # angles in degrees
refractive_indices = [math.sin(math.radians(incidence)) / math.sin(math.radians(refraction)) for incidence, refraction in zip(angles_of_incidence, angles_of_refraction)]
print(f"Refractive Indices: {refractive_indices}")

#21. **Calculate the Doppler shift for sound waves from moving sources.**
source_frequencies = [500, 1000, 1500]  # frequencies in Hz
source_speeds = [10, 20, 15]  # speeds in m/s
observer_speed = 0  # observer is stationary
speed_of_sound = 343  # speed of sound in air in m/s
doppler_shifts = [source_frequency * (speed_of_sound / (speed_of_sound - source_speed)) for source_frequency, source_speed in zip(source_frequencies, source_speeds)]
print(f"Doppler Shifts: {doppler_shifts} Hz")

#22. **Determine the intensity of light at different distances from a source.**
power = 100  # power of the light source in W
distances = [1, 2, 3]  # distances in meters
intensities = [power / (4 * math.pi * distance**2) for distance in distances]
print(f"Intensities: {intensities} W/m^2")

#23. **Compute the capacitance of capacitors in series and parallel circuits.**
capacitors = [1e-6, 2e-6, 3e-6]  # capacitances in F
capacitance_series = 1 / sum([1 / c for c in capacitors])
capacitance_parallel = sum(capacitors)
print(f"Capacitance in Series: {capacitance_series} F")
print(f"Capacitance in Parallel: {capacitance_parallel} F")

#24. **Find the inductance of coils given their physical properties.**
turns = [100, 200, 150]  # number of turns
areas = [0.01, 0.02, 0.015]  # cross-sectional areas in m^2
lengths = [0.1, 0.2, 0.15]  # lengths in meters
permeability = 4 * math.pi * 1e-7  # permeability of free space in H/m
inductances = [(permeability * turn**2 * area) / length for turn, area, length in zip(turns, areas, lengths)]
print(f"Inductances: {inductances} H")

#25. **Calculate the resonant frequency of LC circuits.**
inductances = [1e-3, 2e-3, 1.5e-3]  # inductances in H
capacitances = [1e-6, 2e-6, 1.5e-6]  # capacitances in F
resonant_frequencies = [1 / (2 * math.pi * math.sqrt(L * C)) for L, C in zip(inductances, capacitances)]
print(f"Resonant Frequencies: {resonant_frequencies} Hz")

#26. **Determine the impedance of RLC circuits at different frequencies.**
resistances = [10, 20, 15]  # resistances in ohms
inductances = [1e-3, 2e-3, 1.5e-3]  # inductances in H
capacitances = [1e-6, 2e-6, 1.5e-6]  # capacitances in F
frequencies = [50, 60, 70]  # frequencies in Hz
impedances = [math.sqrt(R**2 + (2 * math.pi * f * L - 1 / (2 * math.pi * f * C))**2) for R, L, C, f in zip(resistances, inductances, capacitances, frequencies)]
print(f"Impedances: {impedances} ohms")

#27. **Compute the energy stored in magnetic fields of inductors.**
inductances = [1e-3, 2e-3, 1.5e-3]  # inductances in H
currents = [1, 2, 1.5]  # currents in A
energies = [0.5 * L * I**2 for L, I in zip(inductances, currents)]
print(f"Energy Stored: {energies} J")

#28. **Find the charge and discharge times of capacitors in RC circuits.**
resistances = [10, 20, 15]  # resistances in ohms
capacitances = [1e-6, 2e-6, 1.5e-6]  # capacitances in F
time_constants = [R * C for R, C in zip(resistances, capacitances)]
print(f"Time Constants: {time_constants} s")

#29. **Calculate the diffraction angles for light passing through slits.**
wavelengths = [500e-9, 600e-9, 700e-9]  # wavelengths in meters
slit_widths = [1e-6, 2e-6, 1.5e-6]  # slit widths in meters
diffraction_angles = [math.asin(wavelength / slit_width) for wavelength, slit_width in zip(wavelengths, slit_widths)]
print(f"Diffraction Angles: {diffraction_angles} radians")

#30. **Determine the polarization of light after passing through polarizers.**
initial_intensity = 100  # initial intensity in W/m^2
angles = [30, 45, 60]  # angles in degrees
final_intensities = [initial_intensity * math.cos(math.radians(angle))**2 for angle in angles]
print(f"Final Intensities: {final_intensities} W/m^2")

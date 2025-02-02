import numpy as np
import matplotlib.pyplot as plt

# Define initial conditions
v0 = 20  # initial velocity in m/s
angle = 45  # launch angle in degrees
g = 9.81  # acceleration due to gravity in m/s^2

# Convert angle to radians
theta = np.radians(angle)

# Time of flight
t_flight = 2 * v0 * np.sin(theta) / g

# Time intervals
t = np.linspace(0, t_flight, num=500)

# Calculate trajectory
x = v0 * np.cos(theta) * t
y = v0 * np.sin(theta) * t - 0.5 * g * t**2

# Plot trajectory
plt.plot(x, y)
plt.xlabel('Distance (m)')
plt.ylabel('Height (m)')
plt.title('Projectile Trajectory')
plt.show()
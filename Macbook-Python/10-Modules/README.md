# Introduction

In the field of physics, solving complex problems often requires advanced computational tools. Python, with its extensive range of modules, provides powerful capabilities to handle various physics-related tasks such as numerical computations, data analysis, and visualizations. These modules simplify the implementation of mathematical models and simulations, making it easier for students and researchers to focus on the core concepts rather than the intricacies of programming.

### Example:
Consider the problem of calculating the trajectory of a projectile. Using Python modules like NumPy and Matplotlib, we can easily compute and visualize the path of the projectile under the influence of gravity.

### Physics Concept: Trajectory of a Projectile

The trajectory of a projectile is the path that an object follows when it is launched into the air and influenced only by gravity and its initial velocity. The motion of the projectile can be analyzed by breaking it into two components: horizontal motion and vertical motion.

1. **Horizontal Motion**: The horizontal component of the motion is uniform, meaning the horizontal velocity remains constant throughout the flight because there are no horizontal forces acting on the projectile (assuming air resistance is negligible).

2. **Vertical Motion**: The vertical component of the motion is uniformly accelerated motion, meaning the vertical velocity changes due to the acceleration caused by gravity. The vertical motion can be described by the equations of motion under constant acceleration.

The key parameters involved in the trajectory of a projectile are:
- Initial velocity ($(v_0$)): The speed at which the projectile is launched.
- Launch angle ($\theta$): The angle at which the projectile is launched with respect to the horizontal.
- Acceleration due to gravity ($g$): The constant acceleration acting on the projectile in the vertical direction, typically $9.81 \, \text{m/s}^2$.

The equations governing the motion of the projectile are:
- Horizontal distance ($x$): $x = v_0 \cos(\theta) \cdot t$
- Vertical distance ($y$): $y = v_0 \sin(\theta) \cdot t - \frac{1}{2} g t^2$

Where $t$ is the time elapsed since the projectile was launched.

The following Python code demonstrates how to calculate and visualize the trajectory of a projectile using NumPy and Matplotlib:

```python
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
```

This example demonstrates how Python modules can be used to solve and visualize physics problems efficiently. By learning these modules, students can enhance their problem-solving skills and gain deeper insights into physical phenomena.


## Python Modules for Physics Students
Here are some useful links to the online documentation for each of the mentioned Python modules:

- [NumPy Documentation](https://numpy.org/doc/)
- [SciPy Documentation](https://docs.scipy.org/doc/scipy/)
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
- [SymPy Documentation](https://docs.sympy.org/latest/index.html)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Astropy Documentation](https://docs.astropy.org/en/stable/)
- [Pint Documentation](https://pint.readthedocs.io/en/stable/)
- [VPython Documentation](https://vpython.org/)
- [PyOpenGL Documentation](http://pyopengl.sourceforge.net/documentation/)
- [PyMC3 Documentation](https://docs.pymc.io/)
### Installation

To use the Python modules mentioned in this document, you need to install them first. You can install these packages using `pip`, the Python package installer. Here are the installation commands for each module:

```sh
pip install numpy
pip install scipy
pip install matplotlib
pip install sympy
pip install pandas
pip install astropy
pip install pint
pip install vpython
pip install PyOpenGL
pip install pymc3
```
### 1. NumPy
NumPy is a fundamental package for scientific computing with Python. It provides support for arrays, matrices, and many mathematical functions. It is widely used in various scientific and engineering domains, including physics, for tasks such as numerical simulations, data analysis, and more. Key features of NumPy include:

- Efficient multi-dimensional array operations
- Mathematical functions for linear algebra, Fourier transforms, and random number generation
- Tools for integrating C/C++ and Fortran code
- Extensive support for data manipulation and analysis

#### Example:
```python
import numpy as np

# Create an array
arr = np.array([1, 2, 3, 4, 5])
print("Array:", arr)

# Perform mathematical operations
print("Mean:", np.mean(arr))
print("Standard Deviation:", np.std(arr))

# Create a 2D array (matrix)
matrix = np.array([[1, 2], [3, 4]])
print("Matrix:\n", matrix)

# Perform matrix multiplication
result = np.dot(matrix, matrix)
print("Matrix multiplication result:\n", result)
```

#### Example:
```python
import numpy as np

# Create an array
arr = np.array([1, 2, 3, 4, 5])
print("Array:", arr)

# Perform mathematical operations
print("Mean:", np.mean(arr))
print("Standard Deviation:", np.std(arr))
```

### Physics Examples with NumPy

#### 1. Calculating Kinetic Energy
```python
import numpy as np

mass = 5.0  # in kg
velocity = 10.0  # in m/s

kinetic_energy = 0.5 * mass * np.square(velocity)
print("Kinetic Energy:", kinetic_energy, "Joules")
```

#### 2. Calculating Potential Energy
```python
mass = 5.0  # in kg
height = 10.0  # in meters
g = 9.81  # acceleration due to gravity in m/s^2

potential_energy = mass * g * height
print("Potential Energy:", potential_energy, "Joules")
```

#### 3. Calculating Gravitational Force
```python
mass1 = 5.0  # in kg
mass2 = 10.0  # in kg
distance = 2.0  # in meters
G = 6.67430e-11  # gravitational constant in m^3 kg^-1 s^-2

gravitational_force = G * (mass1 * mass2) / np.square(distance)
print("Gravitational Force:", gravitational_force, "Newtons")
```

#### 4. Calculating Centripetal Force
```python
mass = 5.0  # in kg
velocity = 10.0  # in m/s
radius = 2.0  # in meters

centripetal_force = mass * np.square(velocity) / radius
print("Centripetal Force:", centripetal_force, "Newtons")
```

#### 5. Calculating Work Done
```python
force = 10.0  # in Newtons
distance = 5.0  # in meters

work_done = force * distance
print("Work Done:", work_done, "Joules")
```

#### 6. Calculating Power
```python
work_done = 50.0  # in Joules
time = 5.0  # in seconds

power = work_done / time
print("Power:", power, "Watts")
```

#### 7. Calculating Momentum
```python
mass = 5.0  # in kg
velocity = 10.0  # in m/s

momentum = mass * velocity
print("Momentum:", momentum, "kg m/s")
```

#### 8. Calculating Impulse
```python
force = 10.0  # in Newtons
time = 2.0  # in seconds

impulse = force * time
print("Impulse:", impulse, "N s")
```

#### 9. Calculating Pressure
```python
force = 100.0  # in Newtons
area = 5.0  # in square meters

pressure = force / area
print("Pressure:", pressure, "Pascals")
```

#### 10. Calculating Density
```python
mass = 10.0  # in kg
volume = 2.0  # in cubic meters

density = mass / volume
print("Density:", density, "kg/m^3")
```
### Quantum Physics Examples with NumPy

#### 1. Calculating Energy Levels of a Particle in a Box
```python
import numpy as np

# Constants
h = 6.626e-34  # Planck's constant in J*s
m = 9.109e-31  # Mass of electron in kg
L = 1e-9  # Length of the box in meters

# Quantum number
n = 1

# Calculate energy level
E_n = (n**2 * h**2) / (8 * m * L**2)
print(f"Energy level for n={n}: {E_n} Joules")
```

#### 2. Calculating the Wavefunction of a Particle in a Box
```python
import numpy as np
import matplotlib.pyplot as plt

# Constants
L = 1e-9  # Length of the box in meters
n = 1  # Quantum number

# Position array
x = np.linspace(0, L, 1000)

# Calculate wavefunction
psi_n = np.sqrt(2 / L) * np.sin(n * np.pi * x / L)

# Plot wavefunction
plt.plot(x, psi_n)
plt.xlabel('Position (m)')
plt.ylabel('Wavefunction')
plt.title(f'Wavefunction for n={n}')
plt.show()
```

#### 3. Calculating the Probability Density of a Particle in a Box
```python
import numpy as np
import matplotlib.pyplot as plt

# Constants
L = 1e-9  # Length of the box in meters
n = 1  # Quantum number

# Position array
x = np.linspace(0, L, 1000)

# Calculate wavefunction
psi_n = np.sqrt(2 / L) * np.sin(n * np.pi * x / L)

# Calculate probability density
prob_density = np.square(psi_n)

# Plot probability density
plt.plot(x, prob_density)
plt.xlabel('Position (m)')
plt.ylabel('Probability Density')
plt.title(f'Probability Density for n={n}')
plt.show()
```

#### 4. Calculating the Expectation Value of Position
```python
import numpy as np

# Constants
L = 1e-9  # Length of the box in meters
n = 1  # Quantum number

# Position array
x = np.linspace(0, L, 1000)

# Calculate wavefunction
psi_n = np.sqrt(2 / L) * np.sin(n * np.pi * x / L)

# Calculate expectation value of position
expectation_x = np.trapz(x * np.square(psi_n), x)
print(f"Expectation value of position for n={n}: {expectation_x} meters")
```

#### 5. Calculating the Expectation Value of Momentum
```python
import numpy as np

# Constants
hbar = 1.0545718e-34  # Reduced Planck's constant in J*s
L = 1e-9  # Length of the box in meters
n = 1  # Quantum number

# Calculate expectation value of momentum
expectation_p = n * np.pi * hbar / L
print(f"Expectation value of momentum for n={n}: {expectation_p} kg*m/s")
```
### 2. SciPy
SciPy builds on NumPy and provides additional functionality for optimization, integration, interpolation, eigenvalue problems, and other advanced mathematical functions.
### Physics Examples with SciPy

#### 1. Solving Ordinary Differential Equations (ODEs)
SciPy provides powerful tools for solving ODEs, which are common in physics for modeling dynamic systems.

```python
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the differential equation
def harmonic_oscillator(y, t, k, m):
    x, v = y
    dydt = [v, -k/m * x]
    return dydt

# Initial conditions: [initial position, initial velocity]
y0 = [1.0, 0.0]

# Time points where solution is computed
t = np.linspace(0, 10, 100)

# Parameters: spring constant k and mass m
k = 1.0
m = 1.0

# Solve ODE
solution = odeint(harmonic_oscillator, y0, t, args=(k, m))

# Plot results
plt.plot(t, solution[:, 0], label='Position (x)')
plt.plot(t, solution[:, 1], label='Velocity (v)')
plt.xlabel('Time (s)')
plt.ylabel('Position and Velocity')
plt.title('Harmonic Oscillator')
plt.legend()
plt.show()
```

#### 2. Performing Fourier Transform
Fourier transforms are used in physics to analyze the frequencies present in a signal.

```python
import numpy as np
from scipy.fft import fft, fftfreq
import matplotlib.pyplot as plt

# Sample rate and duration
sample_rate = 1000
T = 1.0 / sample_rate
t = np.linspace(0.0, 1.0, sample_rate, endpoint=False)

# Create a signal with two frequencies
signal = np.sin(50.0 * 2.0 * np.pi * t) + 0.5 * np.sin(80.0 * 2.0 * np.pi * t)

# Perform Fourier transform
yf = fft(signal)
xf = fftfreq(sample_rate, T)[:sample_rate//2]

# Plot the signal and its Fourier transform
plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.title('Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.subplot(2, 1, 2)
plt.plot(xf, 2.0/sample_rate * np.abs(yf[0:sample_rate//2]))
plt.title('Fourier Transform')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.tight_layout()
plt.show()
```

#### 3. Interpolating Data
Interpolation is useful for estimating values between known data points.

```python
import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

# Known data points
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0, 1, 4, 9, 16, 25])

# Create interpolation function
f = interp1d(x, y, kind='cubic')

# Interpolated values
x_new = np.linspace(0, 5, 100)
y_new = f(x_new)

# Plot original data and interpolation
plt.plot(x, y, 'o', label='Original data')
plt.plot(x_new, y_new, '-', label='Cubic interpolation')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Data Interpolation')
plt.legend()
plt.show()
```
These examples illustrate how SciPy can be used to solve differential equations, perform Fourier transforms, and interpolate data, making it an invaluable tool for physics students.

### Quantum Physics Examples with SciPy

#### 1. Solving the Schrödinger Equation for a Particle in a Box
```python
import numpy as np
from scipy.linalg import eigh
import matplotlib.pyplot as plt

# Constants
hbar = 1.0545718e-34  # Reduced Planck's constant in J*s
m = 9.10938356e-31  # Mass of electron in kg
L = 1e-9  # Length of the box in meters

# Discretize space
N = 1000
x = np.linspace(0, L, N)
dx = x[1] - x[0]

# Construct the Hamiltonian matrix
H = np.zeros((N, N))
for i in range(1, N-1):
    H[i, i] = -2
    H[i, i-1] = 1
    H[i, i+1] = 1
H = -hbar**2 / (2 * m * dx**2) * H

# Solve the eigenvalue problem
energies, wavefunctions = eigh(H)

# Plot the first three wavefunctions
plt.figure(figsize=(10, 6))
for n in range(3):
    plt.plot(x, wavefunctions[:, n], label=f'n={n+1}')
plt.xlabel('Position (m)')
plt.ylabel('Wavefunction')
plt.title('Wavefunctions of a Particle in a Box')
plt.legend()
plt.show()

# Print the first three energy levels
for n in range(3):
    print(f"Energy level for n={n+1}: {energies[n]} Joules")
```

#### 2. Solving the Time-Dependent Schrödinger Equation
```python
import numpy as np
from scipy.sparse import diags
from scipy.sparse.linalg import expm
import matplotlib.pyplot as plt

# Constants
hbar = 1.0545718e-34  # Reduced Planck's constant in J*s
m = 9.10938356e-31  # Mass of electron in kg
L = 1e-9  # Length of the box in meters

# Discretize space
N = 1000
x = np.linspace(0, L, N)
dx = x[1] - x[0]

# Construct the Hamiltonian matrix
diagonals = [-2 * np.ones(N), np.ones(N-1), np.ones(N-1)]
H = diags(diagonals, [0, -1, 1]) * (-hbar**2 / (2 * m * dx**2))

# Initial wavefunction (Gaussian wave packet)
x0 = L / 2
sigma = L / 20
k = 5 * np.pi / L
psi0 = np.exp(-(x - x0)**2 / (2 * sigma**2)) * np.exp(1j * k * x)
psi0 /= np.sqrt(np.sum(np.abs(psi0)**2) * dx)

# Time evolution
t = 1e-15  # Time in seconds
U = expm(-1j * H * t / hbar)
psi_t = U @ psi0

# Plot the initial and final wavefunctions
plt.figure(figsize=(10, 6))
plt.plot(x, np.abs(psi0)**2, label='Initial')
plt.plot(x, np.abs(psi_t)**2, label='After time t')
plt.xlabel('Position (m)')
plt.ylabel('Probability Density')
plt.title('Time Evolution of a Gaussian Wave Packet')
plt.legend()
plt.show()
```
These examples demonstrate how SciPy can be used to solve quantum physics problems, such as finding the energy levels and wavefunctions of a particle in a box and simulating the time evolution of a quantum state.
### 3. Matplotlib
Matplotlib is a plotting library for creating static, animated, and interactive visualizations in Python.
### Physics Examples with Matplotlib

#### 1. Visualizing Simple Harmonic Motion
```python
import numpy as np
import matplotlib.pyplot as plt

# Parameters
A = 1.0  # Amplitude
omega = 2.0  # Angular frequency
phi = 0.0  # Phase
t = np.linspace(0, 10, 1000)  # Time array

# Displacement as a function of time
x = A * np.cos(omega * t + phi)

# Plotting
plt.plot(t, x)
plt.xlabel('Time (s)')
plt.ylabel('Displacement (m)')
plt.title('Simple Harmonic Motion')
plt.show()
```

#### 2. Visualizing Damped Harmonic Motion
```python
import numpy as np
import matplotlib.pyplot as plt

# Parameters
A = 1.0  # Amplitude
omega = 2.0  # Angular frequency
gamma = 0.1  # Damping coefficient
t = np.linspace(0, 10, 1000)  # Time array

# Displacement as a function of time
x = A * np.exp(-gamma * t) * np.cos(omega * t)

# Plotting
plt.plot(t, x)
plt.xlabel('Time (s)')
plt.ylabel('Displacement (m)')
plt.title('Damped Harmonic Motion')
plt.show()
```

#### 3. Visualizing Electric Field Lines
```python
import numpy as np
import matplotlib.pyplot as plt

# Grid of points
x, y = np.meshgrid(np.linspace(-5, 5, 100), np.linspace(-5, 5, 100))

# Electric field components
Ex = x / (x**2 + y**2)**1.5
Ey = y / (x**2 + y**2)**1.5

# Plotting
plt.streamplot(x, y, Ex, Ey, color='b')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Electric Field Lines')
plt.show()
```

#### 4. Visualizing Magnetic Field of a Current Loop
```python
import numpy as np
import matplotlib.pyplot as plt

# Grid of points
x, y = np.meshgrid(np.linspace(-5, 5, 100), np.linspace(-5, 5, 100))

# Magnetic field components
Bx = -y / (x**2 + y**2)**1.5
By = x / (x**2 + y**2)**1.5

# Plotting
plt.streamplot(x, y, Bx, By, color='r')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Magnetic Field of a Current Loop')
plt.show()
```

#### 5. Visualizing Wave Interference
```python
import numpy as np
import matplotlib.pyplot as plt

# Parameters
k = 2 * np.pi / 1.0  # Wave number
omega = 2 * np.pi / 1.0  # Angular frequency
t = 0.0  # Time

# Grid of points
x, y = np.meshgrid(np.linspace(-5, 5, 100), np.linspace(-5, 5, 100))

# Wave functions
z1 = np.sin(k * x - omega * t)
z2 = np.sin(k * y - omega * t)
z = z1 + z2

# Plotting
plt.imshow(z, extent=(-5, 5, -5, 5), origin='lower', cmap='viridis')
plt.colorbar(label='Amplitude')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Wave Interference')
plt.show()
```
#### Example:
```python
import matplotlib.pyplot as plt

# Data for plotting
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Create a plot
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of y = x^2')
plt.show()
```

### 4. SymPy
SymPy is a Python library for symbolic mathematics. It can perform algebraic manipulations, calculus, and other symbolic computations.

#### Example:
```python
import sympy as sp

# Define a symbol
x = sp.symbols('x')

# Perform symbolic computation
expr = x**2 + 2*x + 1
expanded_expr = sp.expand(expr)
print("Expanded expression:", expanded_expr)
```

### 5. Pandas
Pandas is a powerful data manipulation and analysis library. It provides data structures like DataFrame for handling structured data.

#### Example:
```python
import pandas as pd

# Create a DataFrame
data = {'Mass': [1, 2, 3], 'Velocity': [10, 20, 30]}
df = pd.DataFrame(data)
print("DataFrame:\n", df)

# Calculate momentum
df['Momentum'] = df['Mass'] * df['Velocity']
print("DataFrame with Momentum:\n", df)
```
### Physics Examples with Pandas

#### 1. Analyzing Projectile Motion Data
```python
import pandas as pd

# Create a DataFrame with projectile motion data
data = {
    'Time (s)': [0, 1, 2, 3, 4, 5],
    'Height (m)': [0, 4.9, 9.8, 14.7, 19.6, 24.5],
    'Velocity (m/s)': [0, 9.8, 19.6, 29.4, 39.2, 49.0]
}
df = pd.DataFrame(data)
print("Projectile Motion Data:\n", df)

# Calculate the average height and velocity
average_height = df['Height (m)'].mean()
average_velocity = df['Velocity (m/s)'].mean()
print("Average Height:", average_height, "m")
print("Average Velocity:", average_velocity, "m/s")
```

#### 2. Analyzing Free Fall Data
```python
import pandas as pd

# Create a DataFrame with free fall data
data = {
    'Time (s)': [0, 1, 2, 3, 4, 5],
    'Distance (m)': [0, 4.9, 19.6, 44.1, 78.4, 122.5]
}
df = pd.DataFrame(data)
print("Free Fall Data:\n", df)

# Calculate the acceleration due to gravity
df['Acceleration (m/s^2)'] = df['Distance (m)'] / df['Time (s)']**2
print("Free Fall Data with Acceleration:\n", df)
```

#### 3. Analyzing Circular Motion Data
```python
import pandas as pd

# Create a DataFrame with circular motion data
data = {
    'Time (s)': [0, 1, 2, 3, 4, 5],
    'Angle (rad)': [0, 1.57, 3.14, 4.71, 6.28, 7.85],
    'Angular Velocity (rad/s)': [0, 1.57, 1.57, 1.57, 1.57, 1.57]
}
df = pd.DataFrame(data)
print("Circular Motion Data:\n", df)

# Calculate the average angular velocity
average_angular_velocity = df['Angular Velocity (rad/s)'].mean()
print("Average Angular Velocity:", average_angular_velocity, "rad/s")
```

#### 4. Analyzing Harmonic Motion Data
```python
import pandas as pd

# Create a DataFrame with harmonic motion data
data = {
    'Time (s)': [0, 1, 2, 3, 4, 5],
    'Displacement (m)': [0, 1, 0, -1, 0, 1],
    'Velocity (m/s)': [1, 0, -1, 0, 1, 0]
}
df = pd.DataFrame(data)
print("Harmonic Motion Data:\n", df)

# Calculate the maximum displacement and velocity
max_displacement = df['Displacement (m)'].max()
max_velocity = df['Velocity (m/s)'].max()
print("Maximum Displacement:", max_displacement, "m")
print("Maximum Velocity:", max_velocity, "m/s")
```
### 6. Astropy
Astropy is a package for astronomy-related computations. It includes tools for celestial mechanics, astrophysics, and cosmology.

#### Example:
```python
from astropy import units as u
from astropy.constants import G

# Define mass and radius
mass = 5.972e24 * u.kg  # Earth mass
radius = 6371 * u.km  # Earth radius

# Calculate gravitational force
force = G * mass / radius**2
print("Gravitational force:", force)
```

### 7. Pint
Pint is a Python package for handling physical quantities with units. It helps in performing unit conversions and calculations.

#### Example:
```python
import pint

# Create a unit registry
ureg = pint.UnitRegistry()

# Define quantities
distance = 100 * ureg.meter
time = 9.58 * ureg.second

# Calculate speed
speed = distance / time
print("Speed:", speed)
```

### 8. VPython
VPython is a module that allows users to create 3D animations and visualizations, which is useful for physics simulations.

#### Example:
```python
from vpython import sphere, vector

# Create a 3D sphere
ball = sphere(pos=vector(0, 0, 0), radius=1, color=color.red)
```

### 9. PyOpenGL
PyOpenGL is a cross-platform Python binding to OpenGL, which is used for rendering 2D and 3D vector graphics.

#### Example:
```python
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Initialize GLUT
glutInit()

# Create a window
glutCreateWindow('OpenGL Window')

# Define a display function
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.5, -0.5)
    glVertex2f(0.5, -0.5)
    glVertex2f(0.0, 0.5)
    glEnd()
    glFlush()

# Set the display function
glutDisplayFunc(display)

# Start the main loop
glutMainLoop()
```

### 10. PyMC3
PyMC3 is a Python library for probabilistic programming, which allows for Bayesian statistical modeling and probabilistic machine learning.

#### Example:
```python
import pymc3 as pm
import numpy as np

# Generate some data
np.random.seed(123)
data = np.random.randn(100)

# Define a model
with pm.Model() as model:
    mu = pm.Normal('mu', mu=0, sigma=1)
    sigma = pm.HalfNormal('sigma', sigma=1)
    y = pm.Normal('y', mu=mu, sigma=sigma, observed=data)
    
    # Perform inference
    trace = pm.sample(1000)

# Print the results
print(pm.summary(trace))
```

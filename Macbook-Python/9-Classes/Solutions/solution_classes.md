
## Solutions

```python
# 1. Projectile Motion
import math

class Projectile:
    def __init__(self, velocity, angle):
        self.velocity = velocity
        self.angle = math.radians(angle)
    
    def trajectory(self, time):
        g = 9.81  # acceleration due to gravity
        x = self.velocity * time * math.cos(self.angle)
        y = self.velocity * time * math.sin(self.angle) - 0.5 * g * time**2
        return x, y

# 2. Simple Harmonic Motion
class SimpleHarmonicMotion:
    def __init__(self, mass, spring_constant):
        self.mass = mass
        self.spring_constant = spring_constant
    
    def displacement(self, time, amplitude, phase):
        omega = math.sqrt(self.spring_constant / self.mass)
        return amplitude * math.cos(omega * time + phase)

# 3. Electric Circuit Analysis
class ElectricCircuit:
    def __init__(self, resistors):
        self.resistors = resistors
    
    def total_resistance_series(self):
        return sum(self.resistors)
    
    def total_resistance_parallel(self):
        return 1 / sum(1 / r for r in self.resistors)

# 4. Gravitational Force
class GravitationalForce:
    def __init__(self, mass1, mass2, distance):
        self.mass1 = mass1
        self.mass2 = mass2
        self.distance = distance
    
    def force(self):
        G = 6.67430e-11  # gravitational constant
        return G * self.mass1 * self.mass2 / self.distance**2

# 5. Kinematics
class Kinematics:
    def __init__(self, initial_velocity, acceleration):
        self.initial_velocity = initial_velocity
        self.acceleration = acceleration
    
    def final_velocity(self, time):
        return self.initial_velocity + self.acceleration * time
    
    def displacement(self, time):
        return self.initial_velocity * time + 0.5 * self.acceleration * time**2

# 6. Thermodynamics
class Thermodynamics:
    def __init__(self, mass1, temp1, mass2, temp2, specific_heat):
        self.mass1 = mass1
        self.temp1 = temp1
        self.mass2 = mass2
        self.temp2 = temp2
        self.specific_heat = specific_heat
    
    def final_temperature(self):
        return (self.mass1 * self.temp1 + self.mass2 * self.temp2) / (self.mass1 + self.mass2)

# 7. Optics
class Optics:
    def __init__(self, object_distance, image_distance):
        self.object_distance = object_distance
        self.image_distance = image_distance
    
    def focal_length(self):
        return 1 / (1 / self.object_distance + 1 / self.image_distance)

# 8. Fluid Mechanics
class FluidMechanics:
    def __init__(self, volume, fluid_density):
        self.volume = volume
        self.fluid_density = fluid_density
    
    def buoyant_force(self):
        g = 9.81  # acceleration due to gravity
        return self.volume * self.fluid_density * g

# 9. Rotational Dynamics
class RotationalDynamics:
    def __init__(self, mass, radius):
        self.mass = mass
        self.radius = radius
    
    def moment_of_inertia(self):
        return 0.5 * self.mass * self.radius**2

# 10. Wave Motion
class WaveMotion:
    def __init__(self, tension, linear_density):
        self.tension = tension
        self.linear_density = linear_density
    
    def wave_speed(self):
        return math.sqrt(self.tension / self.linear_density)
    
    def frequency(self, wavelength):
        return self.wave_speed() / wavelength

## Advanced Solutions

# 11. Quantum Mechanics
class QuantumMechanics:
    def __init__(self, principal_quantum_number):
        self.principal_quantum_number = principal_quantum_number
    
    def energy_level(self):
        h = 6.626e-34  # Planck's constant
        m = 9.109e-31  # mass of electron
        e = 1.602e-19  # elementary charge
        epsilon_0 = 8.854e-12  # permittivity of free space
        return - (m * e**4) / (8 * epsilon_0**2 * h**2 * self.principal_quantum_number**2)

# 12. Relativity
class Relativity:
    def __init__(self, velocity):
        self.velocity = velocity
    
    def time_dilation(self, proper_time):
        c = 3e8  # speed of light
        return proper_time / math.sqrt(1 - (self.velocity / c)**2)

# 13. Statistical Mechanics
class StatisticalMechanics:
    def __init__(self, energy_levels, temperature):
        self.energy_levels = energy_levels
        self.temperature = temperature
    
    def partition_function(self):
        k_B = 1.38e-23  # Boltzmann constant
        return sum(math.exp(-e / (k_B * self.temperature)) for e in self.energy_levels)
    
    def average_energy(self):
        k_B = 1.38e-23  # Boltzmann constant
        Z = self.partition_function()
        return sum(e * math.exp(-e / (k_B * self.temperature)) for e in self.energy_levels) / Z

# 14. Electromagnetic Waves
class ElectromagneticWaves:
    def __init__(self, frequency):
        self.frequency = frequency
    
    def wavelength(self):
        c = 3e8  # speed of light
        return c / self.frequency

# 15. Nuclear Physics
class NuclearPhysics:
    def __init__(self, mass_protons, mass_neutrons, mass_nucleus):
        self.mass_protons = mass_protons
        self.mass_neutrons = mass_neutrons
        self.mass_nucleus = mass_nucleus
    
    def binding_energy(self):
        c = 3e8  # speed of light
        mass_defect = (self.mass_protons + self.mass_neutrons - self.mass_nucleus)
        return mass_defect * c**2

# 16. Astrophysics
class Astrophysics:
    def __init__(self, radius, temperature):
        self.radius = radius
        self.temperature = temperature
    
    def luminosity(self):
        sigma = 5.67e-8  # Stefan-Boltzmann constant
        return 4 * math.pi * self.radius**2 * sigma * self.temperature**4

# 17. Plasma Physics
class PlasmaPhysics:
    def __init__(self, electron_temperature, electron_density):
        self.electron_temperature = electron_temperature
        self.electron_density = electron_density
    
    def debye_length(self):
        epsilon_0 = 8.854e-12  # permittivity of free space
        e = 1.602e-19  # elementary charge
        k_B = 1.38e-23  # Boltzmann constant
        return math.sqrt(epsilon_0 * k_B * self.electron_temperature / (self.electron_density * e**2))

# 18. Solid State Physics
class SolidStatePhysics:
    def __init__(self, potential_depth, lattice_spacing):
        self.potential_depth = potential_depth
        self.lattice_spacing = lattice_spacing
    
    def band_gap(self):
        h_bar = 1.055e-34  # reduced Planck's constant
        m = 9.109e-31  # mass of electron
        return 2 * self.potential_depth * (1 - math.cos(math.pi * h_bar / (self.lattice_spacing * math.sqrt(2 * m * self.potential_depth))))

# 19. Nonlinear Dynamics
class NonlinearDynamics:
    def __init__(self, sigma, rho, beta):
        self.sigma = sigma
        self.rho = rho
        self.beta = beta
    
    def lorenz(self, x, y, z, dt):
        dx = self.sigma * (y - x) * dt
        dy = (x * (self.rho - z) - y) * dt
        dz = (x * y - self.beta * z) * dt
        return x + dx, y + dy, z + dz

# 20. Cosmology
class Cosmology:
    def __init__(self, hubble_constant):
        self.hubble_constant = hubble_constant
    
    def age_of_universe(self):
        return 1 / self.hubble_constant

    
 
if __name__ == "__main__":
        # 1. Projectile Motion
        projectile = Projectile(velocity=50, angle=45)
        print("Projectile Trajectory at t=2s:", projectile.trajectory(2))

        # 2. Simple Harmonic Motion
        shm = SimpleHarmonicMotion(mass=1, spring_constant=10)
        print("SHM Displacement at t=1s:", shm.displacement(time=1, amplitude=5, phase=0))

        # 3. Electric Circuit Analysis
        circuit = ElectricCircuit(resistors=[10, 20, 30])
        print("Total Resistance in Series:", circuit.total_resistance_series())
        print("Total Resistance in Parallel:", circuit.total_resistance_parallel())

        # 4. Gravitational Force
        gravity = GravitationalForce(mass1=5.97e24, mass2=7.35e22, distance=3.84e8)
        print("Gravitational Force:", gravity.force())

        # 5. Kinematics
        kinematics = Kinematics(initial_velocity=0, acceleration=9.8)
        print("Final Velocity at t=5s:", kinematics.final_velocity(5))
        print("Displacement at t=5s:", kinematics.displacement(5))

        # 6. Thermodynamics
        thermo = Thermodynamics(mass1=1, temp1=100, mass2=1, temp2=0, specific_heat=4.18)
        print("Final Temperature:", thermo.final_temperature())

        # 7. Optics
        optics = Optics(object_distance=10, image_distance=20)
        print("Focal Length:", optics.focal_length())

        # 8. Fluid Mechanics
        fluid = FluidMechanics(volume=1, fluid_density=1000)
        print("Buoyant Force:", fluid.buoyant_force())

        # 9. Rotational Dynamics
        rotation = RotationalDynamics(mass=10, radius=2)
        print("Moment of Inertia:", rotation.moment_of_inertia())

        # 10. Wave Motion
        wave = WaveMotion(tension=100, linear_density=0.01)
        print("Wave Speed:", wave.wave_speed())
        print("Frequency for wavelength 2m:", wave.frequency(2))

        # 11. Quantum Mechanics
        quantum = QuantumMechanics(principal_quantum_number=1)
        print("Energy Level:", quantum.energy_level())

        # 12. Relativity
        relativity = Relativity(velocity=2.5e8)
        print("Time Dilation for proper time 1s:", relativity.time_dilation(1))

        # 13. Statistical Mechanics
        stats = StatisticalMechanics(energy_levels=[1e-21, 2e-21, 3e-21], temperature=300)
        print("Partition Function:", stats.partition_function())
        print("Average Energy:", stats.average_energy())

        # 14. Electromagnetic Waves
        em_wave = ElectromagneticWaves(frequency=5e14)
        print("Wavelength:", em_wave.wavelength())

        # 15. Nuclear Physics
        nuclear = NuclearPhysics(mass_protons=1.007276, mass_neutrons=1.008665, mass_nucleus=4.002603)
        print("Binding Energy:", nuclear.binding_energy())

        # 16. Astrophysics
        astro = Astrophysics(radius=6.96e8, temperature=5778)
        print("Luminosity:", astro.luminosity())

        # 17. Plasma Physics
        plasma = PlasmaPhysics(electron_temperature=1e5, electron_density=1e18)
        print("Debye Length:", plasma.debye_length())

        # 18. Solid State Physics
        solid = SolidStatePhysics(potential_depth=1e-18, lattice_spacing=1e-10)
        print("Band Gap:", solid.band_gap())

        # 19. Nonlinear Dynamics
        nonlinear = NonlinearDynamics(sigma=10, rho=28, beta=8/3)
        x, y, z = nonlinear.lorenz(1, 1, 1, 0.01)
        print("Lorenz System (x, y, z):", x, y, z)

        # 20. Cosmology
        cosmos = Cosmology(hubble_constant=70e3 / 3.086e19)
        print("Age of Universe:", cosmos.age_of_universe())

```

> ## Answer
> Projectile Trajectory at t=2s: (70.71067811865476, 51.090678118654736)

>SHM Displacement at t=1s: -4.998930364396629

>Total Resistance in Series: 60

>Total Resistance in Parallel: 5.454545454545454

>Gravitational Force: 1.986117532348633e+20

>Final Velocity at t=5s: 49.0

>Displacement at t=5s: 122.50000000000001

>Final Temperature: 50.0

>Focal Length: 6.666666666666666

>Buoyant Force: 9810.0

>Moment of Inertia: 20.0

>Wave Speed: 100.0

>Frequency for wavelength 2m: 50.0

>Energy Level: -2.1789580226488724e-18

>Time Dilation for proper time 1s: 1.8090680674665818

>Partition Function: 1.886786037677504

>Average Energy: 1.8405157390533322e-21

>Wavelength: 6e-07

>Binding Energy: -1.7879958e+17

>Luminosity: 3.846994382781468e+26

>Debye Length: 2.181960027615316e-05

>Band Gap: 3.547540870858275e-18

>Lorenz System (x, y, z): 1.0 1.26 0.9833333333333333

>Age of Universe: 440857142857142.9
# Physics Problems for Python Containers

## Problems

1. Calculate the average velocity of a car given its initial velocity of 10 m/s and final velocity of 20 m/s.
2. Determine the gravitational force between two masses of 5 kg and 10 kg separated by a distance of 2 meters.
3. Find the kinetic energy of an object with a mass of 2 kg moving at a velocity of 3 m/s.
4. Calculate the potential energy of an object with a mass of 2 kg at a height of 5 meters.
5. Determine the work done by a force of 10 N over a distance of 5 meters.
6. Calculate the power output of a machine that does 100 J of work in 5 seconds.
7. Find the acceleration of an object that goes from 0 m/s to 20 m/s in 4 seconds.
8. Determine the momentum of an object with a mass of 2 kg moving at a velocity of 3 m/s.
9. Calculate the impulse experienced by an object when a force of 10 N is applied for 2 seconds.
10. Find the frequency of a wave with a wavelength of 2 meters traveling at a speed of 340 m/s.
11. Determine the period of a pendulum with a length of 2 meters.
12. Calculate the electric force between two charges of 1e-6 C and 2e-6 C separated by a distance of 0.5 meters.
13. Find the electric field at a point 0.5 meters away from a point charge of 1e-6 C.
14. Determine the potential difference between two points in an electric field of 1000 N/C separated by a distance of 0.1 meters.
15. Calculate the capacitance of a parallel plate capacitor with an area of 1 m² and a separation of 0.01 meters.
16. Find the magnetic force on a charge of 1e-6 C moving at 10 m/s in a magnetic field of 0.1 T.
17. Determine the magnetic flux through a loop of wire with an area of 0.01 m² in a magnetic field of 0.1 T at an angle of 30 degrees.
18. Calculate the inductance of a coil with 100 turns, an area of 0.01 m², and a length of 0.1 meters.
19. Find the energy stored in an inductor with an inductance of 0.01 H and a current of 2 A.
20. Determine the resonant frequency of an LC circuit with an inductance of 0.01 H and a capacitance of 1e-6 F.
21. Calculate the pressure exerted by a fluid with a density of 1000 kg/m³ at a depth of 10 meters.
22. Find the buoyant force on an object with a volume of 0.01 m³ submerged in a fluid with a density of 1000 kg/m³.
23. Determine the flow rate of a fluid through a pipe with an area of 0.01 m² and a velocity of 2 m/s.
24. Calculate the heat transferred in a thermodynamic process for a mass of 1 kg with a specific heat of 4200 J/(kg K) and a temperature change of 10 K.
25. Find the efficiency of a heat engine that does 100 J of work with a heat input of 200 J.
26. Determine the entropy change in a reversible process where 100 J of heat is transferred at a temperature of 300 K.
27. Calculate the wavelength of light with a frequency of 5e14 Hz.
28. Find the energy of a photon with a wavelength of 500 nm.
29. Determine the refractive index of a medium where the speed of light is 2e8 m/s.
30. Calculate the focal length of a lens with object and image distances of 10 cm and 20 cm, respectively.

## Additional Problems Requiring For Loops

31. Calculate the sum of the first 10 natural numbers.
32. Determine the factorial of a given number, e.g., 5.
33. Find the sum of all even numbers between 1 and 20.
34. Calculate the average of a list of numbers: [2, 4, 6, 8, 10].
35. Determine the maximum value in a list of numbers: [3, 1, 4, 1, 5, 9, 2, 6, 5].
36. Find the number of occurrences of the number 3 in a list: [3, 1, 4, 3, 5, 3, 2, 3, 5].
37. Calculate the sum of the squares of the first 5 natural numbers.
38. Determine the product of all odd numbers between 1 and 10.
39. Find the sum of all prime numbers less than 20.
40. Calculate the Fibonacci sequence up to the 10th term.

## Physics concepts to solve above problems
### Mechanics
- **Velocity** is the rate of change of displacement. It is a vector quantity with both magnitude and direction.
    - Example: If a car moves from point A to point B, covering a distance of 100 meters in 10 seconds, its average velocity is $` v = \frac{100 \, \text{m}}{10 \, \text{s}} = 10 \, \text{m/s} `$. 
- **Acceleration** is the rate of change of velocity. It is also a vector quantity.
    - Example: If a car's velocity changes from 0 to 20 m/s in 4 seconds, its acceleration is $` a = \frac{20 \, \text{m/s} - 0 \, \text{m/s}}{4 \, \text{s}} = 5 \, \text{m/s}^2 `$. 

- **Newton's Laws of Motion**:
    - **First Law**: An object remains at rest or in uniform motion unless acted upon by a net external force.
    - **Second Law**: The force acting on an object is equal to the mass of that object times its acceleration $` ( F = ma ) `$. 
        - Example: A force of 10 N acting on a mass of 2 kg produces an acceleration of $` a = \frac{F}{m} = \frac{10 \, \text{N}}{2 \, \text{kg}} = 5 \, \text{m/s}^2 `$. 
    - **Third Law**: For every action, there is an equal and opposite reaction.

- **Work, Energy, and Power**:
    - **Work** is done when a force moves an object over a distance $` ( W = Fd ) `$. 
        - Example: If a force of 10 N moves an object 5 meters, the work done is $` W = 10 \, \text{N} \times 5 \, \text{m} = 50 \, \text{J} `$. 
    - **Kinetic Energy (KE)** is the energy of motion $` ( KE = \frac{1}{2} mv^2 ) `$. 
        - Example: An object with a mass of 2 kg moving at 3 m/s has $` KE = \frac{1}{2} \times 2 \, \text{kg} \times (3 \, \text{m/s})^2 = 9 \, \text{J} `$. 
    - **Potential Energy (PE)** is the energy stored due to position $` ( PE = mgh ) `$. 
        - Example: An object with a mass of 2 kg at a height of 5 meters has $` PE = 2 \, \text{kg} \times 9.8 \, \text{m/s}^2 \times 5 \, \text{m} = 98 \, \text{J} `$. 
    - **Power (P)** is the rate of doing work $` ( P = \frac{W}{t} ) `$. 
        - Example: A machine that does 100 J of work in 5 seconds has $` P = \frac{100 \, \text{J}}{5 \, \text{s}} = 20 \, \text{W} `$. 

- **Momentum and Impulse**:
    - **Momentum (p)** is the product of mass and velocity $` ( p = mv ) `$. 
        - Example: An object with a mass of 2 kg moving at 3 m/s has $` p = 2 \, \text{kg} \times 3 \, \text{m/s} = 6 \, \text{kg m/s} `$. 
    - **Impulse (J)** is the change in momentum resulting from a force applied over a time interval $` ( J = Ft ) `$. 
        - Example: A force of 10 N applied for 2 seconds gives an impulse of $` J = 10 \, \text{N} \times 2 \, \text{s} = 20 \, \text{Ns} `$. 

### Gravitation
- **Gravitational Force**:
    - Newton's law of universal gravitation states that every mass attracts every other mass with a force $` ( F = G \frac{m_1 m_2}{r^2} ) `$. 
        - Example: The gravitational force between two masses of 5 kg and 10 kg separated by 2 meters is $` F = 6.674 \times 10^{-11} \frac{5 \, \text{kg} \times 10 \, \text{kg}}{(2 \, \text{m})^2} = 8.34 \times 10^{-10} \, \text{N} `$. 

### Waves and Oscillations
- **Wave Properties**:
    - **Frequency (f)** is the number of waves passing a point per second $` ( f = \frac{v}{\lambda} ) `$. 
        - Example: A wave with a wavelength of 2 meters traveling at 340 m/s has $` f = \frac{340 \, \text{m/s}}{2 \, \text{m}} = 170 \, \text{Hz} `$. 
    - **Wavelength (\(\lambda\))** is the distance between successive crests of a wave.
    - **Speed (v)** of a wave is the product of its frequency and wavelength $` ( v = f\lambda ) `$. 

- **Simple Harmonic Motion**:
    - The **period (T)** of a pendulum is given by $` T = 2\pi \sqrt{\frac{L}{g}} `$. 
        - Example: A pendulum with a length of 2 meters has $` T = 2\pi \sqrt{\frac{2 \, \text{m}}{9.8 \, \text{m/s}^2}} \approx 2.83 \, \text{s} `$. 

### Electromagnetism
- **Electric Forces and Fields**:
    - **Electric Force (F)** between two charges is given by Coulomb's law $` ( F = k \frac{q_1 q_2}{r^2} ) `$. 
        - Example: The force between charges of $` 1 \times 10^{-6} \, \text{C} ` and $` 2 \times 10^{-6} \, \text{C} ` separated by 0.5 meters is $` F = 8.99 \times 10^9 \frac{(1 \times 10^{-6} \, \text{C})(2 \times 10^{-6} \, \text{C})}{(0.5 \, \text{m})^2} = 0.072 \, \text{N} `$. 
    - **Electric Field (E)** at a point is given by $` E = k \frac{q}{r^2} `$. 
        - Example: The electric field 0.5 meters away from a charge of $` 1 \times 10^{-6} \, \text{C} ` is $` E = 8.99 \times 10^9 \frac{1 \times 10^{-6} \, \text{C}}{(0.5 \, \text{m})^2} = 3.6 \times 10^4 \, \text{N/C} `$. 
    - **Potential Difference (V)** between two points in an electric field is $` V = Ed `$. 
        - Example: The potential difference in an electric field of 1000 N/C over a distance of 0.1 meters is $` V = 1000 \, \text{N/C} \times 0.1 \, \text{m} = 100 \, \text{V} `$. 

- **Capacitance**:
    - The **capacitance (C)** of a parallel plate capacitor is $` C = \frac{\epsilon_0 A}{d} `$. 
        - Example: A capacitor with an area of 1 m² and a separation of 0.01 meters has $` C = \frac{8.85 \times 10^{-12} \, \text{F/m} \times 1 \, \text{m}^2}{0.01 \, \text{m}} = 8.85 \times 10^{-10} \, \text{F} `$. 

- **Magnetic Forces and Fields**:
    - The **magnetic force (F)** on a moving charge is $` F = qvB `$. 
        - Example: A charge of $` 1 \times 10^{-6} \, \text{C} ` moving at 10 m/s in a magnetic field of 0.1 T experiences $` F = 1 \times 10^{-6} \, \text{C} \times 10 \, \text{m/s} \times 0.1 \, \text{T} = 1 \times 10^{-6} \, \text{N} `$. 
    - **Magnetic Flux (\(\Phi\))** through a loop is $` \Phi = B A \cos(\theta) `$. 
        - Example: A loop with an area of 0.01 m² in a magnetic field of 0.1 T at an angle of 30 degrees has $` \Phi = 0.1 \, \text{T} \times 0.01 \, \text{m}^2 \times \cos(30^\circ) \approx 8.66 \times 10^{-4} \, \text{Wb} `$. 

- **Inductance**:
    - The **inductance (L)** of a coil is $` L = \frac{\mu_0 N^2 A}{l} `$. 
        - Example: A coil with 100 turns, an area of 0.01 m², and a length of 0.1 meters has $` L = \frac{4\pi \times 10^{-7} \, \text{H/m} \times 100^2 \times 0.01 \, \text{m}^2}{0.1 \, \text{m}} = 1.26 \times 10^{-4} \, \text{H} `$. 
    - The **energy (E)** stored in an inductor is $` E = \frac{1}{2} L I^2 `$. 
        - Example: An inductor with an inductance of 0.01 H and a current of 2 A stores $` E = \frac{1}{2} \times 0.01 \, \text{H} \times (2 \, \text{A})^2 = 0.02 \, \text{J} `$. 

### Thermodynamics
- **Heat and Temperature**:
    - The **heat (Q)** transferred in a process is $` Q = mc\Delta T `$. 
        - Example: For a mass of 1 kg with a specific heat of 4200 J/(kg K) and a temperature change of 10 K, $` Q = 1 \, \text{kg} \times 4200 \, \text{J/(kg K)} \times 10 \, \text{K} = 42000 \, \text{J} `$. 

- **Thermodynamic Processes**:
    - **Efficiency (\(\eta\))** of a heat engine is $` \eta = \frac{W}{Q_H} `$. 
        - Example: An engine that does 100 J of work with a heat input of 200 J has $` \eta = \frac{100 \, \text{J}}{200 \, \text{J}} = 0.5 ` or 50%. 
    - **Entropy Change (\(\Delta S\))** in a reversible process is $` \Delta S = \frac{Q}{T} `$. 
        - Example: If 100 J of heat is transferred at a temperature of 300 K, $` \Delta S = \frac{100 \, \text{J}}{300 \, \text{K}} = 0.33 \, \text{J/K} `$. 

### Fluid Mechanics
- **Pressure and Buoyancy**:
    - **Pressure (P)** exerted by a fluid is $` P = \rho gh `$. 
        - Example: A fluid with a density of 1000 kg/m³ at a depth of 10 meters exerts $` P = 1000 \, \text{kg/m}^3 \times 9.8 \, \text{m/s}^2 \times 10 \, \text{m} = 98000 \, \text{Pa} `$. 
    - **Buoyant Force (F_b)** on a submerged object is $` F_b = \rho V g `$. 
        - Example: An object with a volume of 0.01 m³ submerged in a fluid with a density of 1000 kg/m³ experiences $` F_b = 1000 \, \text{kg/m}^3 \times 0.01 \, \text{m}^3 \times 9.8 \, \text{m/s}^2 = 98 \, \text{N} `$. 

- **Flow Rate**:
    - The **flow rate (Q)** of a fluid through a pipe is $` Q = A v `$. 
        - Example: A pipe with an area of 0.01 m² and a velocity of 2 m/s has $` Q = 0.01 \, \text{m}^2 \times 2 \, \text{m/s} = 0.02 \, \text{m}^3/\text{s} `$. 

### Optics
- **Light and Optics**:
    - The **wavelength (\(\lambda\))** of light is $` \lambda = \frac{c}{f} `$. 
        - Example: Light with a frequency of $` 5 \times 10^{14} \, \text{Hz} ` has $` \lambda = \frac{3 \times 10^8 \, \text{m/s}}{5 \times 10^{14} \, \text{Hz}} = 6 \times 10^{-7} \, \text{m} ` or 600 nm. 
    - The **energy (E)** of a photon is $` E = \frac{hc}{\lambda} `$. 
        - Example: A photon with a wavelength of 500 nm has $` E = \frac{6.626 \times 10^{-34} \, \text{Js} \times 3 \times 10^8 \, \text{m/s}}{500 \times 10^{-9} \, \text{m}} = 3.97 \times 10^{-19} \, \text{J} `$. 
    - The **refractive index (n)** of a medium is $` n = \frac{c}{v} `$. 
        - Example: A medium where the speed of light is $` 2 \times 10^8 \, \text{m/s} ` has $` n = \frac{3 \times 10^8 \, \text{m/s}}{2 \times 10^8 \, \text{m/s}} = 1.5 `$. 
    - The **focal length (f)** of a lens is given by $` \frac{1}{f} = \frac{1}{d_o} + \frac{1}{d_i} `$. 
        - Example: A lens with object and image distances of 10 cm and 20 cm has $` \frac{1}{f} = \frac{1}{10 \, \text{cm}} + \frac{1}{20 \, \text{cm}} = \frac{3}{20} \, \text{cm}^{-1} ` or $` f = \frac{20}{3} \, \text{cm} \approx 6.67 \, \text{cm} `$. 

### Modern Physics
- **Photon Energy**:
    - The **energy (E)** of a photon is related to its wavelength (\(\lambda\)) and frequency (f) by $` E = hf ` and $` E = \frac{hc}{\lambda} `$. 
        - Example: A photon with a wavelength of 500 nm has $` E = \frac{6.626 \times 10^{-34} \, \text{Js} \times 3 \times 10^8 \, \text{m/s}}{500 \times 10^{-9} \, \text{m}} = 3.97 \times 10^{-19} \, \text{J} `$. 

These concepts will help you solve the given physics problems effectively.

### Hints:
$$
 \text{average velocity} = \frac{\text{initial velocity} + \text{final velocity}}{2} 
$$

$$
F = G \frac{m_1 m_2}{r^2}
$$

$$
KE = \frac{1}{2} m v^2
$$

$$
PE = mgh
$$

$$
W = Fd
$$

$$
P = \frac{W}{t}
$$

$$
a = \frac{v_f - v_i}{t}
$$

$$
p = mv
$$

$$
J = Ft
$$

$$
f = \frac{v}{\lambda}
$$

$$
T = 2\pi \sqrt{\frac{L}{g}}
$$

$$
F = k \frac{q_1 q_2}{r^2}
$$

$$
E = k \frac{q}{r^2}
$$

$$
V = Ed
$$

$$
C = \frac{\epsilon_0 A}{d}
$$

$$
F = qvB
$$

$$
\Phi = B A \cos(\theta)
$$

$$
L = \frac{\mu_0 N^2 A}{l}
$$

$$
E = \frac{1}{2} L I^2
$$

$$
f = \frac{1}{2\pi \sqrt{LC}}
$$

$$
P = \rho gh
$$

$$
F_b = \rho V g
$$

$$
Q = A v
$$

$$
Q = mc\Delta T
$$

$$
\eta = \frac{W}{Q_H}
$$

$$
\Delta S = \frac{Q}{T}
$$

$$
\lambda = \frac{c}{f}
$$

$$
E = \frac{hc}{\lambda}
$$

$$
n = \frac{c}{v}
$$

$$
\frac{1}{f} = \frac{1}{d_o} + \frac{1}{d_i}$$

$$ \text{average velocity} = \frac{\text{initial velocity} + \text{final velocity}}{2} $$

$$
F = G \frac{m_1 m_2}{r^2}
$$

$$
KE = \frac{1}{2} m v^2
$$

$$
PE = mgh
$$

$$
W = Fd
$$

$$
P = \frac{W}{t}
$$

$$
a = \frac{v_f - v_i}{t}
$$

$$
p = mv
$$

$$
J = Ft
$$

$$
f = \frac{v}{\lambda}
$$

$$
T = 2\pi \sqrt{\frac{L}{g}}
$$

$$
F = k \frac{q_1 q_2}{r^2}
$$

$$
E = k \frac{q}{r^2}
$$

$$
V = Ed
$$

$$
C = \frac{\epsilon_0 A}{d}
$$

$$
F = qvB
$$

$$
\Phi = B A \cos(\theta)
$$

$$
L = \frac{\mu_0 N^2 A}{l}
$$

$$
E = \frac{1}{2} L I^2
$$

$$
f = \frac{1}{2\pi \sqrt{LC}}
$$

$$
P = \rho gh
$$

$$
F_b = \rho V g
$$

$$
Q = A v
$$

$$
Q = mc\Delta T
$$

$$
\eta = \frac{W}{Q_H}
$$

$$
\Delta S = \frac{Q}{T}
$$

$$
\lambda = \frac{c}{f}
$$

$$
E = \frac{hc}{\lambda}
$$

$$
n = \frac{c}{v}
$$

$$
\frac{1}{f} = \frac{1}{d_o} + \frac{1}{d_i}
$$



class User:
    def __init__(self, first_name, last_name, age, email, username):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.username = username

    def describe_user(self):
        
        print(f"User Profile:")
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"Username: {self.username}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back!")

# Example usage
user1 = User("John", "Doe", 30, "john.doe@example.com", "johndoe")
user1.describe_user()
user1.greet_user()


# Inheritance
class Particle:
    def __init__(self, position, velocity, mass):
        self.position = position
        self.velocity = velocity
        self.mass = mass

    def move(self, time):
        self.position[0] += self.velocity[0] * time
        self.position[1] += self.velocity[1] * time
        self.position[2] += self.velocity[2] * time

    def kinetic_energy(self):
        v_squared = sum(v**2 for v in self.velocity)
        return 0.5 * self.mass * v_squared

class ChargedParticle(Particle):
    def __init__(self, position, velocity, mass, charge):
        super().__init__(position, velocity, mass)
        self.charge = charge

    def electric_force(self, electric_field):
        return [self.charge * e for e in electric_field]

# Example usage
charged_particle = ChargedParticle([0, 0, 0], [1, 1, 1], 1.0, 1.6e-19)
print(f"Position: {charged_particle.position}")
print(f"Kinetic Energy: {charged_particle.kinetic_energy()}")
print(f"Electric Force: {charged_particle.electric_force([0, 0, 1e5])}")
# Adding a method to calculate the potential energy of the charged particle in an electric field
class ChargedParticle(Particle):
    def __init__(self, position, velocity, mass, charge):
        super().__init__(position, velocity, mass)
        self.charge = charge

    def electric_force(self, electric_field):
        return [self.charge * e for e in electric_field]

    def potential_energy(self, electric_potential):
        return self.charge * electric_potential

# Example usage
charged_particle = ChargedParticle([0, 0, 0], [1, 1, 1], 1.0, 1.6e-19)
print(f"Position: {charged_particle.position}")
print(f"Kinetic Energy: {charged_particle.kinetic_energy()}")
print(f"Electric Force: {charged_particle.electric_force([0, 0, 1e5])}")
print(f"Potential Energy: {charged_particle.potential_energy(1e5)}")

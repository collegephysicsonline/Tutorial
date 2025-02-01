# This code is designed to help physics students understand the concept of lists in Python
# using the example of fundamental forces in nature. It covers various list operations
# such as accessing elements, slicing, adding, removing, and sorting elements. Additionally,
# it introduces the concept of nested lists by associating fundamental forces with their
# interacting particles and demonstrates how to correlate two lists.


# List of fundamental forces in nature
fundamental_forces = ["Gravitational", "Electromagnetic", "Weak Nuclear", "Strong Nuclear"]

# Print the list
print("Fundamental Forces in Nature:", fundamental_forces)

# Accessing elements by index
print("First force:", fundamental_forces[0])
print("Last force:", fundamental_forces[-1])

# Slicing the list
print("First two forces:", fundamental_forces[:2])
print("Last two forces:", fundamental_forces[2:])

# Adding an element to the list
fundamental_forces.append("Fifth Force")
print("After appending a new force:", fundamental_forces)

# Inserting an element at a specific position
fundamental_forces.insert(2, "New Force")
print("After inserting a new force at index 2:", fundamental_forces)

# Removing an element from the list
fundamental_forces.remove("New Force")
print("After removing 'New Force':", fundamental_forces)

# Popping an element from the list
popped_force = fundamental_forces.pop()
print("Popped force:", popped_force)
print("After popping the last force:", fundamental_forces)

# Finding the index of an element
index_of_weak = fundamental_forces.index("Weak Nuclear")
print("Index of 'Weak Nuclear':", index_of_weak)

# Counting occurrences of an element
count_of_strong = fundamental_forces.count("Strong Nuclear")
print("Count of 'Strong Nuclear':", count_of_strong)

# Sorting the list
fundamental_forces.sort()
print("Sorted list of forces:", fundamental_forces)

# Reversing the list
fundamental_forces.reverse()
print("Reversed list of forces:", fundamental_forces)

# Extending the list with another list
additional_forces = ["Hypothetical Force 1", "Hypothetical Force 2"]
fundamental_forces.extend(additional_forces)
print("After extending with additional forces:", fundamental_forces)

# Clearing the list
fundamental_forces.clear()
print("After clearing the list:", fundamental_forces)
# Nested list: Fundamental forces and their interacting particles
forces_and_particles = [
    ["Gravitational", ["Graviton"]],
    ["Electromagnetic", ["Photon"]],
    ["Weak Nuclear", ["W and Z bosons"]],
    ["Strong Nuclear", ["Gluon"]]
]

# Print the nested list
print("Forces and their interacting particles:", forces_and_particles)

# Accessing elements in the nested list
print("Particles for Electromagnetic force:", forces_and_particles[1][1])

# Adding a new force with its particles
forces_and_particles.append(["Fifth Force", ["Hypothetical Particle"]])
print("After adding a new force with particles:", forces_and_particles)

# Removing a force with its particles
forces_and_particles.remove(["Fifth Force", ["Hypothetical Particle"]])
print("After removing the new force with particles:", forces_and_particles)

# Correlating two lists: Forces and their intermediate particles
intermediate_particles = ["Graviton", "Photon", "W and Z bosons", "Gluon"]
correlations = list(zip(fundamental_forces, intermediate_particles))
print("Correlations between forces and intermediate particles:", correlations)

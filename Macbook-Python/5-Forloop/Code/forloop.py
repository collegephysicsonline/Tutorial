# forloop.py

# Example 1: Simple for loop to iterate over a list
physics_concepts = ["Newton's Laws", "Thermodynamics", "Electromagnetism", "Quantum Mechanics", "Relativity"]

print("Physics Concepts:")
for concept in physics_concepts:
    print(concept)

# Example 2: Using range() to iterate over list indices
print("\nPhysics Concepts with Indices:")
for i in range(len(physics_concepts)):
    print(f"{i}: {physics_concepts[i]}")

# Example 3: Using enumerate() to get index and value
print("\nPhysics Concepts with Enumerate:")
for index, concept in enumerate(physics_concepts):
    print(f"{index}: {concept}")

# Example 4: Using list comprehension to create a new list
concept_lengths = [len(concept) for concept in physics_concepts]
print("\nLength of each Physics Concept:")
print(concept_lengths)

# Example 5: Nested for loop to compare elements
print("\nComparing Physics Concepts:")
for i in range(len(physics_concepts)):
    for j in range(i + 1, len(physics_concepts)):
        print(f"Comparing {physics_concepts[i]} with {physics_concepts[j]}")

# Example 6: Using for loop with conditionals
print("\nPhysics Concepts with more than 10 characters:")
for concept in physics_concepts:
    if len(concept) > 10:
        print(concept)
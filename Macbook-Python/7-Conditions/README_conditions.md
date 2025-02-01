# Introduction to Conditional Statements in Python

In this section, we will explore conditional statements in Python, which allow us to execute certain pieces of code based on specific conditions. This is a crucial concept in programming, as it enables us to control the flow of our programs and make decisions within our code.

## Conditional Statements
### `if` Statement
The `if` statement is used to test a condition. If the condition evaluates to `True`, the code block under the `if` statement is executed. Otherwise, it is skipped.

```python
if condition:
    # code block to execute if condition is True
```

### `else` Statement
The `else` statement can be used in conjunction with the `if` statement to execute a code block if the condition is `False`.

```python
if condition:
    # code block to execute if condition is True
else:
    # code block to execute if condition is False
```

### `elif` Statement
The `elif` (short for "else if") statement allows us to check multiple conditions.

```python
if condition1:
    # code block to execute if condition1 is True
elif condition2:
    # code block to execute if condition1 is False and condition2 is True
else:
    # code block to execute if both condition1 and condition2 are False
```

### `while` Loop
The `while` loop allows us to execute a block of code repeatedly as long as a condition is `True`.

```python
while condition:
    # code block to execute while condition is True
```
### Flowchart for Conditional Statements

Below is a flowchart that explains the flow of the `if`, `elif`, and `else` statements:

```mermaid
graph TD
    A[Start] --> B{condition1}
    B -- True --> C[Execute code block for condition1]
    B -- False --> D{condition2}
    D -- True --> E[Execute code block for condition2]
    D -- False --> F[Execute code block for else]
    C --> G[End]
    E --> G[End]
    F --> G[End]
```

This flowchart demonstrates how the program evaluates each condition in sequence and executes the corresponding code block based on whether the conditions are `True` or `False`.

## Flowchart for `while` Loop

Below is a flowchart that explains the flow of the `while` loop:

```mermaid
graph TD
    A[Start] --> B{condition}
    B -- True --> C[Execute code block]
    C --> B
    B -- False --> D[End]
```

This flowchart demonstrates how the program repeatedly executes the code block as long as the condition is `True`. Once the condition evaluates to `False`, the loop terminates, and the program proceeds to the next part of the code.

## Connecting with Previous Concepts

### Variables
We can use variables to store the conditions we want to test in our `if` and `while` statements.

```python
temperature = 25
if temperature > 20:
    print("It's warm outside.")
```

### Lists and Tuples
We can use conditional statements to iterate over lists and tuples and perform actions based on their elements.

```python
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    if number % 2 == 0:
        print(f"{number} is even.")
```

### Sets and Dictionaries
Conditional statements can also be used to check for the presence of elements in sets and dictionaries.

```python
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
    print("Apple is in the set.")

student_grades = {"Alice": 85, "Bob": 90}
if "Alice" in student_grades:
    print(f"Alice's grade is {student_grades['Alice']}.")
```

By understanding and utilizing conditional statements, you will be able to create more dynamic and responsive programs. This will build on your knowledge of variables, lists, tuples, sets, and dictionaries, allowing you to write more complex and efficient code.

### Physics Examples

Let's apply conditional statements to some physics-related examples.

#### Example 1: Checking Velocity

```python
velocity = 30  # in meters per second
if velocity > 20:
    print("The object is moving fast.")
else:
    print("The object is moving slow.")
```

#### Example 2: Determining Energy State

```python
energy = 50  # in joules
if energy > 100:
    print("High energy state.")
elif energy > 50:
    print("Medium energy state.")
else:
    print("Low energy state.")
```

#### Example 3: Looping Through Forces

```python
forces = [10, 20, 30, 40]  # in newtons
for force in forces:
    if force > 25:
        print(f"{force}N is a strong force.")
    else:
        print(f"{force}N is a weak force.")
```

### Flowchart for Conditional Statements

Below is a flowchart that explains the flow of the `if`, `elif`, and `else` statements in the context of checking velocity:

```mermaid
graph TD
    A[Start] --> B{velocity > 20}
    B -- True --> C[Print "The object is moving fast."]
    B -- False --> D[Print "The object is moving slow."]
    C --> E[End]
    D --> E[End]
```

This flowchart demonstrates how the program evaluates the velocity condition and executes the corresponding print statement based on whether the condition is `True` or `False`.

### Flowchart for `while` Loop

Below is a flowchart that explains the flow of a `while` loop in the context of reducing energy:

```mermaid
graph TD
    A[Start] --> B{energy > 0}
    B -- True --> C[Reduce energy by 10]
    C --> B
    B -- False --> D[End]
```

This flowchart demonstrates how the program repeatedly reduces the energy value as long as the condition is `True`. Once the condition evaluates to `False`, the loop terminates, and the program proceeds to the next part of the code.

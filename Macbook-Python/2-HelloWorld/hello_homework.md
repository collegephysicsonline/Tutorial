# Homework: Hello World in Python

## Objective
Learn how to use the `print()` function in Python to display text on the screen.

## For Practice

1. **Basic Hello World**
    - Write a Python program that prints "Hello, World!" to the console.
    ```python
    print("Hello, World!")
    ```

2. **Personalized Greeting**
    - Modify the program to print a personalized greeting. For example, if your name is John, the output should be "Hello, John!".
    ```python
    name = "John"
    print(f"Hello, {name}!")
    ```

3. **Multiple Lines**
    - Write a Python program that prints the following text on separate lines:
      ```
      Hello, World!
      Welcome to Python programming.
      ```
    ```python
    print("Hello, World!")
    print("Welcome to Python programming.")
    ```

4. **Using Variables**
    - Store the greeting message in a variable and then print it.
    ```python
    message = "Hello, World!"
    print(message)
    ```

## Problem to solve


5. **Combining Strings**
    - Write a program that combines two strings and prints the result. For example, combine "Hello" and "World" to print "Hello World".
 

6. **Printing Quotes**
    - Write a Python program that prints a quote. For example, print "The only limit to our realization of tomorrow is our doubts of today." - Franklin D. Roosevelt.

7. **Escape Characters**
    - Write a Python program that prints a string with a newline character and a tab character. For example:
    ```
    Hello,
    World!
    ```

8. **Printing a Backslash**
    - Write a Python program that prints a string containing a backslash. For example, print "This is a backslash: \\".

9. **Formatted Strings**
    - Write a Python program that uses formatted strings to print the result of a calculation. For example, print "The result of 5 + 3 is 8".

10. **Printing a Multiline String**
    - Write a Python program that prints a multiline string using triple quotes. For example:
    ```
    This is a multiline string.
    It can span multiple lines.
    ```



    ## User Input

    11. **Basic Input**
        - Write a Python program that asks the user for their name and then prints a greeting message. For example:
        ```python
        name = input("Enter your name: ")
        print(f"Hello, {name}!")
        ```

    12. **Numerical Input**
        - Write a Python program that asks the user for a number, adds 10 to it, and then prints the result. For example:
        ```python
        number = int(input("Enter a number: "))
        result = number + 10
        print(f"The result is {result}")
        ```

    ## Modulo Operator

    13. **Even or Odd**
        - Write a Python program that asks the user for a number and then prints whether the number is even or odd. For example:
        ```python
        number = int(input("Enter a number: "))
        if number % 2 == 0:
            print("The number is even.")
        else:
            print("The number is odd.")
        ```

    14. **Remainder Calculation**
        - Write a Python program that asks the user for two numbers and then prints the remainder when the first number is divided by the second number. For example:
        ```python
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        remainder = num1 % num2
        print(f"The remainder is {remainder}")
        ```
        ## More Applications of `input()` Functions

        15. **Basic Calculator**
            - Write a Python program that asks the user for two numbers and then prints the sum, difference, product, and quotient of the numbers. For example:
            ```python
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            sum = num1 + num2
            difference = num1 - num2
            product = num1 * num2
            quotient = num1 / num2
            print(f"The sum is {sum}")
            print(f"The difference is {difference}")
            print(f"The product is {product}")
            print(f"The quotient is {quotient}")
            ```

        16. **Age in Future**
            - Write a Python program that asks the user for their current age and then prints what their age will be in 10 years. For example:
            ```python
            age = int(input("Enter your current age: "))
            future_age = age + 10
            print(f"In 10 years, you will be {future_age} years old.")
            ```

        17. **Temperature Conversion**
            - Write a Python program that asks the user for a temperature in Celsius and then converts it to Fahrenheit. For example:
            ```python
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = (celsius * 9/5) + 32
            print(f"The temperature in Fahrenheit is {fahrenheit}")
            ```

        18. **Simple Interest Calculator**
            - Write a Python program that asks the user for the principal amount, rate of interest, and time period, then calculates and prints the simple interest. For example:
            ```python
            principal = float(input("Enter the principal amount: "))
            rate = float(input("Enter the rate of interest: "))
            time = float(input("Enter the time period in years: "))
            simple_interest = (principal * rate * time) / 100
            print(f"The simple interest is {simple_interest}")
            ```

        19. **BMI Calculator**
            - Write a Python program that asks the user for their weight (in kilograms) and height (in meters), then calculates and prints their Body Mass Index (BMI). For example:
            ```python
            weight = float(input("Enter your weight in kilograms: "))
            height = float(input("Enter your height in meters: "))
            bmi = weight / (height ** 2)
            print(f"Your BMI is {bmi}")
            ```

        20. **Distance Converter**
            - Write a Python program that asks the user for a distance in kilometers and then converts it to miles. For example:
            ```python
            kilometers = float(input("Enter distance in kilometers: "))
            miles = kilometers * 0.621371
            print(f"The distance in miles is {miles}")
            ```

## Submission
- Save your Python programs in a file named `hello_homework.py`.
- Submit the file to your instructor by the due date.

## Additional Resources
- [Python print() function](https://docs.python.org/3/library/functions.html#print)

Happy Coding!


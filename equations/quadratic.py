# solve quadratic equations with discriminant

from math import sqrt

# Create coefficients for equation
a = int(input("a? "))
b = int(input("b? "))
c = int(input("c? "))

"""
Description: calculatics discriminant for equation.

Return: INT D

Parameters: INT a, INT b, INT c
"""

def discriminant(a, b, c):
    D = (b ** 2) - (4 * a * c)
    return D

"""
Description: found roots of quadratic equation and print results.

Return: -

Parameters: INT D, INT a, INT b
"""

def solve(D, a, b):
    if D == 0:
        result = -b / (2 * a)
        print(f"Answer: {result}")
    else:
        sqrt_D = sqrt(D)
        result_1 = (-b + sqrt_D) / (2 * a)
        result_2 = (-b - sqrt_D) / (2 * a)
        print(f"Answers: {result_1} and {result_2}")

"""
Description: start programm

Return: -

Parameters: -
"""

def check():
    D = discriminant(a, b, c)
    if D < 0:
        print("No real roots")
    else:
        solve(D, a, b)

check()

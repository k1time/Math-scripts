# This script generate random math functions

from random import randint
from math import sqrt

func_structures = ["linear", "quadratic", "power", "quadratic_parabola", "hyperbola", "sqrt_func"]

"""
Description: functions creates a values for math functions

Return: random number after math calculations
"""

def generate_linear(a, x, b):
    return a * x + b 

def generate_quadratic(a, x, b, c):
    return a * (x ** 2) + b * x + c

def generate_power(x):
    return x ** x

def generate_quadratic_parabola(x):
    return x ** 2

def generate_hyperbola(x):
    return 1 / x

def generate_sqrt_func(x):
    return sqrt(x)

"""
Description: function get_func() return random name of function

Return: name of function
"""

def get_func(data):
    index = randint(0, len(data) - 1)
    return data[index], index

"""
Description: function get_result() returns a math function

Return: math function
"""

def get_result(func_type, a, x, b, c):
    if func_type == "linear":
        return generate_linear(a, x, b)
    elif func_type == "quadratic":
        return generate_quadratic(a, x, b, c)
    elif func_type == "quadratic_parabola":
        return generate_quadratic_parabola(x)
    elif func_type == "hyperbola":
        return generate_hyperbola(x)
    elif func_type == "sqrt_func":
        return generate_sqrt_func(x)
    else:
        return generate_power(x)
    
"""
Description: function get_write_func() create a form of math function

Return: form of math function
"""

def get_write_func(func_type):
    if func_type == "linear":
        return "f(x) = ax + b"
    elif func_type == "quadratic":
        return "f(x) = ax^2 + bx + c"
    elif func_type == "quadratic_parabola":
        return "f(x) = x^2"
    elif func_type == "hyperbola":
        return "f(x) = 1/x"
    elif func_type == "sqrt_func":
        return "f(x) = √(x)"
    else:
        return "f(x) = x^x"

"""
Start programm from there. Create random a, b, c, x and random math function. Write result of programm
"""

a, b, c, x = randint(1, 1000), randint(1, 1000), randint(1, 1000), randint(1, 100)
selected_func, index = get_func(func_structures)
result = get_result(selected_func, a, x, b, c)
func = get_write_func(selected_func)

print(f"Random function: '{func}'. Answer:  {result}")

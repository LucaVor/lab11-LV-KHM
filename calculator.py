# https://github.com/LucaVor/lab11-LV-KHM
# Partner 1: Luca Voros
# Partner 2: ...

import math

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

def square_root(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a

def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError
    return math.log(b, a)

def exponent(a, b):
    return a ** b
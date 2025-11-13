# https://github.com/LucaVor/lab11-LV-KHM
# Partner 1: Luca Voros
# Partner 2: Kiro Habib

import math
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if not (a < 0 or a > 0):
        raise[ZeroDivisionError]
    else:
        return b/a # raise ZeroDivisionError if a == 0

def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError
    return math.log(b, a)

def exp(a, b):
    return a**b


def square_root(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)
"""mymath - our math example module"""

pi = 3.14159


def area(r):
    """area(r): return the area of a circle with radius r."""
    global pi
    return pi * r * r

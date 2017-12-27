#!/usr/bin/env python3

# ax2+bx+c=0 


import math

def quadratic(a, b, c):
    for n in (a, b, c):
        if not isinstance(n, (int, float)):
            raise TypeError('bad operand type, please input numbers')
    if (a == 0):
        if (b == 0):
            return 'not an equation'
        else:
            x = -c / b
            return x
    else:
        delta = b*b - 4*a*c
        if (delta > 0):
            x1 = (-b + math.sqrt(delta)) / 2*a
            x2 = (-b - math.sqrt(delta)) / 2*a
            return x1, x2
        elif (delta == 0):
            x = (-b + math.sqrt(delta)) / 2*a
            return x
        else:
            return 'None solution'


# test
print(quadratic(0, 0, 2))
print(quadratic(0, 1, 2))
print(quadratic(3, 1, 2))
print(quadratic(3, 6, 2))
print(quadratic(4, 8, 4))
print(quadratic(2, 3, 1))
print(quadratic(1, 3, -4))
print(quadratic(0, 1, 2))
print(quadratic('A', 'b', 'c'))

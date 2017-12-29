#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 输出斐波那契数列的前N个数

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'


# test
fib(6)


# generator
def fib_generator(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

# test
print('generator test')
fib(10)

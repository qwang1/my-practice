#!/usr/bin/env python3

# -*- coding: utf-8 -*-

# 可接收一个或多个数并计算乘积
def product(*args):
    x = 1
    for n in args:
        x = x * n  
    return x


# test
print(product(1))
print(product(1, 2))
print(product(1, 2, 3, 4, 5))

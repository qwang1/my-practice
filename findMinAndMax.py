#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 查找List中的最大值和最小值

def findMinAndMax(L):
    if len(L) == 0:
        return None, None
    min = L[0]
    max = L[0]
    for x in L:
        if x < min:
            min = x
        if x > max:
            max = x
    return min, max


# test
L = list(range(20))
print(findMinAndMax(L))

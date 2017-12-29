#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 杨辉三角

def triangles(n):
    L = [1]
    while True:
        yield L
        L = [L[x] + L[x+1] for x in range(len(L)-1)]
        L.insert(0, 1)
        L.append(1)
        if len(L) > 10:
            break

# test
t = triangles(10)
for i in t:
    print(i)

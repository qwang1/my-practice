#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456

from functools import reduce

def str2float(s):
    def char2nums(s):
        DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.': '.'}
        return DIGITS[s]
    def str2int(x, y):
        return x * 10 + y
    def str2dec(x, y):
        return x / 10 + y
    integer, decimal = s.split('.', 1)
    return reduce(str2int, map(char2nums, integer)) + reduce(str2dec, map(char2nums, decimal[::-1])) * 0.1  


# test 
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']


def normalize(name):
    if not isinstance(name, str):
        raise TypeError('bad operand type')
    return name.title()


# test
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)    


# Tips: Python为string对象提供了转换大小写的方法：upper() 和 lower()。首字母大写，其余小写的capitalize()方法，以及所有单词首字母大写，其余小写的title()方法。

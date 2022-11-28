#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 递归 vs 非递归
# @Time    : 2022/11/28 11:02 上午
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

"""
ref: https://nanxiao.me/recursive-vs-non-recursive/
"""

def Fibonacci(n):
    if n <= 1:
        return n
    return Fibonacci(n - 1) + Fibonacci(n - 2)


print("Fibonacci recursion: {}".format(Fibonacci(10)))


def Fibonacci2(n):
    # if n <= 1:
    #     return n
    fi = 0
    fj = 1
    # for (int i = 2; i <= n; i++) python range 不包括后半，所以 rang(1, n) 循环次数是一样的
    for i in range(1, n):
        temp = fi + fj
        fi = fj
        fj = temp
    return fj


print("Fibonacci no recursion: {}".format(Fibonacci2(10)))


















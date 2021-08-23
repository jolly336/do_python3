#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 匿名函数 Lambda
# @Time    : 2019/4/21 下午4:39
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

"""
* lambda 表达式-匿名函数

> 本章节函数式的语法和技巧是个人推荐的，也是 Python 比较好的编码方式

匿名函数：定义一个函数，不需要定义函数名字

# expression 是表达式，不是代码块，代码块很大，代码块可以写复杂的逻辑 if else 等
lambda parameter_list:expression

* 三元表达式



"""


# 表达式，不是代码块，代码块很大
# lambda parameter_list:expression

def add(x, y):
    return x + y


print(add(1, 2))  # 3
f = lambda x, y: x + y  # 把函数赋值给变量，这种是没意义的，还是把函数赋值了个名字
# f = lambda x, y: a = x + y # Error: a = x + y 是个语句，不是表达式
print(f(1, 2))  # 3

# 回忆一下：之前学习的章节哪个适合用匿名函数？-> 正则

# 三元表达式 x > y ? x : y
# 条件为真时返回的结果 if 条件判断 else 条件为假时的返回结果

x = 2
y = 3

r = x if x > y else y  # 其他语言 x > y ? x : y
print(r)

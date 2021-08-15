#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 身份运算符 is、is not
# @Time    : 2019/4/7 下午2:51
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

"""
is 和 == 的区别是啥？

关系运算符 == 是比较值是否相等，is 不是比较值相等，is 比较的是两个变量的身份是否相等（内存地址）
"""

a = 1  # 当两个变量取值相等时，is 才返回 true
b = 2
print(a is b)

a = 1
b = 1
print(a == b)
print(a is b)

# 关系运算符 == 是比较值是否相等，is 不是比较值相等，is 比较的是两个变量的身份是否相等（内存地址）
a = 1
b = 1.0
print(a == b)  # True，关系运算符，是相等的
print(a is b)  # False

print(id(a))
print(id(b))

# 集合是无序的，取值是相等的，无序的！
a = {1, 2, 3}
b = {2, 1, 3}
print(a == b)  # True
print(a is b)  # Flase

# 元组是序列！顺序会影响到取值判断的 ==
c = (1, 2, 3)
d = (2, 1, 3)
print(c == d)  # False
print(c is d)  # False

# 类型判断
a = 'hello'
# type + 关系运算符，不推荐使用这种方式！
print(type(a) == int)
print(type(a) == str)

# 推荐：使用 isinstance
# 面向对象：isinstance 可以判断子类属于哪个对象，type不可以
print(isinstance(a, str))
# 判断 a是否后面元组中的任意一种
print(isinstance(a, (int, str, float)))

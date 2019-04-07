#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 身份运算符 is、is not
# @Time    : 2019/4/7 下午2:51
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

a = 1
b = 2
print(a is b)

a = 1
b = 1
print(a == b)
print(a is b)

# 值是否相等，is 不是比较值相等，is 比较的是两个变量的身份是否相等（内存地址）
a = 1
b = 1.0
print(a == b)  # True
print(a is b)  # False

print(id(a))
print(id(b))

# 集合是无序的，取值是相等的
a = {1, 2, 3}
b = {2, 1, 3}
print(a == b)  # True
print(a is b)  # Flase

# 元组是序列！
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
print(isinstance(a, str))
# 判断 a是否后面元组中的任意一种
print(isinstance(a, (int, str, float)))



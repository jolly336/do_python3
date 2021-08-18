#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : None
# @Time    : 2019/4/21 下午9:11
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me


# None 空

# None不等于：空字符串、空的列表 0 False
# 类型，值

a = ''
b = False
c = []

print(a == None)
print(b == None)
print(c == None)

print(a is None)

# <class 'NoneType'>
# 空也是一个对象
print(type(None))


# 判空

# a
# if not a
# if a is None

def fun():
    return None


# a = fun()
a = []

if not a: # not 逻辑运算，结果得到False
    print('S')
else:
    print('F')

if a is None:
    print('S')
else:
    print('F')

# 推荐判空操作

# if a:
# if not a:

# 当a为如下情况时，都可以生效

a =  None
a = ''
a = []
a = False


# None False 类型不同
# '不存在' '真假'


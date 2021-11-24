#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : None
# @Time    : 2019/4/21 下午9:11
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me


'''
# None 空

# None 不等于：空字符串、空的列表 0 False
# 1）类型上不一样；2）值，取值，值的比较上也是不一样的；
（类型、值）

推荐：
对 None、''、[]、False 这些判断都使用判断，区别 None 类型：

if a
if not
'''

a = ''
b = False
c = []

# 1）值不一样的
print(a == None)  # False
print(b == None)  # False
print(c == None)  # False

# 2）类型不一样，Python 的 None 本身也是一个对象，它也是一个类型
print(a is None)  # False

# <class 'NoneType'>
# 空也是一个对象，一切皆对象！
print(type(None))  # <class 'NoneType'>


# 判空，列表判空

# 变量 a，not a 和 a is None 区别？看上去没啥区别，但区别是很大的。
# a
# if not a
# if a is None

def fun():
    return None


# 测试：第一种函数返回 None，第二种 a 是个空列表
a = fun()
# a = []

# not a 对于空列表 []，not 会对列表进行逻辑运算，结果得到 bool 值
if not a:  # not 逻辑运算，结果得到 False
    print('S')
else:
    print('F')

if a is None:
    print('S')
else:
    print('F')

# 推荐判空操作 if a, not a

# if a:
# if not a:

# 当 a 为如下情况时，使用 if a, if not a 判断都可以生效！！！

a = None
a = ''
a = []
a = False

# None False 类型不同
# '不存在' '真假'

# 很多时候我们使用 if None 和 if False 得到相同的结果，但结果相同不代表它们本质和意义是相同的。
# if None
# if False

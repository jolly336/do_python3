#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 闭包-是一种辅助的编程方式
# @Time    : 2019/4/21 下午3:56
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

# 闭包 = 函数 + 环境变量(函数定义时候)
# 现场

# 旅行者 x,y，不断计算出旅行者位置

# x = 0
# 3 result = 3
# 5 result = 8
# 6 result = 14

# 1. 一个错误误区
# origin = 0
#
# def go(step):
#     # UnboundLocalError: local variable 'origin' referenced before assignment
#     new_pos = origin + step
#     # origin被赋值，认为局部变量
#     origin = new_pos
#     return origin
#
# print(go(2))
# print(go(3))
# print(go(6))

# 2. global 设置全局变量
origin = 0


def go(step):
    global origin
    new_pos = origin + step
    origin = new_pos
    return new_pos


print(go(2))
print(go(3))
print(go(6))

# 3. 闭包实现

# 闭包可以保存环境变量的状态，记忆上次调用的状态
# 闭包所有的修改都局限在方法的内部，而global会修改全局变量，很糟糕
# 闭包的环境变量需要常驻内存，会容易引起内存泄漏

origin = 0

def factory(pos):
    def go(step):
        # 声明不是局部变量
        nonlocal pos
        new_pos = pos + step
        pos = new_pos
        return new_pos

    return go


tourist = factory(origin)
print(tourist(2))
print(origin)
print(tourist.__closure__[0].cell_contents)
print(tourist(3))
print(origin)
print(tourist.__closure__[0].cell_contents)
print(tourist(5))
print(origin)
print(tourist.__closure__[0].cell_contents)

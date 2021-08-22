#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 用字典实现枚举类型
# @Time    : 2019/4/20 下午7:34
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

"""
思考：如果没有枚举，你会怎么表示这个类型？字典？

# 上面的字典和类，都有一个问题就是：可变的，在代码里可以轻易更改值；
# 第二个问题是：没有防止相同标签的功能

"""

# 全局变量，实现，不好
# 法一：全局变量，系统性编程还需要加强下
yellow = 1
greeen = 2

# 法二：字典，最切近枚举类型
a = {'yellow': 1, 'green': 2}
a['yellow'] = 3  # 改变字典的取值


# 法三：类，用数据结构-字典或者类来封装下数据，是有一定的编程的~
class TypeDiamond():
    yellow = 1
    greeen = 2

# 上面的字典和类，都有一个问题就是：可变的，在代码里可以轻易更改值；
# 第二个问题是：没有防止相同标签的功能

# 枚举和普通类相比有什么优势？

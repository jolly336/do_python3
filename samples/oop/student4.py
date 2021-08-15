#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 类-Python机制
# @Time    : 2019/4/14 下午12:14
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

# 面向对象
# 有意义的面向对象的代码
# 类 = 面向对象
# 类、对象
# 类最基本的作用：封装
# 类和对象

# 类：首字母大写，驼峰式命名
# 类是个模块，可以生成各种不同对象

"""
self与实例方法
"""

class Student():
    # 学生数量
    sum = 0
    name = 'qiyue'
    age = 0

    # 构造函数
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(name)
        print(age)

    def do_homework(self):
        print('homework')


student = Student('Nelson', 18)
print(student.__dict__)

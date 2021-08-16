#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 类-类方法定义
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
类方法

* 如何写类方法？-@classmethod
* 如何调用类方法？-Student.plus_sum()
"""


class Student():
    # 学生数量
    sum = 0

    # 构造函数
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def do_homework(self):
        print('homework')

    # 类方法定义
    # 装饰器，后面高阶函数会学习到：）
    @classmethod
    def plus_sum(cls):  # 类方法形参是 cls，和 self 一样都可以随意改成其他名字，cls 不能代表就是类方法，需要使用装饰器 @classmethod 来修饰才是
        cls.sum += 1  # 在类方法里进行之前在构造函数里操作类变量的语句
        print(cls.sum)


student1 = Student('Nelson', 18)
Student.plus_sum()
student2 = Student('Nelson', 18)
Student.plus_sum()
student3 = Student('Nelson', 18)
Student.plus_sum()

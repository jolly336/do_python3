#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 类-实例方法如何访问类变量？
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
在实例方法中访问实例变量与类变量

* 实例变量中如何访问 sum?
    - 在类外部访问时，大写 Student.sum 获取
    - 在类内部访问时，获取方式 self.__class__.sum
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
        # bug
        # 建议：访问实例变量，带上self.
        print(self.name)
        print(self.__dict__)
        # 读取形参name
        print(name)

        # <built-in function sum> 打印的是内置sum函数
        print(sum)  # 打印不是我们期望的上面类变量 sum

        # 方式二：访问类变量第二种方式
        print(self.__class__.sum)

    def do_homework(self):
        print('homework')


student = Student('Nelson', 18)
# 方式一：访问类变量第一种方式
print(Student.sum)

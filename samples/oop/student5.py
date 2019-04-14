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
        # 访问实例变量，带上self.
        print(self.name)
        print(self.__dict__)
        # 读取形参name
        print(name)

        # <built-in function sum> 打印的是内置sum函数
        print(sum)

        # 访问类变量第二种方式
        print(self.__class__.sum)

    def do_homework(self):
        print('homework')


student = Student('Nelson', 18)
# 访问类变量第一种方式
print(Student.sum)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 类-静态方法
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

    # 构造函数
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def do_homework(self):
        print('homework')

    # 类方法定义
    @classmethod
    def plus_sum(cls):
        cls.sum += 1
        print(cls.sum)
        # print(self.name)

    # 不建议使用静态方法，和面向对象函数没有什么联系
    @staticmethod
    def add(x, y):
        # 静态方法可以访问类变量
        print(Student.sum)
        # print(self.name)
        print('This is a static method.')


student1 = Student('Nelson', 18)
student1.add(1, 2)
Student.add(1, 2)

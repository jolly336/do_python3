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

"""
静态方法

思考：静态方法、实例方法、类方法的区别？

* 静态方法没有强制参数传递指定的名字，self、cls 等 @staticmethod
* 类方法和类关联 @classmethod
* 实例方法和类对象关联
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
    @classmethod
    def plus_sum(cls):
        cls.sum += 1
        print(cls.sum)
        # print(self.name)

    # 不建议使用静态方法，和面向对象函数没有什么联系
    # 装饰器
    @staticmethod
    def add(x, y):
        # 静态方法可以访问类变量
        print(Student.sum)  # 类变量最好放到类方法中使用，这里虽然可以使用，但是麻烦，Student.name，类方法中 cls.name 获取
        # print(self.name) # 访问实例变量？不行~
        print('This is a static method.')


student1 = Student('Nelson', 18)
student1.add(1, 2)  # 对象和类都可以调用静态方法
Student.add(1, 2)

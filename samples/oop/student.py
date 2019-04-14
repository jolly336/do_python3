#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 类
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
    name = ''  # 全局变量
    age = 0

    # 构造函数
    def __init__(self, name, age):
        print('student')
        # 构造函数不能返回字符串
        # return 'student'

        # 初始化对象的属性
        name = name
        age = age

    # 行为 与 特征：方法
    def print_file(self):
        print('name: ' + self.name)
        print('age: ' + str(self.age))

    def do_homework(self):
        print('homework')

    # 类只负责定义，不负责执行，调用要放到外部！
    # TypeError: print_file() missing 1 required positional argument: 'self'
    # print_file()


# 调用放到外部
# student = Student()
# student.print_file()

# 显示调用构造函数，默认返回 None
student = Student('Nelson', 18)
print(student.name)
# a = student.__init__()
# print(a)
# # <class 'NoneType'>
# print(type(a))


class Printer():
    # 打印应该不属于Student，而应属于打印机
    def print_file(self):
        print('name: ' + self.name)
        print('age: ' + str(self.age))

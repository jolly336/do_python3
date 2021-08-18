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

* 定义实例方法时，self 必须出现
* 调用实例方法时，不需要传入对 self 传参
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
        # self 类似 java 的 this?
        # self 为啥要写出来，猜测可能 Python 是为了 显胜于隐~
        # self 代表的是实例，不是类！
        # print(name)  # 不建议这种访问，要访问实例变量 name 最好加上 self.name
        # print(age)
        print(self.name)  # 建议写法，防止形参改了，不加 self 出错~
        print(self.age)

    def do_homework(self):
        print('homework')


student = Student('Nelson', 18)
print(student.__dict__)  # __dict__ 显示实例下的所有成员变量

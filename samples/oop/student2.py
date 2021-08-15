#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 类-「类变量」和「实例变量」
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
内容：类变量和实例变量

思考：为什么要有类变量？？？
"""
class Student():
    # 一个班级里所有学生的总数
    sum = 0
    # 类变量，不是实例变量，区别其他语言 Java
    name = 'qiyue'
    age = 0

    # 构造函数
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def do_homework(self):
        print('homework')


# 显示调用构造函数，默认返回 None
student1 = Student('Nelson', 18)
student2 = Student('Jolly', 18)
# 对象name和类name
print(student1.name)  # 实例变量
print(student2.name)  # 实例变量
print(Student.name)  # 类变量

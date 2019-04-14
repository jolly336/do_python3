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
class Student():
    name = 'qiyue'
    age = 0

    # 构造函数
    def __init__(self, name, age):
        name = name
        age = age
        # self.name = name
        # self.age = age

    def do_homework(self):
        print('homework')


student = Student('Nelson', 18)
# 实例变量，当在实例变量找不到，就会去类里面找，找不到再去父类里找
print(student.name)
# 类变量
print(Student.name)

# 字典，保存当前对象下所有变量
print(student.__dict__)
print(Student.__dict__)
